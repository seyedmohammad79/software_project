from django.urls import path
from . import views

urlpatterns = [
    path('request-payment/', views.request_payment, name='request-payment'),
    path('verify-payment/', views.verify_payment, name='verify-payment'),
]