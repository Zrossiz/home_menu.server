from django.urls import path
from .views import CreateCategoryAPIView

urlpatterns = [
    path('', CreateCategoryAPIView.as_view())
]