from src.order import Order


class OrderRepository:

    def __init__(self, session):
        self.session = session

    def get_by_email(self, customer_email):
        return self.session.query(Order).filter(Order.customer_email == customer_email).all()
