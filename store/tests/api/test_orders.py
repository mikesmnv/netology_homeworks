import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

from api.models import Product, OrderPosition, \
    ProductReview, Order, ProductCollection


@pytest.mark.django_db
def test_products_get(api_client):
    username = "admin"
    password = "admin1551"
    api_client.login(username=username, password=password)
    product = Product.objects.create(
        name="Iphone7",
        description="text",
        price=50000
    )
    url = reverse("products-detail", args=[product.id])
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert resp_json
    assert resp_json["id"] == product.id
    assert resp_json["name"] == product.name


@pytest.mark.django_db
def test_products_list(api_client):

    product1 = Product.objects.create(
        name="Iphone7",
        description="text",
        price=50000
    )
    product2 = Product.objects.create(
        name="Iphone8",
        description="text",
        price=70000
    )

    url = reverse("products-list")
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_orders_get(api_client):
    username = "admin"
    password = "admin1551"
    user = User.objects.create_user(username=username, password=password)
    user.save()
    api_client.login(username=username, password=password)
    product = Product.objects.create(
        name="Iphone7",
        description="text",
        price=50000
    )
    order = Order.objects.create(
        user=user,
        status="Нов"
    )
    positions = OrderPosition.objects.create(product=product, order=order, quantity=2)
    url = reverse("orders-detail", args=[order.id])
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_product_review_list(api_client):
    username = "admin"
    password = "admin1551"
    user1 = User.objects.create_user(username=username, password=password)
    user1.save()
    api_client.login(username=username, password=password)
    product1 = Product.objects.create(
        name="Iphone7",
        description="text",
        price=50000
    )
    product2 = Product.objects.create(
        name="Iphone10",
        description="text",
        price=70000
    )
    review1 = ProductReview.objects.create(
        author=user1,
        product=product1,
        review="Good",
        score=4
    )
    url = reverse("product-reviews-detail", args=[user1.id])
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK
    username = "mike"
    password = "mike1551"
    user2 = User.objects.create_user(username=username, password=password)
    user2.save()
    api_client.login(username=username, password=password)
    review2 = ProductReview.objects.create(
        author=user2,
        product=product2,
        review="so-so",
        score=3
    )
    url = reverse("product-reviews-list")
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_collections(api_client):
    username = "mike"
    password = "1234567"
    user = User.objects.create_user(username=username, password=password)
    user.save()
    api_client.login(username=username, password=password)
    product = Product.objects.create(
        name="Iphone7",
        description="text",
        price=50000
    )
    collection = ProductCollection.objects.create(
        name="Phones",
        text="Text"
        )
    url = reverse("product-collections-detail", args=[collection.id])
    resp = api_client.get(url)
    assert resp.status_code == HTTP_401_UNAUTHORIZED
