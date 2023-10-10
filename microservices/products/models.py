from django.db import models

# Create your models here.

class Products(models.Model):
	name = models.CharField('Nom du produit', max_length=255, null=False, blank=False)

	def __str__(self):
		return self.name