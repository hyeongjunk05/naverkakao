from django.urls import path
from .views      import *

urlpatterns = [
    path('/create/<int:product_id>', CreateReview.as_view()),
    path('/update/<int:product_id>', UpadteReview.as_view()),
    path('/delete/<int:product_id>', DeleteReview.as_view()),
    path('/read/<int:product_id>',   ReadReview.as_view()),
]