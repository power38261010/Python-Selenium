from payment_system.payment_methods.credit_card import CreditCardPayment
from payment_system.payment_methods.paypal import PaypalPayment
from payment_system.order import Order

if __name__ == "__main__":

    # Creo instancias de estrategias de pago
    credit_card_strategy = CreditCardPayment()
    paypal_strategy = PaypalPayment()

    # Creo una orden con una estrategia de pago
    order_credit_card = Order(100, credit_card_strategy)
    order_paypal = Order(50, paypal_strategy)

    # Proceso pagos
    order_credit_card.process_payment()
    order_paypal.process_payment()