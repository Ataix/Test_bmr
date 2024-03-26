from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSetMixin

from .filters import ProductFilter
from .models import Product
from .serializers import ProductSerializer, ProductCreateUpdateSerializer


class ProductListView(ListAPIView):
    """
    Api view for listing of all products
    """
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class ProductCreateView(CreateAPIView):
    """
    Independent api view for creating new products
    """
    queryset = Product.objects.all()
    serializer_class = ProductCreateUpdateSerializer
    permission_classes = [IsAuthenticated]


class ProductViewSet(ViewSetMixin,
                     RetrieveAPIView,
                     UpdateAPIView,
                     DestroyAPIView):
    """
    View set for RUD operations
    """
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

    def get_permissions(self):
        """
        Returns appropriate permissions
        :return:
        """
        if self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthenticated]
        else:
            permissions = []
        return [permission() for permission in permissions]


