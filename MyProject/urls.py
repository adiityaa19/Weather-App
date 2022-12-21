from django.contrib import admin
from django.urls import path, include
from WeatherApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('weather/',views.weather,name="weather"),
    path('delete/<CName>',views.delete_city,name="DCity")
]
