class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 1:
            print('Wrong age')
        elif age > 100:
            print('Wrong age')
        else:
            self.__age = age
 
a = Person(name='Jan', age = 55)
print(a.age)