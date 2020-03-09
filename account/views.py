import json
import bcrypt
import jwt

import my_settings
<<<<<<< HEAD
from .models import *
=======
from .models import Account
>>>>>>> 5801240c9d54601e005ce713d08d425669d0691d
from .utils import login_requested

from django.views import View
from django.http import HttpResponse, JsonResponse
from django.db import IntegrityError
from django.shortcuts import redirect
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
<<<<<<< HEAD
                username        = data['username'],
                email           = data['email'],
                password        = password,
                agree_location  = False,
                agree_promotion = False,
=======
                username=data['username'],
                email=data['email'],
                password=password,
                agree_location=False,
                agree_promotion=False,
>>>>>>> 5801240c9d54601e005ce713d08d425669d0691d
            ).save()

            return HttpResponse(status=200)

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

<<<<<<< HEAD
class KakaoSignIn(View):
    def get(self, request):
        kakao_token = request.headers["Authorization"]
        headers = {'Athorization' : f"Bearer {kakao_token}"}
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

class NaverSignIn(View):
    def get(self, request):
        naver_token = request.headers["Authorization"]
        headers = {'Athorization' : f"Bearer {naver_token}"}
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

=======
>>>>>>> 5801240c9d54601e005ce713d08d425669d0691d
class ProfileUpdate(View):
    @login_requested
    def post(self, request):
        data = json.loads(request.body)
        profile = Account.objects.get(id = request.agent.id)
        try:
            if data.get('username'):
                profile.username = data.get('username')
            if data.get('phone'):
                profile.phone    = data.get('phone')
            if data.get('email'):
                profile.email    = data.get('email')
            profile.save()
            return JsonResponse({'message':'USERINFO_CHANGED'}, status=200)
        except KeyError:
            return JsonResponse({'message':'INVALID_KEY'}, status=400)

    @login_requested
    def get(self, request):
        profile = Account.objects.get(id = request.agent.id)
        try:
            agent_profile = {
                "username"      : profile.username,
                "email"         : profile.email,
                "phone"         : profile.phone
            }
            return JsonResponse({"agent_profile": agent_profile}, status=200)
        except KeyError:
            return JsonResponse({"message":"INVALID_KEY"}, status=400)