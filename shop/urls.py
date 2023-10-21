"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from account.views import RegistrationAPIView, ProfileAPIView
from products.views import ProductListAPI, ProductAPI, CategoryListAPI, PopularProductsAPI
from cart.views import CartAPIView, CartAddAPIView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/shop/categories/<str:gender>/', CategoryListAPI.as_view(), name='category_list'),
    path('api/shop/products/<str:category>/', ProductListAPI.as_view(), name='product_list'),
    path('api/shop/product/<slug:slug>/', ProductAPI.as_view(), name='product_detail'),
    path('api/shop/popular-products/', PopularProductsAPI.as_view(), name='popular_products'),

    path('api/cart/', CartAPIView.as_view(), name='cart_list'),
    path('api/cart/add/<slug:slug>/', CartAddAPIView.as_view(), name='cart_add'),

    path('api/registration/', RegistrationAPIView.as_view(), name='registration'),
    path('api/profile/', ProfileAPIView.as_view(), name='profile'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [path("__debug__/", include("debug_toolbar.urls")), ] + urlpatterns
