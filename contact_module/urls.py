from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactUsVIew.as_view(), name='contact_us_page')
]
