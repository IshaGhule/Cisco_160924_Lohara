class Employee:
    def __init__(self, name, address, code, salary):
           self.name = name
           self.address = address
           self.code = code
           self.salary = salary

    def __str__(self):
           return f'{self.name}, {self.address}, {self.code}, {self.salary}'
    

isha= Employee('Isha', '908/2/2, wasan nagar', 'ABC12345', 200000)
print(isha)      