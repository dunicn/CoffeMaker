avl_water = 400
avl_milk = 540
avl_coffee = 120
avl_money = 550
disposable_cups = 9


def coffee_maker(water, milk, coffee, money):
    global avl_water
    global avl_milk
    global avl_coffee
    global avl_money
    global disposable_cups
    avl_water -= water
    avl_milk -= milk
    avl_coffee -= coffee
    avl_money += money
    disposable_cups -= 1


def buy_method():
    input_ = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
    if input_ == 1:  # type int
        return coffee_maker(250, 0, 16, 4)  # esspreso: water 250ml, no milk, coffee 16g, costs 4$
    elif input_ == 2:
        return coffee_maker(350, 75, 20, 7)  # latte: water 350ml, milk 75ml, coffee 20g, costs 7$
    elif input_ == 3:
        return coffee_maker(200, 100, 12, 6)  # cappuccino: water 200ml, milk 100ml, coffee 12g, costs 6$
    #  input == back


def fill_method():
    global avl_water
    global avl_milk
    global avl_coffee
    global disposable_cups
    water = int(input("Write how much water you want to add into the coffee machine: "))
    milk = int(input("Write how much milk you want to add into the coffee machine: "))
    coffee = int(input("Write how much coffee you want to add into the coffee machine: "))
    cups = int(input("Write how many disposable cups you want to add into the coffee machine: "))
    avl_water += water
    avl_milk += milk
    avl_coffee += coffee
    disposable_cups += cups


def choose_method(input_):
    if input_ == "buy":
        return buy_method()  # there is no need for return
    elif input_ == "fill":
        return fill_method()
    elif input_ == "take":
        #  I gave you avl_money
        global avl_money
        avl_money = 0


def print_status():  # remaining method
    print("The coffee machine has:")
    print(avl_water, "ml of water")
    print(avl_milk, "ml of milk")
    print(avl_coffee, "g of coffee beans")
    print(disposable_cups, "of disposable cups")
    print(avl_money, " of money")


def coffee_machine_process():
    input_ = str(input("Write action (buy, fill, take): "))
    while input_ != "exit":
        choose_method(input_)
        input_ = str(input("Write action (buy, fill, take): "))

coffee_machine_process()

