from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .serializer import ProductSerializer
from .models import Product


class ProductAPIList(ListAPIView):
    # Вывод списка товаров

    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response = self.get_paginated_response(serializer.data)
            if 'cnt' in request.COOKIES:
                cnt = int(request.COOKIES.get('cnt'))
                response.set_cookie('cnt', str(cnt+1))
            else:
                cnt = 1
                response.set_cookie('cnt', str(cnt))

            return response

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        gender = self.kwargs.get('gender')
        category = self.kwargs.get('category')
        return Product.objects.filter(gender=gender, category__title=category)


class ProductAPI(RetrieveAPIView):
    # Вывод одного товара

    serializer_class = ProductSerializer

    def get_queryset(self):
        gender = self.kwargs.get('gender')
        category = self.kwargs.get('category')
        slug = self.kwargs.get('slug')
        return Product.objects.get(gender=gender, category__title=category, slug=slug)
