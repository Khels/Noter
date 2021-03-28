from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

User = settings.AUTH_USER_MODEL


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), unique=True)
    avatar = models.ImageField(
        _('avatar'),
        upload_to='notes/',
        blank=True,
        null=True,
        help_text='Here you can upload a photo of yourself'
    )
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
