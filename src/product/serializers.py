from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'category',
            'description',
            'quantity',
            'price',
        )


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'category',
            'description',
            'quantity',
            'price',
        )

    def create(self, validated_data):
        if float(validated_data['price']) < 0:
            raise ValidationError(
                'Invalid price. Should be greater or equal to zero'
            )
        if int(validated_data['quantity']) < 0:
            raise ValidationError(
                'Invalid quantity. Should be greater or equal to zero'
            )
        product = Product.objects.create(**validated_data)
        return product

    def update(self, instance, validated_data):
        if 'price' in validated_data and float(validated_data['price']) < 0:
            raise ValidationError(
                'Invalid price. Should be greater or equal to zero'
            )
        if 'quantity' in validated_data and validated_data['quantity'] < 0:
            raise ValidationError(
                'Invalid quantity. Should be greater or equal to zero'
            )
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
