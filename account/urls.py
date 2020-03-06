from django.urls import path
from .views      import SignUp, SignIn, KakaoSignIn

urlpatterns = [
    path('/signup', SignUp.as_view()),
    path('/signin', SignIn.as_view()),
    path('/signin/kakao', KakaoSignIn.as_view()),
]