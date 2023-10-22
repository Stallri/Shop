from django.db import models

from products.models import Product
from account.models import User
from ordering.models import Order


class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product}'

    class Meta:
        verbose_name = 'Товар корзины'
        verbose_name_plural = 'Товары корзины'
