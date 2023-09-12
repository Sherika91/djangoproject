from django.views.generic import CreateView, UpdateView
from django.core.mail import send_mail
from django.shortcuts import redirect, reverse, render
from config import settings
from users.forms import UserRegisterForm, UserProfileForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from users.models import User
from django.views import View
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as BaseLoginView, PasswordResetDoneView
from django.contrib.auth.views import LogoutView as BaseLogoutView
import string
import random


class LoginView(BaseLoginView):
    """Login on website"""
    title = 'Login'
    template_name = 'users/login.html'
    success_url = reverse_lazy('catalog:index')


class LogoutView(BaseLogoutView):
    """Logout from website"""
    template_name = 'users/login.html'
    success_url = reverse_lazy('catalog:index')


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    title = 'New user registration'

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.save()
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        activation_url = reverse_lazy('users:confirm_email', kwargs={'uidb64': uid, 'token': token})
        current_site = get_current_site(self.request)

        send_mail(
            recipient_list=[user.email],
            subject='Registration on the site',
            message=f'You have successfully registered on the site, please activate your account by clicking on the '
                    f'link: http://{current_site}{activation_url}"',
            from_email=settings.EMAIL_HOST_USER
        )

        return redirect('users:email_confirmation_sent')


class ConfirmationSentView(PasswordResetDoneView):
    """User confirmation sent"""
    template_name = "users/includes/inc_email_confirmation_sent.html"


class ConfirmEmailView(View):
    """Confirm user email"""
    def get(self, request, *args, **kwargs):
        try:
            uid = urlsafe_base64_decode(kwargs['uidb64']).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, kwargs['token']):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('users:email_confirmed')
        else:
            return redirect('users:email_confirmation_failed')


class EmailConfirmedView(TemplateView):
    """Email confirmation success"""
    template_name = 'users/includes/inc_email_confirmed.html'
    title = "Your email is activated."


class EmailConfirmationFailedView(TemplateView):
    """Email confirmation failed"""
    template_name = 'users/includes/inc_email_confirmation_failed.html'
    title = "Email confirmation failed"


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/profile.html'

    def get_object(self, queryset=None):
        return self.request.user


@login_required
def generate_new_password(request):
    """Generate new password and send it to user email"""
    characters = string.ascii_letters + string.digits
    new_password = ''.join([str(random.choice(characters)) for _ in range(12)])
    send_mail(
        subject="You've changed your password",
        message=f'You have successfully changed your password, your new password: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )

    request.user.set_password(new_password)
    request.user.save()

    return redirect(reverse('catalog:index'))


def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            characters = string.ascii_letters + string.digits
            new_password = ''.join([str(random.choice(characters)) for _ in range(12)])
            user.set_password(new_password)
            user.save()

            send_mail(
                subject="You've changed your password",
                message=f'You have successfully changed your password, your new password: {new_password}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email]
            )
            return redirect(reverse("users:login"))  # Перенаправление на страницу входа
        except User.DoesNotExist:
            return render(request, 'users/includes/inc_password_reset_form.html',
                          {'error_message': 'User not found'})  # error message if user not found
    return render(request, 'users/includes/inc_password_reset_form.html')
