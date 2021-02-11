import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.status import HTTP_200_OK

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
        user=user.id,
        positions=[{"product": 1, "quantity": 2}],
        status="Нов"
    )
    url = reverse("orders-detail", args=[order.id])

    resp = api_client.get(url)

    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert resp_json
    assert resp_json["id"] == order.id


@pytest.mark.django_db
def test_product_review_list(api_client):

    review1 = ProductReview.objects.create(
        id=1,
        author=1,
        product=1,
        review="Good",
        score=4

    )
    review2 = Order.objects.create(
        id=2,
        author=1,
        product=2,
        review="so-so",
        score=3
    )

    url = reverse("product-reviews-list")
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
 #   assert len(resp_json) == 7


@pytest.mark.django_db
def test_orders_filter(api_client):

    order1 = Order.objects.create(
        user_id=2,
        status="Выполняется",
        positions=[{"product": 2, "quantity": 2}]
    )

    order2 = Order.objects.create(
        user_id=2,
        status="Готов",
        positions=[{"product": 1, "quantity": 1}]
    )

    url = reverse("orders-list")
    resp = api_client.get(url, {"status": "Готов"})
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()

    assert len(resp_json) == 1
    result = resp_json[0]
    assert result["id"] == order2.id
