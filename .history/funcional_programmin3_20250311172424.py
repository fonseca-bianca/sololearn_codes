"""
Functiond can take other functions as arguments
"""
def welcome(name):
    return "Welcome, " + name

def process_user(name, func):
    return func(name)

print(process_user("Alice", welcome))
#output: Welcome, Alice

###################################################

def order(dish):
    return "Your order: " + dish

def process_order(dish, func):
    print(func(dish))
    
process_order("Spaghetti", order)
    