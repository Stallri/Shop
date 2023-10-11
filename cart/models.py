from django.db import models

from products.models import Product
from account.models import User


class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    