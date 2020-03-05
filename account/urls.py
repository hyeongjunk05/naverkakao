from django.urls import path
from .views      import (
    SignUp, 
    SignIn, 
    KakaoSignIn, 
    NaverSignIn, 
    ProfileUpdate
)

urlpatterns = [
    path('/signup', SignUp.as_view()),
    path('/signin', SignIn.as_view()),
    path('/signin/kakao', KakaoSignIn.as_view()),
    path('/signin/naver', NaverSignIn.as_view()),
    path('/profileupdate', ProfileUpdate.as_view()),
    
]