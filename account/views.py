import json
import bcrypt
import jwt
import requests

import my_settings
from .models import (
    SocialLog,
    Account,
    MarketingAgree,
    SnsConnection,
    RefundAccount,
    UserAdditionalInfo
)
from .utils import login_requested

from django.views import View
from django.http import HttpResponse, JsonResponse
from django.db import IntegrityError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

SECRET_KEY = my_settings.SECRET_KEY

class SignUp(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            validate_email(data['email'])
            if Account.objects.filter(email=data['email']).exists():
                return JsonResponse({'message': "ALEADY_EXISTS_EMAIL"}, status=400)

            password = bcrypt.hashpw(
                data['password'].encode(), bcrypt.gensalt()).decode('utf-8')

            Account(
                username        = data['username'],
                email           = data['email'],
                password        = password,
                agree_location  = False,
                agree_promotion = False,
            ).save()

            return JsonResponse({'message':"SIGNUP_COMPLETE"}, status=200)

        except ValidationError:
            return JsonResponse({"message": "INVALID_EMAIL_FORM"}, status=400)
        except KeyError:
            return JsonResponse({"message": "INVALID_KEYS"}, status=400)

class SignIn(View):
    def post(self, request):
        data = json.loads(request.body)        

        try:
            validate_email(data['email'])
            user = Account.objects.get(email=data['email'])
            if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                access_token = jwt.encode(
                    {'id': user.id}, SECRET_KEY['secret'], algorithm=SECRET_KEY['algorithm'])
                return JsonResponse({'access_token': access_token.decode('utf-8')}, status=200)

            else:
                return JsonResponse({"message": "INVALID_PASSWORD"}, status=401)

        except Account.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'}, status=400)

        except KeyError:
            return JsonResponse({'message': 'INVALID_KEY'}, status=400)

class KakaoSignIn(View):
    def get(self, request):
        try:
            kakao_token = request.headers["Authorization"]
            headers = {'Authorization' : f"Bearer {kakao_token}"}
            urls = "https://kapi.kakao.com/v2/user/me"
            response = requests.get(urls, headers = headers, timeout = 2)
            kakao_userinfo = response.json()

            if Account.objects.filter(sns_id = kakao_userinfo['id']).exists():
                user = Account.objects.get(sns_id = kakao_userinfo['id'])
                token = jwt.encode({"id":user.id}, SECRET_KEY['secret'], SECRET_KEY['algorithm']).decode('utf-8')
                return JsonResponse({"access_token": token}, status = 200)
            
            else:
                Account.objects.create(
                    social_platform_id = SocialLog.objects.get(social = 'kakao').id,
                    sns_id             = kakao_userinfo['id'],
                    email              = kakao_userinfo['kakao_account'].get('email', None),
                    username           = kakao_userinfo['properties'].get('nickname', None)
                )
                user = Account.objects.get(sns_id = kakao_userinfo['id'])
                token = jwt.encode({"id":user.id}, SECRET_KEY['secret'], SECRET_KEY['algorithm']).decode('utf-8')
                return JsonResponse({"access_token": token}, status = 200)
        except KeyError:
            return JsonResponse({"message":"INVALID_KEY"}, status=400)


class NaverSignIn(View):
    def get(self, request):
        try:
            naver_token = request.headers["Authorization"]
            headers = {'Authorization' : f"Bearer {naver_token}"}
            urls = "https://openapi.naver.com/v1/nid/me"
            response = requests.get(urls, headers = headers, timeout = 2)
            naver_userinfo = response.json()

            if Account.objects.filter(sns_id = naver_userinfo['response'].get('id')).exists():
                user = Account.objects.get(sns_id = naver_userinfo['response'].get('id'))
                token = jwt.encode({"id":user.id}, SECRET_KEY['secret'], SECRET_KEY['algorithm']).decode('utf-8')
                return JsonResponse({"access_token": token}, status = 200)
            
            else:
                Account.objects.create(
                    social_platform_id = SocialLog.objects.get(social = 'naver').id,
                    sns_id             = naver_userinfo['response'].get('id',None),
                    email              = naver_userinfo['response'].get('email', None),
                    username           = naver_userinfo['response'].get('name', None)
                )
                user = Account.objects.get(sns_id = naver_userinfo['response'].get('id'))
                token = jwt.encode({"id":user.id}, SECRET_KEY['secret'], SECRET_KEY['algorithm']).decode('utf-8')
                return JsonResponse({"access_token": token}, status = 200)
        except KeyError:
            return JsonResponse({"message":"INVALID_KEY"}, status=400)

class ProfileUpdate(View):
    @login_requested
    def post(self, request):
        data = json.loads(request.body)
        profile = UserAdditionalInfo.objects.get(user = request.agent)
        try:
            profile.marketing_agree.email_receive      = data.get('email_receive', None)
            profile.marketing_agree.sms_receive        = data.get('sms_receive', None)
            profile.marketing_agree.app_receive        = data.get('app_receive', None)
            profile.sns_connection.kakao_connection    = data.get('kakao_connection', None)
            profile.sns_connection.naver_connection    = data.get('naver_connection', None)
            profile.sns_connection.facebook_connection = data.get('facebook_connection', None)
            profile.refund.refund_account              = data.get('refund_account', None)
            profile.refund.refund_bank                 = data.get('refund_bank', None)
            profile.refund.account_holder              = data.get('account_holder', None)
            profile.save()
            return JsonResponse({"message":"UPDATE_COMPLETE"}, status=200)
        except KeyError:
            return JsonResponse({"message":"INVALID_KEY"}, status=400)

    @login_requested
    def get(self, request):
        profile = UserAdditionalInfo.objects.get(user = request.agent)
        try:
            agent_profile = {
                "email_receive"       : profile.marketing_agree.email_receive,
                "sms_receive"         : profile.marketing_agree.sms_receive,
                "app_receive"         : profile.marketing_agree.app_receive,
                "kakao_connection"    : profile.sns_connection.kakao_connection,
                "naver_connection"    : profile.sns_connection.naver_connection,
                "facebook_connection" : profile.sns_connection.facebook_connection,
                "refund_account"      : profile.refund.refund_account,
                "refund_bank"         : profile.refund.refund_bank,
                "account_holder"      : profile.refund.account_holder,
            }
            return JsonResponse({"agent_profile": agent_profile}, status=200)
        except KeyError:
            return JsonResponse({"message":"INVALID_KEY"}, status=400)