class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

class Fighter(Person):
    # heart_level = 1
    def __init__(self, fname, lname, element):
        super().__init__(fname, lname)
        self.element = element

    def slash(self):
        print(f"You do a {self.element} slash!")
        # heart_level += 1
        # print(f"Your heart level grew to {heart_level}!")

    def stab(self):
        print(f"You do a {self.element} stab!")
        # heart_level += 1
        # print(f"Your heart level grew to {heart_level}!")

    def poke(self):
        print(f"you do a simple {self.element} poke...")
        # heart_level += 1
        # print(f"Your heart level grew to {heart_level}!")

class Cleric(Person):
    def __init__(self, fname, lname, god):
        super().__init__(fname, lname)
        self.god = god

    def prayer(self):
        print(f"You call upon {self.god} to help you!")

    def heal(self):
        print(f"you use {self.god} love to cast healing!")

    def buff(self):
        print(f"You use {self.god}'s power to raise strength!")

class Item():
    item_hold = 0
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_item(self):
        print(f"You got {self.name}!")
        self.item_hold += 1