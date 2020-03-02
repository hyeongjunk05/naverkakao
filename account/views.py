import json
import bcrypt
import jwt

import my_settings
from .models import Account
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
                username=data['username'],
                email=data['email'],
                password=password,
                agree_location=False,
                agree_promotion=False,
            ).save()  # social login만 추가.

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


class KakaoSignIn(View):
    def get(self, request):
        client_id = SECRET_KEY['kakao']
        redirect_uri = "http://127.0.0.1:8000/account/signin/kakao"

        return redirect(
            f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
        )

# class KakaoSignInToken(View):
#     def get(self, request):

#         try:
#             code = request.GET.get("code")
#             client_id = SECRET_KEY['kakao']
#             redirect_uri = "http://127.0.0.1:8000/account/signin/kakao"

#             token = request.get(f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}"
#             )

#             token_json = token_request.json()

#             error = token_json.get("error", None)

#             access_token = token_json.get("access_token")

#             profile_request = request.get("https://kapi.kakao.com/v2/user/me", headers={"Authorization" : f"Bearer {access_token}"},
#             )
        
#             profile_json = profile_request.json()

#             kakao_account = profile_json.get("kakao_account")
#             email = kakao_account.get("email", None)
#             kakao_id = profile_json.get('id')
        
#         except KeyError:
#             return JsonResponse({"message":"INVALID_TOKEN"}, status = 400)

#         if Account.objects.filter(kakao_id = kakao_id).exists():
#             user = Account.objects.get(kakao_id = kakao_id)
#             token = jwt.encode({"email" : email}, SECRET_KEY, algorithm = "HS256")
#             token = token.decode("utf-8")

#             return JsonResponse({"token" : token}, status=200)

#         else :
#             Account(
#                 kakao_id = kakao_id,
#                 email    = email,
#             ).save()

#             token = jwt.encode({"email" : email}, SECRET_KEY, algorithm = "HS256")
#             token = token.decode("utf-8")

#             return JsonResponse({"token" : token}, status = 200)

# class Profile(View):
#     @login_requested
#     def post(self, request):
#         data = json.loads(request.body)

# class Oauthh(View):
#     def oauth(self, request):
#         code = request.GET('code')
#         print('code = ' + str(code))

#         return redirect('blogMain')

# def detail(request):
#     login_request_uri = 'https://kauth.kakao.com/oauth/authorize?'
 
#     client_id = '6c1099960cb0fa31091beb2228746350'
#     redirect_uri = 'http://127.0.0.1:8000/oauth'
 
#     login_request_uri += 'client_id=' + client_id
#     login_request_uri += '&redirect_uri=' + redirect_uri
#     login_request_uri += '&response_type=code'
