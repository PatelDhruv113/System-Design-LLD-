# Realization ka matlab hai ek class kisi interface (ya abstract contract) ko implement karti hai.

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass


class CreditCard(Payment):
    def pay(self):
        print("Payment by Credit Card")

card = CreditCard()
card.pay()