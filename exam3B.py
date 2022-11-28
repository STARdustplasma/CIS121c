from exam3 import Customer

customer = Customer('bob')

customer1 = Customer('bob')

customer1.makePurchase(100)
customer1.discountReached()
customer1.makePurchase(95)
customer1.discountReached()
customer1.makePurchase(5)
customer1.discountReached()

customer1.loyalty()
