from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Product, OrderPosition, \
    ProductReview, Order, ProductCollection


class UserSerializer(serializers.ModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True,
                                                queryset=Order.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'e-mail', 'orders']


class OrderPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderPosition
        fields = ("id", "product_id", "quantity")


class OrderSerializer(serializers.ModelSerializer):

    positions = OrderPositionSerializer(many=True,
                                              required=True)

    class Meta:
        model = Order
        fields = ("id", "user_id", "positions", "status",
                  "full_price", "created_at", "updated_at")

    def create(self, validated_data):
        order_positions_data = validated_data("positions")
        order = super().create(validated_data)
        raw_order_positions = []
        for order_position_data in order_positions_data:
            position = OrderPosition(
                order_id=order,
                id=order_position_data["product_id"],
                quantity=order_position_data["quantity"],
            )
            raw_order_positions.append(position)
        OrderPosition.objects.bulk_create(raw_order_positions)
        return order



class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("id", "name", "description", "price",
                  "created_at", "updated_at")


class ProductReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductReview
        fields = ("id", "author_id", "product_id",
                  "review", "score", "created_at", "updated_at")


class ProductCollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCollection
        fields = ("id", "name", "text",
                  "products", "created_at", "updated_at")
