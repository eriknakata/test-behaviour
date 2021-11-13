from decimal import Decimal

import pytest
from src.order_repository import OrderRepository
from tests.integration_test import IntegrationTest
from tests.order_factory import OrderFactory


class TestOrderRepository(IntegrationTest):

    @pytest.fixture
    def order_repository(self, session):
        return OrderRepository(session)

    def test_should_return_the_customer_orders(self, order_repository):
        orders = OrderFactory.create_batch(size=5, customer_email='test@gmail.com')

        db_orders = order_repository.get_by_email('test@gmail.com')

        assert orders == db_orders

    def test_should_return_empty_when_customer_has_no_orders(self, order_repository):
        OrderFactory.create(customer_email='test@gmail.com')

        db_orders = order_repository.get_by_email('other@gmail.com')

        assert not db_orders

    def test_should_return_the_customer_total_pricing(self, order_repository):
        OrderFactory.create_batch(size=5, customer_email='test@gmail.com', total=10.50)

        total = order_repository.sum_customer_orders('test@gmail.com')

        assert total == Decimal(52.50)

    def test_should_return_zero_when_customer_has_no_orders(self, order_repository):
        total = order_repository.sum_customer_orders('test@gmail.com')

        assert total == Decimal(0.00)
