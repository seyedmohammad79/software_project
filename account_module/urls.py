from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_page'),
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('logout/', views.logout_user, name='logout_page'),
    path('register/', views.RegisterView.as_view(), name='register_page'),
    path('activate-account/<email_activate_url>', views.RegisterView.as_view(), name='activate_account'),
    path('forget-password/', views.ForgetPasswordView.as_view(), name='forget_password'),
    path('authenticate/<email_activate_url>', views.AuthenticateView.as_view(), name='authenticate_page'),
    path('reset_pass/<email_activate_url>', views.ResetPasswordView.as_view(), name='reset_pass_page'),
    path('api/users/', views.UserApiView.as_view())
]
