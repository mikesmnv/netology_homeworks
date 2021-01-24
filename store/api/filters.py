from django_filters import rest_framework as filters

from api.models import Product, ProductReview,\
    Order


class OrderFilters(filters.FilterSet):

    id = filters.ModelMultipleChoiceFilter(
        queryset=Order.objects.all(),
        field_name="id",
        to_field_name="id",
    )
    status = filters.CharFilter(lookup_expr="iexact")
    price = filters.RangeFilter()
    created_at = filters.DateFilter()
    updated_at = filters.DateFilter()

    class Meta:
        model = Order
        fields = ("status", "price", "created_at", "updated_at")


class ProductFilters(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="iexact")
    description = filters.CharFilter(lookup_expr="iexact")
    price = filters.RangeFilter()

    class Meta:
        model = Product

        fields = ("name", "description", "price")


class ProductReviewFilters(filters.FilterSet):

    author_id = filters.RangeFilter()
    product_id = filters.RangeFilter()
    created_at = filters.DateFilter()

    class Meta:
        model = ProductReview
        fields = ("author_id", "product_id", "created_at")
