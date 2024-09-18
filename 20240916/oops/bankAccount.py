class Account:
    def __init__(self, number, name, initial_amount=1000):
        self.__number = number
        self.__name = name
        self.__balance = initial_amount
    def __repr__(self):
        return f'[number= {self.__number}, name= {self.__name}, balance={self.__balance}]'
    def __str__(self):
        return self.__repr__()
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount > self.__balance:
            print('No enough balance')
            return
        self.__balance -= amount
    #enddef
#endclass

isha_ac = Account(name='Isha',number='1234567890',initial_amount = 3000)
print(isha_ac)
isha_ac.deposit(200000)
print(isha_ac)
isha_ac.deposit(10000)
print(isha_ac)
isha_ac.withdraw(50000)
print(isha_ac)
print(isha_ac.__dict__)
#print(isha_ac.__balance) # Error,it is private function
isha_ac.withdraw(200000)
print(isha_ac)