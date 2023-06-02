def make_pizza(*toppings):
    """
    Summerise the pizza we are about to make
    """
    print("\nMake pizza with the following toppings")
    for topping in toppings:
        print(f"- {topping}")



make_pizza('pepperoni')
make_pizza('muchroom','green pepper', 'extra cheese')
