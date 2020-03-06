import jwt
import bcrypt

import my_settings
from .models import Account

from django.http import JsonResponse, HttpResponse

SECRET_KEY = my_settings.SECRET_KEY


def login_requested(func):
    def wrapper(self, request, *args, **kwargs):
        access_token = request.headers.get('Authorization', None)

        try:
            token_decoded = jwt.decode(
                access_token, SECRET_KEY['secret'], SECRET_KEY['algorithm'])  # ['email']
            #agent_id = decode["user"]
            agent = Account.objects.get(id=token_decoded["id"])
            request.agent = agent

        except jwt.DecodeError:
            return JsonResponse({'message' : 'INVALID_USER'}, status=401)

        except Account.DoesNotExist:
            return JsonResponse({"message": "INVALID_TOKEN"}, status=401)

        return func(self, request, *args, **kwargs)
    return wrapper