from rest_framework import serializers

from .models import OrderItem, Order


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'id',
            'product',
            'quantity',
            'price',
        )


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            'created_at',
            'address',
            'comment',
            'total',
            'discount',
            'items',
        )

    def create(self, validated_data):
        """
        Create and return a new `Order`. Inserts user to order from request.
        :param validated_data:
        :return: order object
        """
        request = self.context.get('request')
        items = validated_data.pop('items')
        print(validated_data)
        print(request)
        order = Order.objects.create(**validated_data)
        order.user = request.user
        order.save()
        for item in items:
            item = OrderItem.objects.create(**item)
            order.items.add(item)
        return order
