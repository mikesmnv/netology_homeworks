import datetime

from django.db import models
from django.contrib import auth

score_choises = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f"{self.id} : {self.name}"


class ProductReview(models.Model):
    id = models.PositiveIntegerField()
    author_id = models.ForeignKey("auth.User", on_delete=models.CASCADE,
                                  primary_key=True, related_name="review")
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE,
                                   related_name="reviews")
    review = models.TextField()
    score = models.PositiveIntegerField(choices=score_choises)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f"{self.id} : {datetime.datetime.date(self.created_at)}"


class OrderPosition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE,
                                 related_name="positions")
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Информация о заказе'
        verbose_name_plural = 'Информация о заказах'

    def __str__(self):
        return f"{self.order.user_id} : {self.product_id}"


class StatusChoices(models.TextChoices):
    NEW = 'Нов', "Новый заказ"
    IN_PROGRESS = 'Вып', "Выполняется"
    DONE = 'Гот', "Заказ готов"


class Order(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="orders")
    position = models.ManyToManyField(Product, through=OrderPosition,
                                      related_name="orders")
    status = models.TextField(choices=StatusChoices.choices)
    full_price = models.DecimalField(max_digits=12, decimal_places=2,
                                     blank=True,
                                     null=True)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.id} : {datetime.datetime.date(self.created_at)}"


class ProductCollection(models.Model):
    name = models.CharField(max_length=25)
    text = models.TextField()
    products = models.ManyToManyField(Product, related_name="collections")
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

    def __str__(self):
        return f"{self.id} : {self.name}"
