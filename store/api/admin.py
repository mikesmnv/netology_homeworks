from django.contrib import admin
from api.models import Product, OrderPosition, \
    ProductReview, Order, ProductCollection


class OrderPositionAdmin(admin.ModelAdmin):
    pass


class OrderPositionInLine(admin.TabularInline):
    model = OrderPosition


class ProductAdmin(admin.ModelAdmin):
    pass


class ProductCollectionAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderPositionInLine]


class ProductReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductCollection, ProductCollectionAdmin)
admin.site.register(OrderPosition, OrderPositionAdmin)
