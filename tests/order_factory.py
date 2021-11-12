import factory

from src.connection_factory import Session
from src.order import Order


class OrderFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Order
        sqlalchemy_session = Session

    customer_email = factory.Faker('email')
    total = factory.Faker('pydecimal', min_value=1, max_value=100, right_digits=2)
