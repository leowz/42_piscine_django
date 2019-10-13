import random
import beverages

class CoffeeMachine:
    def __init__(self):
        self.count = 0;

    class EmptyCup(beverages.HotBeverage):
        name = 'empty cup';
        price = '0.90';

        def description(self):
            return "An empty cup?! Gimme my money back!";

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.");

    def repair(self):
        self.count = 0;

    def serve(self, beverage):
        if (self.count > 9):
            raise self.BrokenMachineException();
        self.count += 1;
        ran = random.randint(0,1);
        if (ran % 2 == 0):
            return self.EmptyCup();
        else:
            return beverage;

if __name__ == '__main__':
    m = CoffeeMachine();
    for i in range(1, 20):
        try:
            print(m.serve(beverages.Cappuccino()))
            print(m.serve(beverages.Coffee()))
            print(m.serve(beverages.Tea()))
            print(m.serve(beverages.Chocolate()))
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
            m.repair()
            print("repair machine\n")

