import random
from ability import MysticShot, AbsoluteZero
from grid import hex_grid
import json

class Character:
    def __init__(self, name, ad, armor, mr, hp, speed, range, mana, max_mana, speed_multiplier=1, hp_multiplier=1, titanStacks=0, omni=0, star_lvl=1, ad_multiplier=1, position=None, team=None, ability=None, dmgAmp=1.0, cost=0, critDmg=1.4, critRate=0.25, dura=0, abilityCrit=False):
        self.name = name
        self.star_lvl = star_lvl
        self.ad = ad
        self.ap = 100
        self.armor = armor
        self.mr = mr
        self.speed = speed
        self.range = range
        self.position = position
        self.omni = omni
        self.mana = mana
        self.max_mana = max_mana
        self.speed_multiplier = speed_multiplier
        self.cost = cost
        self.hp = self.max_hp = hp
        self.hp_multiplier = hp_multiplier
        self.dura = dura
        self.ad_multiplier = ad_multiplier
        self.attack_speed = 1
        self.titanStacks=titanStacks
        self.team=team
        self.critDmg = critDmg
        self.critRate = critRate
        self.abilityCrit = abilityCrit
        self.items = []
        self.mana_regen = 0
        self.targetable = True
        self.shielded = False
        self.shield = 0
        self.healing_reduction = False
        self.revived = False
        self.ad_multiplier = ad_multiplier
        self.dmg_amp = dmgAmp
        self.attack_count = 0
        self.ability = ability
        self.activated = []
        self.effects = {}

    def __lt__(self, other):
        stat1 = random.random()
        stat2 = random.random()
        return stat1 < stat2
    
    def __repr__(self):
        return (f"Character(name={self.name}, position={self.position}, item={self.items}, team={self.team}, star_lvl={self.star_lvl})")
    
    # Block of code for dealing with Effects
    def apply_effect(self, effect_name, duration, magnitude=0, refresh=True):
        """Applies an effect with a duration. If `refresh=True`, it resets duration when reapplied."""
        if effect_name in self.effects and refresh:
            self.effects[effect_name]["duration"] = duration  # Refresh duration
        else:
            self.effects[effect_name] = {"duration": duration, "magnitude": magnitude}

    def tick_effects(self):
        """Reduces effect duration each tick and removes expired ones."""
        expired_effects = []
        for effect, data in self.effects.items():
            data["duration"] -= 1
            if data["duration"] <= 0:
                expired_effects.append(effect)
        
        # Remove expired effects
        for effect in expired_effects:
            del self.effects[effect]

    def has_effect(self, effect_name):
        """Check if the character has an active effect."""
        return effect_name in self.effects
    
    # Updates champion stats at start of game
    def update_stats(self):
        self.max_hp = self.max_hp * self.hp_multiplier
        self.hp = self.max_hp
        if self.critRate > 1:
            self.critDmg += self.critRate - 1
            self.critRate = 1
            
    # Adds an item to the character
    def add_item(self, item):
        self.items.append(item)
        self.activated.append(False)
        item.apply(self)

    # Pathfinding algorithm to find the closest enemy
    def find_closest_enemy(self, board):
        closest_enemy = None
        min_distance = float('inf')
        for character in board.character_positions:
            if character.team != self.team:
                distance = hex_grid.calculate_distance(self.position, board.get_character_position(character))
                if distance < min_distance:
                    min_distance = distance
                    closest_enemy = character
        return closest_enemy
    
    def update_position(self, new_position):
        self.position = new_position

    def walk(self, target, board):
        """Move the character 1 step closer to the target, prioritizing diagonal movement."""
        x, y = self.position

        possible_moves = [
            (x + 1, y), (x - 1, y),  # Horizontal moves
            (x, y + 1), (x, y - 1),  # Vertical moves
            (x + 1, y - 1), (x - 1, y + 1)  # Diagonal moves
        ]

        # Filter out moves that are out of bounds or occupied
        valid_moves = [
            (new_x, new_y) for new_x, new_y in possible_moves
            if 0 <= new_x < board.rows and 0 <= new_y < board.cols and board.board[new_x][new_y] == ''
        ]

        # Sort valid moves by distance to the target
        valid_moves.sort(key=lambda pos: hex_grid.calculate_distance(pos, target.position))

        if valid_moves:
            self.position = valid_moves[0]
            print(f"{self.name} moves to {self.position}")
        else:
            print(f"{self.name} is blocked and stays at {self.position}")

    
    # Function to take damage
    def take_damage(self, attacker, damage, board):
        actual_dmg = damage * (1 - (self.armor) / (self.armor + 100))
        projected_hp = self.hp - (actual_dmg - self.shield)
        hit = True
        self.use_item_ability(projectedHP=projected_hp, hit=hit)
        if attacker.omni != 0:
            attacker.heal(actual_dmg * attacker.omni)
        for item in attacker.items:
            if item.name == "Hextech Gunblade":
                ally = board.get_lowest_percent_health_ally(attacker)
                if ally != None:
                    ally.heal(actual_dmg * 0.2)
        if self.shield > 0:
            shield_damage = min(actual_dmg, self.shield)
            self.shield -= shield_damage
            actual_dmg -= shield_damage
        if actual_dmg > 0:
            self.hp -= max(0, actual_dmg)
            if self.hp <= 0:
                board.remove_character(self)
            print(f"{self.name} takes {damage:.2f} damage but is reduced by {damage - actual_dmg}. {self.name}'s HP: {self.hp}")

    # Function to attack
    def attack(self, board, time, battle):
        target = self.find_closest_enemy(board)
        # Specifically for runaans
        attacked_enemies = set()
        self.attack_count += 1
        if target != None:
            distance = hex_grid.calculate_distance(self.position, target.position)
            if distance > self.range:
                self.walk(target, board)
                battle.schedule_event(battle.time + (1 / self.speed * self.speed_multiplier), "attack", self)
            else:
                projectedHP = self.hp
                attacked = True
                targetHP = target.hp
                self.use_item_ability(projectedHP=projectedHP, attacked=attacked, targetHP=targetHP, battle=battle, board=board)
                crit = random.random() < self.critRate  # Determines if attack is a crit
                damage = self.ad * self.ad_multiplier * (self.critDmg if crit else 1) * self.dmg_amp
                for item in self.items:
                    if item.name == "Runaan's Hurricane":
                        enemy = board.get_second_enemy(self, target, exclude=attacked_enemies)
                        if enemy:
                            enemy.take_damage(self, 0.6 * damage, board)
                            attacked_enemies.add(enemy)
                print(f"{self.name} on team {self.team} attacks {target.name} on team {target.team} for {damage:.2f} damage {'(CRIT!)' if crit else ''} at time {time}")
                target.take_damage(self, damage, board)
                self.mana += 10
                battle.schedule_event(battle.time + (1 / self.speed * self.speed_multiplier), "attack", self)
                #if self.mana >= self.max_mana:
                #    self.use_ability(target, board)

    #Function for healing
    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
        print(f"{self} healed {amount}")

    # Function to use item ability
    def use_item_ability(self, **kwargs):
        for i, item in enumerate(self.items):
            crit = random.random() < self.critRate if self.abilityCrit else False
            item.ability.activate(self, i, **kwargs)

    # Function to use ability
    def use_ability(self, target, board):
        if self.mana >= self.max_mana:
            print(f"{self.name} on team {self.team} uses {self.ability.name} on {target.name} team {target.team}")
            self.mana -= self.max_mana
            crit = random.random() < self.critRate if self.abilityCrit else False
            self.ability.activate(self, target, crit, board)

    # Builds a character from a JSON file
    @staticmethod
    def create_character(name, position, team):
        with open('/Users/jerry/Desktop/TFT Battle Sim/second_filtered_champions.json') as f:
            champions_data = json.load(f)

        champion = next((champ for champ in champions_data if champ['name'] == name), None)
        if not champion:
            raise ValueError(f"Champion {name} not found in the data.")

        stats = champion['stats']
        if not stats:
            raise ValueError(f"Champion {name} not found in the data.")

        return Character(
            name=name,
            cost=champion['cost'],
            ad=stats['damage'],
            armor=stats['armor'],
            mr=stats['magicResist'],
            speed=stats['attackSpeed'],
            range=stats['range'],
            mana=stats['initialMana'],
            max_mana=stats['mana'],
            position=position,
            team=team,
            hp=stats['hp']
        )
