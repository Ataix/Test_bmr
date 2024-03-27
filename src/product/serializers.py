from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for review
    """
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True
    )

    class Meta:
        model = Review
        fields = (
            'id',
            'product',
            'text',
            'author',
            'created_at',
            'rate',
        )


class ReviewCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for review creation and update
    """
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True
    )

    class Meta:
        model = Review
        fields = (
            'id',
            'product',
            'text',
            'created_at',
            'rate',
        )

    def create(self, validated_data):
        """
        Validating rate for review creation
        :param validated_data:
        :return:
        """
        if int(validated_data['rate']) <= 0:
            validated_data['rate'] = 1
        elif int(validated_data['rate']) > 5:
            validated_data['rate'] = 5
        review = Review.objects.create(**validated_data)
        return review

    def update(self, instance, validated_data):
        """
        Validating rate for review update
        :param instance:
        :param validated_data:
        :return:
        """
        if int(validated_data['rate']) <= 0:
            validated_data['rate'] = 1
        elif int(validated_data['rate']) > 5:
            validated_data['rate'] = 5
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for product
    """
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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['reviews'] = ReviewSerializer(
            instance.reviews.all(), many=True
        ).data
        return representation


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for product creation and update
    """
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
        """
        Validating price and quantity for product creation
        :param validated_data:
        :return:
        """
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
        """
        Validating price and quantity for product updating
        :param instance:
        :param validated_data:
        :return:
        """
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
