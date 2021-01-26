from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets, mixins
from api.permissions import IsOwnerOrReadOnly
from api.serializers import *
from api.filters import *


class ProductViewset(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProductFilters
    permission_classes = [permissions.IsAdminUser]

class ProductReviewViewset(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):

    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProductReviewFilters
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

class OrderViewset(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):


    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = OrderFilters
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        sum = 0
        for order in Order.objects.all().prefetch_related("OrderPosition", "Product"):
            for product in order.products.all():
                sum += order.price * product.quantity
            order.full_price = sum
        resp = super().create(request, *args, **kwargs)
        return resp

class CollectionViewset(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):


    queryset = ProductCollection.objects.all()
    serializer_class = ProductCollectionSerializer
    permission_classes = [permissions.IsAdminUser]

