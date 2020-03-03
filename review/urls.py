from django.urls import path
from .views      import CreateReview, UpadteReview, DeleteReview

urlpatterns = [
    path('/<int:product_id>', CreateReview.as_view()),
    path('/update/<int:product_id>/<int:review_id>', UpadteReview.as_view()),
    path('/delete/<int:product_id>/<int:review_id>', DeleteReview.as_view()),
]