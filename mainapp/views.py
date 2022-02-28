#? Built-in Imports
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from django.utils.translation import gettext_lazy as _
from django.contrib import messages

#? Authenticaion Imports
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView,
)

#? Generic Views Imports
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.detail import DetailView


#? Local App Imports
from mainapp.forms import (
    UserForm,
    CustomAuthenticationForm, 
    CustomPasswordResetForm, 
    CustomSetPasswordForm, 
    CustomePasswordChangeForm,
    CustomUserCreationForm
)

UserModel = get_user_model()

class LandingPageView(TemplateView):
    template_name = 'base.html'  

class ProfileView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('mainapp:login-view')
    template_name = 'mainapp/profile.html'

class Login(LoginView):
    template_name = 'mainapp/registration/login.html'
    next_page = reverse_lazy('mainapp:profile-view')
    form_class = CustomAuthenticationForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.next_page)
        messages.success(request, _('Logged in successfully!'))
        return super().get(request, *args, **kwargs)
    
class Logout(TemplateView):
    template_name =  "mainapp/loginCofirm.html"

    def get(self, request, *args, **kwargs):
        messages.success(request, _('Logged out successfully.'))
        return super().get(request, *args, **kwargs)

class LogoutDone(LogoutView):
    template_name = "mainapp/registration/logout.html"
    # next_page = reverse_lazy('mainapp:logout-view')
    
class Register(FormView):
    template_name = 'mainapp/registration/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('mainapp:register-done-view')
    
    def get(self, request, *args, **kwargs):
        messages.success(request, _('Account created successfully!'))
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class RegisterDone(TemplateView):
    title = _('Account created!')
    template_name = 'mainapp/register_done.html'

class EditProfile(LoginRequiredMixin, UpdateView):
    template_name = 'mainapp/edit_profile.html'
    form_class = UserForm

    def get_queryset(self):
        user = self.request.user
        return UserModel.objects.filter(email=user)
    
    def get_success_url(self) -> str:
        return reverse("mainapp:edit-done-view", kwargs={'pk':self.get_object().id})
    

class EditProfileDone(LoginRequiredMixin, UpdateView):
    template_name = 'mainapp/edit_profile.html'
    form_class = UserForm

    def get_queryset(self):
        user = self.request.user
        return UserModel.objects.filter(email=user)


#? Password Management
class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    login_url = reverse_lazy('mainapp:login-view')
    template_name = 'mainapp/registration/password_change_form.html'
    success_url = reverse_lazy('mainapp:change-done-view')
    form_class = CustomePasswordChangeForm

class PasswordChangeDone(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'mainapp/registration/password_change_done.html'

class PasswordReset(PasswordResetView):
    title = _('Reset your password')
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('mainapp:reset-done')
    template_name = 'mainapp/registration/password_reset_form.html'
    email_template_name = 'mainapp/registration/password_reset_email.html'
    subject_template_name = 'mainapp/registration/password_reset_subject.txt'

    def get(self, request, *args, **kwargs):
        messages.success(request, _('Password reset sent. Please check your email inbox.'))
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = UserModel.objects.filter(email=email)
        if not user.exists():
            form.add_error('email', _("We can't find a user with that e-mail address."))
            return self.form_invalid(form)
        return super().form_valid(form)

class PasswordResetDone(PasswordResetDoneView):
    template_name = 'mainapp/registration/password_reset_done.html'
    
class PasswordResetConfirm(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('mainapp:reset-complete')
    template_name = 'mainapp/registration/password_reset_confirm.html'

class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'mainapp/registration/password_reset_complete.html'

