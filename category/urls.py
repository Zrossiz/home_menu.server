from django.urls import path
from .views import CategoryListAPIView

urlpatterns = [
    path('', CategoryListAPIView.as_view()),
    path('<int:pk>/', CategoryListAPIView.as_view())
]