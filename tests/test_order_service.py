import pytest
from decimal import Decimal

from src.order_repository import OrderRepository
from src.order_service import OrderService
from tests.integration_test import IntegrationTest
from tests.order_factory import OrderFactory


class TestOrderService(IntegrationTest):

    @pytest.fixture
    def order_repository(self, session):
        return OrderRepository(session)

    @pytest.fixture
    def order_service(self, order_repository):
        return OrderService(order_repository)

    def test_should_return_the_total_by_customer(self, order_service):
        OrderFactory.create_batch(size=5, customer_email='test@gmail.com', total=20.00)

        total = order_service.get_total_orders_by_user('test@gmail.com')

        assert total == Decimal(100.00)

    def test_should_return_zero_when_customer_has_no_orders(self, order_service):
        assert order_service.get_total_orders_by_user('test@gmail.com') == Decimal(0.00)
