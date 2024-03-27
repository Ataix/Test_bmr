from django.urls import path

from .views import (
    ProductListView, ProductCreateView, ProductViewSet, ReviewViewSet
)

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product-list'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('<int:pk>/', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    })),
    path('<int:pk>/reviews/', ReviewViewSet.as_view({
        'post': 'create',
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    })),
]
