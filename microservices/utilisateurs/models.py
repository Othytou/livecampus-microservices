from django.db import models
# Un modele d'identification de Djangdo
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Si on veut personaliser des champs
    # AbstractUser comprend id, username, email, firstname et lastname
    age = models.PositiveBigIntegerField(null=True, blank=True) 