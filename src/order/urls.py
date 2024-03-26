from django.urls import path

from .views import OrderCreateView, OrderListView, OrderRetrieveView

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order-create'),
    path('list/', OrderListView.as_view(), name='order-list'),
    path('<int:pk>/', OrderRetrieveView.as_view(), name='order-detail'),
]
