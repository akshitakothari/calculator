class Calculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.choice = 0
        self.result = 0

    def display(self):
        print('''MENU
      1.ADDITION
      2.SUBTRACTION
      3.MULTIPLICATION
      4.DIVISION
      5.EXIT ''')

    def get_numbers(self):
        while True:
            try:
                self.num1 = int(input("enter num1= "))
                self.num2 = int(input("enter num2= "))
                break
            except ValueError:
                print("please enter valid int inputs!")

    def add(self):
        self.result = self.num1 + self.num2
        print(self.num1, '+', self.num2, '=', self.result)

    def subtract(self):
        self.result = self.num1 - self.num2
        print(self.num1, '-', self.num2, '=', self.result)
    
    def multiply(self):
        self.result = self.num1 * self.num2
        print(self.num1, '*', self.num2, '=', self.result)


    def divide(self):
        if self.num2 == 0:
            print("denominator can't be 0! ")
            return
        else:
            self.result = self.num1 / self.num2
            print(self.num1, '/', self.num2, '=', self.result)
        
    def run(self):
        while True:
            self.display()
            try:
                self.choice = int(input("enter your choice(1/2/3/4/5): "))
            except ValueError:
                print("please enter no. between 1 to 5!")
                continue
            if self.choice == 5:
                print("goodbye!")
                break
            elif self.choice not in [1,2,3,4,5]:
                print("invalid choice! Enter again!")
                continue
            self.get_numbers()
            if self.choice == 1:
                self.add()
            elif self.choice == 2:
                self.subtract()
            elif self.choice == 3:
                self.multiply()
            elif self.choice == 4:
                self.divide()

calc=Calculator()
calc.run()