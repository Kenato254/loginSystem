from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

#? Auth import
from django.contrib.auth import password_validation
from django.contrib.auth.forms import (
    PasswordResetForm, 
    SetPasswordForm, 
    PasswordChangeForm, 
    UserCreationForm
)
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

#? User model
UserModel = get_user_model()
class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ("first_name", "last_name", "date_of_birth")
        widgets = {
            "first_name": forms.TextInput(attrs={
                "class":"appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm",
                "placeholder": "First name"
            }),
            "last_name": forms.TextInput(attrs={
                "class":"appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm",
                "placeholder": "Last name"
            }),
        }

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={  
            "class": "appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm",
            "placeholder": "Create password",
            "required":"",
            "autocomplete":"new-password"
        }),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            "class": "appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm",
            "placeholder": "Confirm password",
            "required":"",
            "autocomplete":"new-password"
        }),
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = UserModel
        fields = ('email', )
        widgets = {
            'email': forms.EmailInput(attrs={
                "class":"appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm",
                "placeholder": "Email address",
                "required":'',
                "autocomplete":"email"
            }),
        }

class CustomePasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password check"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            "class": "appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm",
            "placeholder": "Old password",
            "required":"",
        })
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={  
            "class": "appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm",
            "placeholder": "New password",
            "required":"",
            "autocomplete":"new-password"
        }),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            "class": "appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm",
            "placeholder": "Confirm password",
            "required":"",
            "autocomplete":"new-password"
        }),
    )

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={  
            "class": "appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm",
            "placeholder": "New password",
            "required":"",
            "autocomplete":"new-password"
        }),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            "class": "appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm",
            "placeholder": "Confirm password",
            "required":"",
            "autocomplete":"new-password"
        }),
    )   

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={
            "class":"appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm",
            'autocomplete': 'email',
            'placeholder': 'Email address'
        })
    )

class CustomAuthenticationForm(forms.ModelForm):

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(email)s and password. Note that password "
            "field may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
        'email_error':_('User with this email does not exist.'),
        'password_error':_('Password is incorrect.'),
    }
    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

        # Gets the USERNAME_FIELd which is email field in this case.
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
    
    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            email_check = UserModel.objects.filter(email=email)
            if not email_check.exists():
                raise self.get_email_error()
            if not email_check[0].check_password(password):
                raise self.get_password_incorrect()

            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
    
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(
                self.error_messages['inactive'],
                code='inactive'
            )
    
    def get_user(self):
        return self.user_cache
    
    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
            params={'email': self.username_field.verbose_name},
        )
    
    def get_email_error(self):
        return ValidationError(
            self.error_messages['email_error'],
            code='email_error',
            params={'email': self.username_field.verbose_name},
        )

    def get_password_incorrect(self):
        return ValidationError(
            self.error_messages['password_error'],
            code='password_error',
            params={'password': _('password field.')}
        )

    class Meta:
        model = UserModel
        fields = ("email", 'password')
        widgets = {
            'email': forms.EmailInput(attrs={
                "class":"appearance-none rounded-t-md relative block w-96 px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm",
                "placeholder": "Email address",
                "required":'',
                "autocomplete":"email"
            }),

            'password': forms.PasswordInput(attrs={
                "class": "appearance-none rounded relative block w-96 px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm",
                "placeholder": "Password",
                "required":"",
                "autocomplete":"current-password"
            })
        } 