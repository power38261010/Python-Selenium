class Order:
    def __init__(self, total_amount, payment_strategy):
        self.total_amount = total_amount
        self.payment_strategy = payment_strategy

    def process_payment(self):
        self.payment_strategy.pay(self.total_amount)