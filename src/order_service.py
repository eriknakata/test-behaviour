class OrderService:

    def __init__(self, order_repository):
        self.order_repository = order_repository

    def get_total_orders_by_user(self, customer_email):
        customer_orders = self.order_repository.get_by_email(customer_email)

        return sum([order.total for order in customer_orders])
