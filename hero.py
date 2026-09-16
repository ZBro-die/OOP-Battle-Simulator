import random


class Hero:
    """The hero braving Doom's Arena"""

    def __init__(self, name):
        self.name = name
        self.health = 120
        self.attack_power = 10

    def h_attack(self):
            """Return a random amount of damage between 0 and the hero's attack stat."""
            return random.randint(1, self.attack_power)

    def h_take_damage(self, damage):
        """subtract health without allowing it to fall below zero."""
        self.health = self.health - damage
        if self.health < 0:
             self.health = 0

    def h_is_alive(self):
        """Return True while the hero has health remaining."""
        return self.health > 0
   