import uuid

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


ROLE_CHOICES = (
    ('admin', 'admin'),
    ('employee', 'employee'),
    ('user', 'user')
)


class UserManager(BaseUserManager):
    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError(_('The email must be set'))
        if not password:
            raise ValueError(_('The password must be set'))
        email = self.normalize_email(email)

        user = User(email=email, **other_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('role', 'admin')
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get('role') != 'admin':
            raise ValueError('Superuser must have admin role')
        return self.create_user(email, password, **other_fields)


class User(AbstractUser):

    first_name = None
    last_name = None

    id = models.UUIDField(primary_key=True, unique=True, editable=False,
                          default=uuid.uuid4, verbose_name='Public identifier')
    email = models.EmailField("Email Address", unique=True)
    username = models.CharField(max_length=20)
    role = models.CharField(max_length=8, choices=ROLE_CHOICES, default='user')

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
