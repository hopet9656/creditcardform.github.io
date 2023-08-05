from django.urls import path
from . import views

urlpatterns = [
    path('', views.credit_card_form, name='credit_card_form'),
    path('success/', views.success, name='success'),
]
