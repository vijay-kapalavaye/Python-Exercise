class Animal:
    def __init__(self,a,b):
        self.height=a
        self.weight=b
    def display(self):
        print(self.weight,self.height)
class Dog(Animal):
    def speak(self):
        print("BOW BOW !")
d=Dog(1.5,25)
d.display()
d.speak()