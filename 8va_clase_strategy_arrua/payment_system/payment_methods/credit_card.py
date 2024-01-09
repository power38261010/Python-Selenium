from payment_system.payment_strategy import PaymentStrategy

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f'Pague {amount} pesos usando tarjeta de credito.')