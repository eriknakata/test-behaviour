import pytest
from decimal import Decimal
from unittest.mock import MagicMock
from src.order_service import OrderService


class TestOrderService:

    @pytest.fixture
    def order_repository(self):
        return MagicMock()

    @pytest.fixture
    def order_service(self, order_repository):
        return OrderService(order_repository)

    def test_should_return_the_total_by_customer(self, order_service):
        order_service.order_repository.sum_customer_orders = MagicMock(return_value=Decimal(100.00))

        assert order_service.get_total_orders_by_user('test@gmail.com') == Decimal(100.00)

    def test_should_return_zero_when_customer_has_no_orders(self, order_service):
        order_service.order_repository.sum_customer_orders = MagicMock(return_value=Decimal(0.00))

        assert order_service.get_total_orders_by_user('test@gmail.com') == Decimal(0.00)
