from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string


# Create your models here.

"""
class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, unique=False)
    identification_card = models.CharField(max_length=20, blank=True, null=True)
    token = models.CharField(max_length=500, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    birthdate = models.CharField(max_length=500, blank=True, null=True)
    #sucursal = models.ForeignKey(Sucursal, blank=True, null=True, related_name="fk_sucursal_user", on_delete=models.CASCADE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['user_type']

    def generate_verification_token(self):
        self.token = get_random_string(length=32)

    class Meta:
        unique_together = (('email', 'company_key'))


"""




