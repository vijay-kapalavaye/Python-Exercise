class Animal:
    def __init__(self,a, b):
        self.height=a
        self.weight=b
    def display(self):
        print(self.height,self.weight)
class Dog(Animal):
    def speak(self):
        print("bow bow")

f=Dog(2,5)
f.display()
f.speak()