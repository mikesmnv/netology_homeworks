from rest_framework import permissions
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from api.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from api.serializers import *
from api.filters import *


class ProductViewset(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProductFilters
    permission_classes = [permissions.IsAuthenticatedOrReadOnly & IsAdminOrReadOnly]

    def create(self, request, *args, **kwargs):
        print(request.user)
        if request.user.is_staff:
            resp = super().create(request, *args, **kwargs)
            return resp
        else:
            return Response({"message": "You are not admin!"})


class ProductReviewViewset(mixins.CreateModelMixin,   # API - 2
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProductReviewFilters
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def put(self, request):
        print(request)
#        print(request.data)
        user_id = request.data.pop('author')
        if request.user.id == user_id:
#            print(request.data)
            return super().update(request.data)
        else:
            return Response({"message": "You can't change this review!"})

class OrderViewset(viewsets.ModelViewSet):

    queryset = Order.objects.prefetch_related("position").all()
    serializer_class = OrderSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = OrderFilters
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CollectionViewset(viewsets.ModelViewSet):

    queryset = ProductCollection.objects.all()
    serializer_class = ProductCollectionSerializer
    permission_classes = [permissions.IsAdminUser]

