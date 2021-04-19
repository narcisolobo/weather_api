from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('weather.routes')),
    path('admin/', admin.site.urls),
]