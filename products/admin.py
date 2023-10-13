from django.contrib import admin
from .models import Product, ProductPhoto, Comment, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductPhoto)
class ProductPhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
