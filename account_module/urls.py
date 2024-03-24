from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index_page'),
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('logout/', views.logout_user, name='logout_page'),
    path('register/', views.RegisterView.as_view(), name='register_page'),
    path('activate-account/<email_active_url>', views.ActivateUserView.as_view(), name='activate_account'),
    path('forget-password/', views.ForgetPasswordView.as_view(), name='forget_password'),
    path('authenticate/', views.AuthenticateEmailView.as_view(), name='authenticate_email'),
    path('authenticate/<email_active_url>', views.AuthenticateView.as_view(), name='authenticate_page'),
    path('reset-pass/<email_active_url>', views.ResetPasswordView.as_view(), name='reset_pass_page'),
    path('api/users/', views.UserApiView.as_view())
]
