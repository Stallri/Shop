from django.contrib import admin
from .models import Product, ProductPhoto, Comment, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'available', 'number_of_sold', 'price')
    ordering = ('category', 'number_of_sold')


@admin.register(ProductPhoto)
class ProductPhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'gender')
    ordering = ('gender',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
