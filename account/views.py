import json
import bcrypt
import jwt
import requests

import my_settings
from .models import Account, SocialLog
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
                username=data['username'],
                email=data['email'],
                password=password,
                agree_location=False,
                agree_promotion=False,
            ).save()  # social login만 추가.

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
        kakao_token = request.headers["Authorization"]
        headers = {'Athorization' : f"Bearer {kakao_token}"}
        urls = "https://kapi.kakao.com/v2/user/me"
        response = requests.get(urls, headers = headers, timeout = 2)
        kakao_userinfo = response.json()
        print('ddddd')

        if Account.objects.filter(sns_id = kakao_userinfo['id']).exists():
            user = Account.objects.get(sns_id = kakao_userinfo['id'])
            token = jwt.encode({"id":user.id}, SECRET_KEY['secret'], SECRET_KEY['algorithm']).decode('utf-8')
            print('aaaaa')
            return JsonResponse({"access_token": token}, status = 200)
        
        else:
            Account.objects.create(
                social_platform_id = SocialPlatform.objects.get(social = 'kakao').id,
                sns_id             = kakao_userinfo['id'],
                email              = kakao_userinfo['kakao_account'].get('email', None),
                username           = kakao_userinfo['properties'].get('nickname', None)
            )
            user = Account.objects.get(sns_id = kakao_userinfo['id'])
            token = jwt.encode({"id":user.id}, SECRET_KEY['secret'], SECRET_KEY['algorithm']).decode('utf-8')
            print('kkkk')
            return JsonResponse({"access_token": token}, status = 200)



