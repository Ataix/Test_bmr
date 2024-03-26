from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer


class OrderCreateView(CreateAPIView):
    """
    Create a new order
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderListView(ListAPIView):
    """
    Listing of orders for specific user
    """
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        """
        Overrides generic's ListAPIView's list function for customized queryset
        """
        queryset = self.filter_queryset(
            Order.objects.filter(user=request.user).order_by('created_at')
        )
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class OrderRetrieveView(RetrieveAPIView):
    """
    Retrieves specific order
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
