import django_filters

from .models import Product


class ProductFilter(django_filters.FilterSet):
    """
    Filtering product model
    """
    price_from = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_to = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    name = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = [
            'price_from',
            'price_to',
            'name',
            'category',
        ]
