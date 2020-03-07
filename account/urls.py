from django.urls import path
from .views      import SignUp, SignIn, ProfileUpdate

urlpatterns = [
    path('/signup', SignUp.as_view()),
    path('/signin', SignIn.as_view()),
    path('/profileupdate', ProfileUpdate.as_view()),
]