class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def make_sound(self):
        print(f"{self.name} говорить {self.sound}")
cat = Animal("Кіт", "Мяу")
dog = Animal("Собака", "Гав")
cat.make_sound()
dog.make_sound()
