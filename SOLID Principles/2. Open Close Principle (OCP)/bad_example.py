class PaymentProcessor:
    def pay(self, payment_method: str, amount: int):
        if payment_method == "UPI":
            print(f"Starting UPI transaction of Rs.{amount}")
            print(f"UPI transaction finisheed")
        elif payment_method == "credit_card":
            print(f"Starting Credit card transaction of Rs.{amount}")
            print(f"Credit card transaction finisheed")
        elif payment_method == "net_banking":
            print(f"Starting Net banking transaction of Rs.{amount}")
            print(f"Net banking transaction finisheed")
        else:
            print("Payment method was not found")

pay_p = PaymentProcessor()
pay_p.pay("credit_card",500)