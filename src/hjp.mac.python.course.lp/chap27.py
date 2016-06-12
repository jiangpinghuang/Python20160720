class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)
        
x = FirstClass()
y = FirstClass()

x.setdata("king Arthur")
y.setdata(3.141258)

x.display()
y.display()

x.data = "Learning Python"
x.display()

y.data = 12.345
y.display()

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
        
bob = Person('Bob Smith')
sue = Person('Sue Jones', job = 'dev', pay = 100000)
print(bob.name, bob.pay)
print(sue.name, sue.pay)