from django.db import models
from django.conf import settings
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class NonFractured(models.Model):
    description_not_fractured = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        help_text='Enter the description if the result is Not Fractured',
    )


class Fractured(models.Model):
    description_fractured = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        help_text='Enter the description if the result is Fractured',
    )


class Patient(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.EmailField()
    Phone = models.BigIntegerField()
    Xray = models.FileField(upload_to='Xray/', null=True, verbose_name="Xray Image")
    RESULT_OPTIONS = [
        ('Fractured', 'Fractured'),
        ('Not Fractured', 'Not Fractured'),
    ]
    result = models.CharField(
        max_length=30, 
        choices=RESULT_OPTIONS,
        blank=True,
        null=True,
    )
    fractured_info = models.ForeignKey(Fractured, on_delete=models.CASCADE, related_name='fractured_patients', null=True, blank=True)
    non_fractured_info = models.ForeignKey(NonFractured, on_delete=models.CASCADE, related_name='non_fractured_patients', null=True, blank=True)