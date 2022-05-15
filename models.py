from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        email = email.lower()  # makes email all lower case (not necessary)

        user = self.model(
            email=email,
            name=name
        )

        user.set_password(password)  # hash password
        user.save(using=self._db)  # save to correct database

        return user


class UserAcc(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)  # 1 byte
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
