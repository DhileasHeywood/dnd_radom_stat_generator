import random

class Character:

    def __init__(self, name):
        self.name = name
        self.strength = self.calculate_attribute()
        self.dexterity = self.calculate_attribute()
        self.constitution = self.calculate_attribute()
        self.intelligence = self.calculate_attribute()
        self.wisdom = self.calculate_attribute()
        self.charisma = self.calculate_attribute()

    def calculate_attribute(self):
        d6 = [1, 2, 3, 4, 5, 6]

        rolls = random.choices(d6, k = 4)
        rolls.sort

        if rolls[0] == 1:
            rolls[0] == random.choices(d6, k = 1)
            rolls.sort
            return sum(rolls[1:])

        else:
            return sum(rolls[1:])

    def mod(self, x):
        mod = x // 2
        modifier = '{:+}'.format(mod - 5)
        return modifier

    def for_template(self):
        character = {
            "name":self.name,
            "str":(self.strength, self.mod(self.strength)),
            "dex":(self.dexterity, self.mod(self.dexterity)),
            "con":(self.constitution, self.mod(self.constitution)),
            "int":(self.intelligence, self.mod(self.intelligence)),
            "wis":(self.wisdom, self.mod(self.wisdom)),
            "cha":(self.charisma, self.mod(self.charisma))
            }

        return character
