from django.contrib import admin
from .models import Product, ProductPhoto, Comment, Category


class ProductPhotoTabularInline(admin.TabularInline):
    model = ProductPhoto


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'available', 'discount', 'price')
    ordering = ('category', 'number_of_sold')
    inlines = [ProductPhotoTabularInline]


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'gender')
    ordering = ('gender',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
