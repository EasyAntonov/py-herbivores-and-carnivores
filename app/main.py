class Animal:
    alive = []

    def __init__(self, name, health = 100, hidden = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}"
                )

class Herbivore (Animal):

    def hide(self):
        self.hidden = not self.hidden



class Carnivore (Animal):

    def bite(self, herbivore):
        if isinstance(herbivore, Herbivore):
            if not herbivore.hidden:
                herbivore.health -= 50
            if herbivore.health <= 0:
                if herbivore in Animal.alive:
                    Animal.alive.remove(herbivore)
