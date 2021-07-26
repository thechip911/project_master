from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField

from accounts.managers import UserManager
from utils.messages import HELP_TEXTS


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(
        _("User Name"),
        max_length=200,
    )

    mobile_number = PhoneNumberField(
        _('mobile number'),
        null=True,
        blank=True
    )

    email = models.EmailField(
        _("Email"),
        max_length=150,
        unique=True,
    )

    is_admin = models.BooleanField(
        _('Is Project Admin'),
        default=False,
        help_text=HELP_TEXTS['IS_PROJECT_ADMIN'],
    )

    is_employee = models.BooleanField(
        _('Is Employee'),
        default=False,
        help_text=HELP_TEXTS['IS_PROJECT_ADMIN'],
    )

    is_staff = models.BooleanField(
        _('Is Staff'),
        default=False,
        help_text=HELP_TEXTS['IS_STAFF'],
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ('-id',)
        verbose_name_plural = 'User'

    def __str__(self):
        return f'{self.name} | ({self.email})'

    @property
    def sys_id(self):
        return f'USR-{str(self.id).zfill(6)}'
