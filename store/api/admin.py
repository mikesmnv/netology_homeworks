from django.contrib import admin

from api.models import Product, OrderPosition, \
    ProductReview, Order, ProductCollection


class ProductAdmin(admin.ModelAdmin):
    pass


class ProductCollectionAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


class OrderPositionAdmin(admin.ModelAdmin):
    pass


class ProductReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(OrderPosition, OrderPositionAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductCollection, ProductCollectionAdmin)
