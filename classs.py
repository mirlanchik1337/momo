class Hero:
    def __init__(self, name, abyliti):
        self.name = name
        self.abyliti =abyliti

class Hero_super(Hero):
    def __str__(self):
        return f'{self.name} it is super_hero'
#
# c = Hero_super("Ironman", "fire")
# print(c.__str__()) это  проверочка кода