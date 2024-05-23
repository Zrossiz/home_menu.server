from django.urls import path
from .views import CreateTimeToCookAPIView

urlpatterns = [
    path('', CreateTimeToCookAPIView.as_view())
]