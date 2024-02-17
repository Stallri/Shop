from django.urls import path

from products.views import ProductListAPI, ProductAPI, CategoryListAPI, PopularProductsAPI

urlpatterns = [
    path('categories/<slug:gender>/', CategoryListAPI.as_view(), name='category_list'),
    path('products/<slug:category>/', ProductListAPI.as_view(), name='product_list'),
    path('product/<slug:slug>/', ProductAPI.as_view(), name='product_detail'),
    path('popular-products/', PopularProductsAPI.as_view(), name='popular_products'),
]