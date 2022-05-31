from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )

    LANGUAGE_KR = "kr"
    LANGUAGE_EN = "en"
    LANGUAGE_CHOICES = (
        (LANGUAGE_KR, "한국어"),
        (LANGUAGE_EN, "English"),
    )

    CURRENCY_KST = "KST"
    CURRENCY_USD = "USD"
    CURRENCY_CHOICES = (
        (CURRENCY_KST, "KST"),
        (CURRENCY_USD, "USD"),
    )

    avatar = models.ImageField(
        blank=True,
    )
    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=10,
        blank=True,
    )
    bio = models.TextField(
        blank=True,
    )

    language = models.CharField(
        choices=LANGUAGE_CHOICES,
        max_length=2,
        blank=True,
    )

    currency = models.CharField(
        choices=CURRENCY_CHOICES,
        max_length=10,
        blank=True,
    )

    birthdate = models.DateField(
        null=True,
        blank=True,
    )
    superhost = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.username
