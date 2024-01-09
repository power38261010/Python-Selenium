from payment_system.payment_strategy import PaymentStrategy

class PaypalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f'Pague {amount} dolares usando Paypal.')