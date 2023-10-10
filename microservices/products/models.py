from django.db import models

# Create your models here.

class Products(models.Model):
	Name = models.CharField('Nom du produit', max_length=255, null=False, blank=False)
	Quantity = models.IntegerField('Quantité', null=False, default=0)
	Price = models.FloatField('Prix du produit', null=False, default=0.00)
	DISPONIBILITE = models.BooleanField('Disponible', default=False)

	def __str__(self):
		return self.Name
