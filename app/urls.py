from django.contrib import admin
from django.urls import path
from core.views import weather, api

urlpatterns = [
    path('api/', api, name='api'),
    path('', weather, name='weather'),
    path('admin/', admin.site.urls),
]
