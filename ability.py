class Ability:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def activate(self):
        pass  # Override in subclasses

class MysticShot(Ability):
    def __init__(self):
        super().__init__("Mystic Shot", 100, "Ezreal fires a bolt that deals 100% AD damage and reduces target's armor by 15 for 5 seconds.")

    def activate(self, character, target, crit, board):
        damage = character.ad * (character.critDmg if crit else 1)
        target.take_damage(damage, board)
        print(f"{character.name} uses {self.name}, dealing {damage:.2f} damage to {target.name} {'(CRIT!)' if crit else ''}.")

class AbsoluteZero(Ability):
    def __init__(self):
        super().__init__("Absolute Zero", 120, "Nunu channels for 3 seconds, then deals 200% AP damage to nearby enemies and reduces their speed by 30% for 4 seconds.")

    def activate(self, character, target, crit, board):
        # Simulate Absolute Zero ability for Nunu
        damage = character.ad * (character.critDmg if crit else 1)
        target.take_damage(damage, board)
        print(f"{character.name} uses {self.name}, dealing {damage:.2f} damage to {target.name} {'(CRIT!)' if crit else ''}.")
