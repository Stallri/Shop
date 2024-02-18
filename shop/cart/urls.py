from django.urls import path

from cart.views import CartAPIView, CartAddAPIView

urlpatterns = [
    path('', CartAPIView.as_view(), name='cart_list'),
    path('<slug:slug>/', CartAddAPIView.as_view(), name='cart_add'),
]
