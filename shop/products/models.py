from django.conf import settings
from django.db import models

from discounts.models import Discount


class Product(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE,
                                 verbose_name='Категория')
    number_of_sold = models.PositiveIntegerField(verbose_name='Количество проданных товаров', default=0)
    available = models.BooleanField(default=True, verbose_name='Наличие')
    discount = models.ForeignKey(Discount, related_name='products', blank=True, null=True, on_delete=models.SET_NULL,
                                 verbose_name='Скидка')
    price = models.PositiveIntegerField(verbose_name='Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'


class ProductPhoto(models.Model):
    photo = models.ImageField(upload_to='image', verbose_name='Фотография')
    product = models.ForeignKey('Product', related_name='photos', on_delete=models.CASCADE,
                                verbose_name='Товар')

    def __str__(self):
        return f'photo to "{self.product.title}"'

    class Meta:
        verbose_name = 'Фотографии товаров'
        verbose_name_plural = 'Фотографии товаров'


class Category(models.Model):
    GENDER_CHOICE = [
        ('man', 'Мужчинам'),
        ('woman', 'Женщинам'),
        ('boy', 'Мальчикам'),
        ('girl', 'Девочкам'),
    ]
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    title = models.CharField(max_length=255, verbose_name='Название')
    gender = models.CharField(max_length=5, choices=GENDER_CHOICE, verbose_name='Пол')

    def __str__(self):
        return f'{self.title} ({self.get_gender_display()})'

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


class Comment(models.Model):
    stars = models.PositiveIntegerField(verbose_name='Звёзды')
    content = models.TextField(verbose_name='Текст')
    product = models.ForeignKey('Product', related_name='comments', on_delete=models.CASCADE,
                                verbose_name='Товар')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE,
                             verbose_name='Пользователь')

    def __str__(self):
        return f'comment from {self.user.email}to "{self.product.title}"'

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'
