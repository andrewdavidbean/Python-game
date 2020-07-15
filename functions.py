# Win = ("x | x | x") and ("0 | 0 | 0")
# if Win:
#     print ("Win")
# elif Win:
#     print ("You lose")

# ("0 | 0 | 0")

# x = "X"
# o = "O"
# print("     |      |      ")
# print("  {}  |   {}  |   {}  ".format(x, x, x))
# print("     |      |      ")
# print("-------------------")
# print("     |      |      ")
# print("  {}  |      |      ".format(o))
# print("     |      |      ")
# print("-------------------")
# print("     |      |      ")
# print("     |  {}   |      ".format(o))
# print("     |      |      ")
# if x == "o" or x == "O":
#     print("Congratulations, you have won!")
# else:
#     print("Better luck next time!")

# age = 18
# if age < 18:
#     print ("£8")
# elif age  >= 60:
#     print ("£7.50")
# else:
#     print ("£10.95")

# age = 100
# if age < 18:
#     print("Child prices are £8, pay up!")
# elif age >= 18 and age < 60:
#     print("£10.95 are the adult prices")
# elif age >= 60 and age < 99:
#     print("For fossils, it's £7.50")
# else:
#     print("You must be a mega fossil, kudos. You come in for free")

# def coffee_order(size, type_of_drink):
#     print("Your {} {} is ready to drink".format(size, type_of_drink))
# coffee_order("grande", "soy latte")

# def cash_withdrawal(amount, accnum):
#     print("Withdrawing {} from account {}".format(amount, accnum))
# cash_withdrawal(100, 123456789)
# cash_withdrawal(60, 50449921)
# cash_withdrawal(40, 50449931)

# def multiply_by_nine_fifths(celcius):
#     return celcius *(9/5)
# def get_fahrenheit(celcius):
#     return multiply_by_nine_fifths(celcius) + 32
# print("The temeperature is {} degrees F".format(get_fahrenheit(1500)))

# order_count = 0

# def take_order(topping1,topping2):
#     global order_count
#     order_count += 1
#     print("order number {}: pizza with {} and {}".format(order_count,topping1,topping2))

# take_order("pineapple","pepperoni")

# import time
# order_count = 0
# def take_order(topping1, topping2):
#     global order_count
#     order_count += 1
#     print("Order number {}: Pizza with {} and {}".format(order_count, topping1, topping2))
# take_order("pepperoni", "pineapple")
# time.sleep(2.0)
# take_order("mushrooms", "peppers")
# time.sleep(2.0)
# take_order("cheese", "pepperoni")
# time.sleep(2.0)
# take_order("chicken", "pineapple")
# time.sleep(2.0)
# take_order("meat feast", "extra pepperoni")

