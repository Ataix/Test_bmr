from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for registration process
    """
    password = serializers.CharField(min_length=6, write_only=True)
    password_confirm = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'password_confirm',
        )

    def validate(self, attrs):
        """
        Validate the pair of passwords
        :param attrs:
        :return:
        """
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('passwords does not same')
        return attrs

    def create(self, validated_data):
        """
        User creation
        :param validated_data:
        :return:
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    Basic user serializer
    """
    class Meta:
        model = User
        fields = '__all__'
