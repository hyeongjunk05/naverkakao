from django.urls import path
from .views      import MainView, ProductView

urlpatterns = [
    path('', MainView.as_view()),
    path('/<int:product_id>', ProductView.as_view())
]