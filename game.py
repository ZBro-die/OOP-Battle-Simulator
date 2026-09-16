from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Dusty Undergroud"

def battle(hero: Hero, enemy: Goblin):
    while hero.h_is_alive() and enemy.is_alive():
        hero_damage = hero.h_attack()
        enemy.take_damage(hero_damage)

        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.h_take_damage(enemy_damage)


    if hero.h_is_alive():
        print(f"{hero.name} surives...")
    else:
        print(f"{enemy.name} ends your journey...")


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Doom: Tremble! in fear of {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("DoomBots raise the gates...")

    goblin = Goblin("Symbiote Infected Creature")

    print(f"{goblin.name} crawls into the arena with {goblin.health} HP.")

    newGoblin = Goblin("Brotherhood Mutant")
    
    print(f"{newGoblin.name} stumbles into the arena with {goblin.health} HP.")
        
    hero = Hero("THE WANDERER")

    print(f"{hero.name} is shoved into the arena with {hero.health} HP.")

    battle(hero, goblin)


if __name__ == "__main__":
    main()
