from django.contrib import admin
from django.urls import path, include
from django.urls import path, include
from django.shortcuts import redirect


urlpatterns = [
    path('', lambda request: redirect('credit_card_form')),
    path('admin/', admin.site.urls),
    path('credit-card/', include('credit_card_app.urls')),
]
