from Race import Race


class Character:
    def __init__(self, name, alignment, race):
        self.name = name
        self.alignment = alignment
        self.race = race

    def get_str_bonus(self):
        if self.race is Race.human:
            return 5
        elif self.race is Race.orc:
            return 10
        else:
            return 0



john = Character("john", "someAllignment", Race.human)
#stuff happens
print(john.get_str_bonus())
