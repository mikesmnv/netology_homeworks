from rest_framework import serializers
from api.models import Product, OrderPosition, \
    ProductReview, Order, ProductCollection


class OrderPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderPosition
        fields = ("id", "product_id", "quantity")


class OrderSerializer(serializers.ModelSerializer):

    order_positions = OrderPositionSerializer(many=True,
                                              required=True)

    class Meta:
        model = Order
        fields = ("id", "user_id", "order_positions", "status",
                  "price", "created_at", "updated_at")

    def create(self, validated_data):
        order_positions_data = validated_data("positions")
        order = super().create(validated_data)
        raw_order_positions = []
        for order_position_data in order_positions_data:
            order_position = OrderPosition(
                position=order,
                position_id=order_position_data["product_id"],
                quantity=order_position_data["quantity"],
            )
            raw_order_positions.append(order_position)
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
                  "products", "score", "created_at", "updated_at")
