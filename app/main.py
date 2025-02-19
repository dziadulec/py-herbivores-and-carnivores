class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.hidden = False
        self.health = health
        self.name = name
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return "{" + (f"Name: {self.name}"
                      f", Health: {self.health}, Hidden: {self.hidden}") + "}"


class Herbivore(Animal):

    def hide(self) -> None:
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):

    @staticmethod
    def bite(victim: Animal) -> None:
        if victim.hidden is False and not isinstance(victim, Carnivore):
            victim.health -= 50
            if victim.health <= 0:
                Animal.alive.remove(victim)
