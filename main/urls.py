from django.urls import path

from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('thanks', views.thank_you, name='thank_you'),
    path('submit', views.contact, name='contact')
]