from django.urls import path
<<<<<<< HEAD
from .views      import SignUp, SignIn, KakaoSignIn, NaverSignIn, ProfileUpdate
=======
from .views      import SignUp, SignIn, ProfileUpdate
>>>>>>> 5801240c9d54601e005ce713d08d425669d0691d

urlpatterns = [
    path('/signup', SignUp.as_view()),
    path('/signin', SignIn.as_view()),
<<<<<<< HEAD
    path('/signin/kakao', KakaoSignIn.as_view()),
    path('/signin/naver', NaverSignIn.as_view()),
    path('/profileupdate', ProfileUpdate.as_view()),
    
=======
    path('/profileupdate', ProfileUpdate.as_view()),
>>>>>>> 5801240c9d54601e005ce713d08d425669d0691d
]