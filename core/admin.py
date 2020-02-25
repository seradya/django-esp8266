from django.contrib import admin
from .models import Weather


class WeatherAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Weather._meta.fields]

admin.site.register(Weather, WeatherAdmin)