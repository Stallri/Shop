from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from account.views import RegistrationAPIView, ProfileAPIView
from products.views import ProductListAPI, ProductAPI, CategoryListAPI, PopularProductsAPI
from cart.views import CartAPIView, CartAddAPIView
from ordering.views import OrderAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),

    path('api/shop/categories/<str:gender>/', CategoryListAPI.as_view(), name='category_list'),
    path('api/shop/products/<str:category>/', ProductListAPI.as_view(), name='product_list'),
    path('api/shop/product/<slug:slug>/', ProductAPI.as_view(), name='product_detail'),
    path('api/shop/popular-products/', PopularProductsAPI.as_view(), name='popular_products'),

    path('api/cart/', CartAPIView.as_view(), name='cart_list'),
    path('api/cart/<slug:slug>/', CartAddAPIView.as_view(), name='cart_add'),

    path('api/order/', OrderAPI.as_view(), name='ordering'),

    path('api/registration/', RegistrationAPIView.as_view(), name='registration'),
    path('api/profile/', ProfileAPIView.as_view(), name='profile'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [path("__debug__/", include("debug_toolbar.urls")), ] + urlpatterns
