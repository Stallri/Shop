from django.conf import settings
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class ProductPhoto(models.Model):
    photo = models.ImageField(upload_to='image')
    product = models.ForeignKey('Product', related_name='photos', on_delete=models.CASCADE)

    def __str__(self):
        return f'photo to "{self.product.title}"'


class Comment(models.Model):
    stars = models.PositiveIntegerField()
    content = models.TextField()
    product = models.ForeignKey('Product', related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f'comment from {self.user.email}to "{self.product.title}"'
