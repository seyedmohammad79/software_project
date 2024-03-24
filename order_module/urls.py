from django.urls import path
from . import views

urlpatterns = [
   # path('add-to-order', '', name='add_to_order'),
    path('request-payment/', views.request_payment, name='request-payment'),
    path('verify-payment/', views.verify_payment, name='verify-payment'),
]
