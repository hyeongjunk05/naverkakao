from django.urls import path
from .views      import MainView, ProductView, SearchView

urlpatterns = [
    path('/<str:category>', MainView.as_view()),
    path('/<int:product_id>', ProductView.as_view()),
    path('/cities/<str:category>', SearchView.as_view())
]