import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APIClient

from api.models import Product, OrderPosition, \
    ProductReview, Order, ProductCollection


@pytest.mark.django_db
def test_products_get(api_client):

    product = Product.objects.create(
        id=1,
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
def test_orders_get(api_client):

    order = Order.objects.create(
        user_id=2,
        status="Нов",
        positions=[{"product": 2, "quantity": 2}]
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
        author_id=1,
        product_id=1,
        review="Good",
        score=4

    )
    order2 = Order.objects.create(
        id=1,
        author_id=2,
        product_id=2,
        review="so-so",
        score=3
    )

    url = reverse("product-reviews-list")
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == 7


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
