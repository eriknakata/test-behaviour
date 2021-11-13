from sqlalchemy import func
from src.order import Order


class OrderRepository:

    def __init__(self, session):
        self.session = session

    def get_by_email(self, customer_email):
        return self.session.query(Order).filter(Order.customer_email == customer_email).all()

    def sum_customer_orders(self, customer_email):
        return (
                   self.session.query(func.sum(Order.total))
                       .filter(Order.customer_email == customer_email)
                       .scalar()
               ) or 0.00
