from django.conf import settings
from django.db import models

from products.models import Product
# Create your models here.
class Cart(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, null=True)
	item = models.ManyToManyField(Product, through="CartItem")
	user2 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user2", blank=True, null=True)

	def __str__(self):
		return str(self.id)

class CartItem(models.Model):
	cart = models.ForeignKey("Cart")
	item = models.ForeignKey(Product)
	quantity = models.PositiveIntegerField(default=1)
	

