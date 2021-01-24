from django.db import models


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


class User(models.Model):
    name = models.CharField(max_length=25)
    password = models.CharField(max_length=10)
    email = models.EmailField()
#    token = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.id} : {self.name}"


class ProductReview(models.Model):
    id = models.PositiveIntegerField()
    author_id = models.ForeignKey(User, on_delete=models.CASCADE,
                                  primary_key=True, related_name="review")
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE,
                                   related_name="reviews")
    review = models.TextField()
    score = models.PositiveIntegerField()
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
        return f"{self.id} : {self.created_at}"


class OrderPosition(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_id = models.ForeignKey("Order", on_delete=models.CASCADE,
                                 related_name="positions")
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"{Order.user_id} : {Order.user_id}"


class StatusChoices(models.TextChoices):
    NEW = 'Нов', "Новый заказ"
    IN_PROGRESS = 'Вып', "Выполняется"
    DONE = 'Гот', "Заказ готов"


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    position = models.ManyToManyField(Product, through=OrderPosition,
                                      related_name="orders")
    status = models.TextField(choices=StatusChoices.choices)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = 'Информация о заказе'
        verbose_name_plural = 'Информация о заказах'
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.id} : {self.created_at}"


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
