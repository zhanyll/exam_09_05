class Animals:
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    super().__init__(name=name)
    def voice(self):
        print('Meow!')

class Dog(Animal):
    super().__init__(name=name)
    def voice(self):
        print('Gav!')
