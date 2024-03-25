from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
)
from rest_framework.viewsets import ViewSetMixin

from .models import Product
from .serializers import ProductSerializer, ProductCreateUpdateSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateUpdateSerializer


class ProductViewSet(ViewSetMixin,
                     RetrieveAPIView,
                     UpdateAPIView,
                     DestroyAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        """
        Returns the appropriate serializer
        :return:
        """
        if self.action in ('update', 'partial_update'):
            return ProductCreateUpdateSerializer
        else:
            return ProductSerializer
