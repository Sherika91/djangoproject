from django.urls import path
from users.apps import UsersConfig
from users.views import (RegisterView, ProfileView, generate_new_password, LoginView, LogoutView,
                         ConfirmEmailView, ConfirmationSentView, password_reset, EmailConfirmedView,
                         EmailConfirmationFailedView)

app_name = UsersConfig.name


urlpatterns = [
     path('', LoginView.as_view(template_name='users/login.html'), name='login'),
     path('logout/', LogoutView.as_view(), name='logout'),
     path('register/', RegisterView.as_view(), name='register'),
     path('email_confirmation_sent/', ConfirmationSentView.as_view(), name='email_confirmation_sent'),
     path('confirm_email/<str:uidb64>/<str:token>/', ConfirmEmailView.as_view(), name='confirm_email'),
     path('email_confirmed/', EmailConfirmedView.as_view(), name='email_confirmed'),
     path('emaol_confrimation_failed/', EmailConfirmationFailedView.as_view(), name='email_confirmation_failed'),
     path('profile/', ProfileView.as_view(), name='profile'),
     path('profile/genpassword', generate_new_password, name='genpassword'),
     path('password_reset/', password_reset, name='password_reset'),

]
