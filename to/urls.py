
from django.contrib import admin
from django.urls import path
from app_to.views import app_start, list_obj, data_obj


urlpatterns = [
    path('admin/', admin.site.urls),
    path('title/', app_start, name='app_start'),
    path('<int:pk>/', list_obj, name='list_objects'),
    path('data_obj/<int:pk>/', data_obj, name='data_obj'),
]




