from django.db import models

from django.utils import timezone
from django.utils.translation import gettext_lazy as _

#? Authentication built-ins and models
from django.contrib import auth
from django.contrib.auth.models import (
    AbstractBaseUser, 
    BaseUserManager, 
    PermissionsMixin, 
    Group, 
    Permission
)
#? Validators Built-ins
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if email and password:
            validate_email(email)
            validate_password(password)

            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save()
            return user
        else:
            raise ValueError(_('The Email must be set.'))
    
    def create_superuser(self, email, password, **extra_fields):
        """
        ? Create and save a SuperUser with the given email and password.
        """
        #* Set Superuser properties
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        #* Check superuser properties are well set
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff = True'))
        if extra_fields.get('is_active') is not True:
            raise ValueError(_('Superuser must have is_active = True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser = True'))
        
        return self.create_user(email, password, **extra_fields)

    def with_perm(self, perm, is_active=True, include_superusers=True, backend=None, obj=None):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    'You have multiple authentication backends configured and '
                    'therefore must provide the `backend` argument.'
                )
        elif not isinstance(backend, str):
            raise TypeError(
                'backend must be a dotted import path string (got %r).'
                % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, 'with_perm'):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    ? Creating own custom AbstractUser
    """
    email = models.EmailField(
        _('email address'), 
        max_length=150,
        unique=True,
        help_text=_('Required. example@domain.com.'),
        validators=[validate_email],
        error_messages={
            'unique': _("A user with that email address already exists."),
        },
    )
    username = models.CharField(max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    date_of_birth = models.DateField('Date of birth.', blank=True, null=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="customuser_set",
        related_query_name="customuser",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="customuser_set",
        related_query_name="customuser",
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    objects =  CustomUserManager()

    def get_full_name(self) -> str:
        return '%s %s'%(self.first_name, self.last_name)
    
    def get_email_user(self) -> str:
        return '{}'.format(self.email)
