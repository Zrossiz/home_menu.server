from django.urls import path
from .views import TimeToCookAPIView

urlpatterns = [
    path('', TimeToCookAPIView.as_view()),
    path('<int:pk>/', TimeToCookAPIView.as_view())
]