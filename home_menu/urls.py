from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/category/', include('category.urls')),
    path('api/dish', include('dish.urls')),
    path('api/time_to_cook', include('time_to_cook.urls'))
]
