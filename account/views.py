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