class Animal:
    def make_sound(self):
        print("Bark")

class human(Animal):
    def make_sound(self):
        print("Speak")

harsh = human()
dog = Animal()
harsh.make_sound()
dog.make_sound()