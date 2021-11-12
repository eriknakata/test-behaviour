from decimal import Decimal

import pytest
from unittest.mock import MagicMock
from src.order_service import OrderService
from tests.order_factory import OrderFactory


class TestOrderService:

    @pytest.fixture
    def order_repository(self):
        return MagicMock()

    @pytest.fixture
    def order_service(self, order_repository):
        return OrderService(order_repository)

    def test_should_return_the_total_by_customer(self, order_service):
        order_service.order_repository.get_by_email = MagicMock(return_value=
                                                                OrderFactory.build_batch(10, total=Decimal(10),
                                                                                         customer_email='test@gmail.com'))

        assert order_service.get_total_orders_by_user('test@gmail.com') == Decimal(100.00)

    def test_should_return_zero_when_customer_has_no_orders(self, order_service):
        order_service.order_repository.get_by_email = MagicMock(return_value=[])

        assert order_service.get_total_orders_by_user('test@gmail.com') == Decimal(0.00)
