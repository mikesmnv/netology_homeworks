from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Product, OrderPosition, \
    ProductReview, Order, ProductCollection


class UserSerializer(serializers.ModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True,
                                                queryset=Order.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'e-mail', 'orders')


class OrderPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPosition
        fields = ("product", "quantity")


class OrderSerializer(serializers.ModelSerializer):
    positions = OrderPositionSerializer(many=True,
                                        required=True, )

    class Meta:
        model = Order
        fields = ("user", "positions", "status",
                  "full_price", "created_at", "updated_at")

    def create(self, validated_data):
#        print(validated_data)
        order_positions_data = validated_data.pop("positions")
        full_price = 0
        # order = super().create(validated_data)
        raw_order_positions = []
        for order_position in order_positions_data:
            full_price += Product.objects.get(id=order_position["product"].id).price * \
                      order_position["quantity"]
        order = Order(user=validated_data["user"],
                      status=validated_data["status"],
                      full_price=full_price)
        order.save()
        for order_position in order_positions_data:
            position = OrderPosition(
                 order=order,
                 product=order_position["product"],
                 quantity=order_position["quantity"],
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
        fields = ("author", "product",
                  "review", "score", "created_at", "updated_at")


class ProductCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCollection
        fields = ("id", "name", "text",
                  "products", "created_at", "updated_at")
