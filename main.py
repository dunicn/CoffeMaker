class CoffeeMaker:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.money = 550
        self.disposable_cups = 9

        self.state = "main_menu"
        self.user_interaction()

    def user_interaction(self):
        if self.state == "main_menu":
            print("Write action (buy, fill, take, remaining, exit):")
        elif self.state == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino or 'back' if you changed your mind: ")
        elif self.state == "fill_water":
            print("Write how much water you want to add into the coffee machine")
        elif self.state == "fill_milk":
            print("Write how much milk you want to add into the coffee machine")
        elif self.state == "fill_coffee":
            print("Write how much coffee you want to add into the coffee machine: ")
        elif self.state == "fill_disposable_cups":
            print("Write how many disposable cups you want to add into the coffee machine: ")

    def get_input(self, user_input):
        if self.state == "main_menu":
            print()
            if user_input == "buy":
                self.state = "buy"
            if user_input == "fill":
                self.state = "fill_water"
            elif user_input == "take":
                self.take()
            elif user_input == "remaining":
                self.remaining_resources()
            elif user_input == "exit":
                return False

        elif self.state == "buy":
            self.buy(user_input)
            self.state = "main_menu"
        elif self.state == "fill_water":
            self.water += int(user_input)
            self.state = "fill_milk"
        elif self.state == "fill_milk":
            self.milk += int(user_input)
            self.state = "fill_coffee"
        elif self.state == "fill_coffee":
            self.coffee += int(user_input)
            self.state = "fill_disposable_cups"
        elif self.state == "fill_disposable_cups":
            self.disposable_cups += int(user_input)
            self.state = "main_menu"

        if self.state == "main_menu":
            print()
        self.user_interaction()
        return True

    def buy(self, chosen_coffee):
        water_needed = 0
        milk_needed = 0
        coffee_needed = 0
        coffee_cost = 0
        if chosen_coffee == "1":
            water_needed = 250
            milk_needed = 0
            coffee_needed = 16
            coffee_cost = 4

        elif chosen_coffee == "2":
            water_needed = 350
            milk_needed = 75
            coffee_needed = 20
            coffee_cost = 7
        elif chosen_coffee == "3":
            water_needed = 200
            milk_needed = 100
            coffee_needed = 12
            coffee_cost = 6
        elif chosen_coffee == "back":
            return

        if self.water < water_needed:
            print("Sorry, not enough water!")
        elif self.milk < milk_needed:
            print("Sorry, not enough milk!")
        elif self.coffee < coffee_needed:
            print("Sorry, not enough coffee!")
        elif self.disposable_cups == 0:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= water_needed
            self.milk -= milk_needed
            self.coffee -= coffee_needed
            self.disposable_cups -= 1
            self.money += coffee_cost

    def take(self):
        print("I gave you $", self.money)
        self.money = 0

    def remaining_resources(self):
        print("The coffee machine has:")
        print(self.water, "ml of water")
        print(self.milk, "ml of milk")
        print(self.coffee, "g of coffee beans")
        print(self.disposable_cups, "of disposable cups")
        print(self.money, " of money")


coffee_maker = CoffeeMaker()

while coffee_maker.get_input(input()):
    pass
