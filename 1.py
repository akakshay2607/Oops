class Atm:
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()
        
    def menu(self):
        inp = input("""
        Press the following buttons for:
        1.To set pin
        2.To change pin
        3.To check balance
        4.To withdraw balance
        5.Anyother thing to exit
        """)
        if inp == '1':
            self.set_pin()
            
        elif inp == '2':
            self.change_pin()
            
        elif inp == '3':
            self.check_balance()
            
        elif inp == '4':
            self.withdraw()
        else:
            exit()
            
    def set_pin(self):
        new_pin = input('Please enter the pin to set\n')
        self.pin = new_pin
        print('Pin set successfully')
        balance = int(input("Please Enter the balance you have\n"))
        self.balance = balance
        self.menu()
        
    def change_pin(self):
        old_pin = input('Enter your old pin\n')
        if old_pin == self.pin:
            new_pin = input('Please enter the new pin\n')
            self.pin = new_pin
            print('Pin changes successfully')
        else:
            print('Pin incorrect')
        self.menu()
    
    def check_balance(self):
        pin = input('Enter your pin\n')
        if pin == self.pin:
            print(f"your available balance is {self.balance}")
        self.menu()
    
    def withdraw(self):
        pin = input('Enter your pin\n')
        if pin == self.pin:
            amount = int(input('Enter the amount you want to withdraw\n'))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print(f"your remaining balance is {self.balance}")
            else:
                print('Insufficient amount')
                print(f"Your availabel balance is {self.balance} and you are asking for {amount}")
        self.menu()
    
a = Atm()