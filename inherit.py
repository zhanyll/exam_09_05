class Animals:
    def __init__(self, name, foot, color, voice):
        self.name = name
        self.foot = foot
        self.color = color
        self.voice = voice

class Cat(Animal):
    super().__init__(name=name, foot=foot, color=color, voice=voice)
    def __init__(self, breed):
        self.breed = breed

sam = Cat(name='Sam', foot = 4, color= 'black', voice= 'meow')