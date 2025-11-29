from django.urls import path
from . import views

app_name = 'specc_site'

urlpatterns = [
    path('', views.home, name='home'),
]
