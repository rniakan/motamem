from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=255)


class Post(models.Model):
    title = models.CharField(max_length=255)
    publisher_name = models.CharField(max_length=255)
    publish_date = models.DateField()
    text = models.TextField()
    image = models.ImageField(upload_to='photos/', null=True)
    caption = models.CharField(max_length=255, default="no image")


class UserType(models.Model):
    name = models.CharField(max_length=50)
    permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
    )

    class Meta:
        verbose_name = 'User Type'
        verbose_name_plural = 'User Types'

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.ForeignKey(UserType, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.user.email


class CustomUser(AbstractUser):
    USER = 'user'
    ADMIN = 'admin'
    ROLE_CHOICES = [
        (USER, 'کاربر عادی'),
        (ADMIN, 'مدیر'),
    ]
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, default=USER)

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)