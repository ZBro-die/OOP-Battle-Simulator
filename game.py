from goblin import Goblin


ARENA_NAME = "Dr. Doom's Destruction Dome"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Tremble! in fear of {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("DoomBots raise the gates...")

    goblin = Goblin("Symbiote Infected Creature")

    print(f"{goblin.name} crawls into the arena with {goblin.health} HP.")

    newGoblin = Goblin("Brotherhood Mutant")
    
    print(f"{newGoblin.name} crawls into the arena with {goblin.health} HP.")
        

    print("But no hero has answered the call... yet.")


if __name__ == "__main__":
    main()
