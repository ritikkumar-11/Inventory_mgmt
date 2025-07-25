from rest_framework import serializers
from .models import User, Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        try:
            user = User(username=validated_data['username'])
            user.set_password(validated_data['password'])
            user.save()
            return user
        except Exception as e:
            raise serializers.ValidationError({"error": str(e)})


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'type',
            'sku',
            'image_url',
            'description',
            'quantity',
            'price',
        ]

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantity should be greater than 0")
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price should be greater than 0")
        return value


class UpdateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['quantity']

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantity should be greater than 0")
        return value

    def update(self, instance, validated_data):
        try:
            instance.quantity = validated_data.get('quantity', instance.quantity)
            instance.save()
            return instance
        except Exception as e:
            raise serializers.ValidationError({"error": str(e)})
