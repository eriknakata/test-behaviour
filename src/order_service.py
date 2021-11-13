class OrderService:

    def __init__(self, order_repository):
        self.order_repository = order_repository

    def get_total_orders_by_user(self, customer_email):
        return self.order_repository.sum_customer_orders(customer_email)
