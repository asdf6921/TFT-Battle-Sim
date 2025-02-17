# itemAbility.py

class ItemAbility:
    """Base class for all item abilities."""
    def __init__(self, ability_name=None):
        self.ability_name = ability_name

    def activate(self, i, **kwargs):
        """Defines the effect of the item ability. Should be overridden by subclasses."""
        pass


 
class ProtectorsVowAbility(ItemAbility):
    def activate(self, i, **kwargs):
        projectedHP = kwargs.get("projectedHP", None)
        if projectedHP != None:
            if not self.activated[i]:
                if (projectedHP < 0.4 * self.max_hp):
                    self.shielded = True
                    self.shield = 0.25 * self.max_hp
                    self.armor += 20
                    self.mr += 20
                    print(f"{self.name} on {self.team} gained a Protectors Vow shield for {self.shield} hp")
                    self.activated[i] = True

class RedemptionAbility(ItemAbility):
    def activate(self, i, **kwargs):
        pass

class GuinsoosRagebladeAbility(ItemAbility):
    def activate(self, i, **kwargs):
        attacked = kwargs.get("attacked", None)
        if attacked:
            self.speed_multiplier += 0.1

class IonicSparkAbility(ItemAbility):
    def activate(self, i, **kwargs):
        pass

class SterakGageAbility(ItemAbility):
    def activate(self, i, **kwargs):
        projectedHP = kwargs.get("projectedHP", None)
        if projectedHP != None:
            if not self.activated[i]:
                if (projectedHP < 0.6 * self.max_hp):
                    self.hp += 0.25 * self.max_hp
                    self.max_hp *= 1.25
                    self.ad_multiplier += 0.35
                    print(f"{self.name} on {self.team} used sterak's gage")
                    self.activated[i] = True

class DragonClawAbility(ItemAbility):
    def activate(self, i, **kwargs):
        battle = kwargs.get("battle")  # Get battle instance
        attacked = kwargs.get("attacked")
        if attacked:
            return
        if battle is None:
            return  # Safety check

        if self.hp > 0:  # Only heal if the holder is still alive
            heal_amount = self.max_hp * 0.025  # 2.5% max HP
            self.hp = min(self.max_hp, self.hp + heal_amount)
            print(f"{self.name} heals for {heal_amount:.2f}, HP: {self.hp:.2f} at time {battle.time}")

        # Schedule next heal in 2 seconds
        battle.schedule_event(battle.time + 2, "item_ability", (self, i))

class GuardBreakerAbility(ItemAbility):
    def activate(self, i, **kwargs):
        pass

class GargoylesStoneplateAbility(ItemAbility):
    def activate(self, i, **kwargs):
        pass

class BrambleVestAbility(ItemAbility):
    def activate(self, i, **kwargs):
        pass

class GiantSlayerAbility(ItemAbility):
    def activate(self, i, **kwargs):
        pass

class SunfireCapeAbility(ItemAbility):
    def activate(self, i, **kwargs):
        pass

class HandofJusticeAbility(ItemAbility):
    def activate(self, i, **kwargs):
        if not self.activated[i]:
            if self.hp < 0.5 * self.max_hp:
                self.omni += 0.12
                self.ad_multiplier -= 0.15
                self.ap -= 15
                self.activated[i] = True
        if self.activated[i]:
            if self.hp >= 0.5 * self.max_hp:
                self.omni -= 0.12
                self.ad_multiplier += 0.15
                self.ap += 15
                self.activated[i] = False

class EdgeofNightAbility(ItemAbility):
    def activate(self, i, **kwargs):
        projectedHP = kwargs.get("projectedHP", None)
        if projectedHP != None:
            if not self.activated[i]:
                if (projectedHP < 0.6 * self.max_hp):
                    self.shielded = True
                    self.shield = self.hp - projectedHP
                    self.targetable = False
                    self.speed += 0.15
                    self.activated[i] = True

class TitansResolveAbility(ItemAbility):
    def activate(self, i, **kwargs):
        if not self.activated[i]:    
            attacked = kwargs.get("attacked")
            hit = kwargs.get("hit")
            if attacked or hit:
                self.ad_multiplier += 0.02
                self.ap += 2
                self.titanStacks += 1
            if self.titanStacks == 25:
                self.activated[i] = True
                self.armor += 20
                self.mr += 20

class ArchangelsStaffAbility(ItemAbility):
    def activate(self, i, **kwargs):
        battle = kwargs.get("battle")
        attacked = kwargs.get("attacked")
        if attacked:
            return
        if battle is None or battle.time == 0:
            return

        if self.hp > 0:
            self.ap += 30

        battle.schedule_event(battle.time + 5, "item_ability", (self, i))

class EvenshroudAbility(ItemAbility):
    def activate(self, i, **kwargs):
        pass

class NashorsToothAbility(ItemAbility):
    def activate(self, i, **kwargs):
        pass

class MorellonomiconAbility(ItemAbility):
    def activate(self, i, **kwargs):
        pass

class CrownguardAbility(ItemAbility):
    def activate(self, i, **kwargs):
        pass

class AdaptiveHelmAbility(ItemAbility):
    def activate(self, i, **kwargs):
        if not self.activated[i]:
            position = self.position
            if position.x <= 1 or position.x >= 6:
                self.ap += 15
                battle = kwargs.get("battle")
                battle.schedule_event(battle.time + 3, "item_ability", (self, i))
            else:
                self.mr += 40
                self.armor += 40
                self.mana_on_hit = 1
                

class BlueBuffAbility(ItemAbility):
    def activate(self, i, **kwargs):
        pass

class RedBuffAbility(ItemAbility):
    def activate(self, i, **kwargs):
        pass

class LastWhisperAbility(ItemAbility):
    def activate(self, i, **kwargs):
        pass

class SteadfastHeartAbility(ItemAbility):
    def activate(self, i, **kwargs):
        if not self.activated[i]:
            if self.hp < 0.5 * self.max_hp:
                self.dura -= 0.07
                self.activated[i] = True
        if self.activated[i]:
            if self.hp >= 0.5 * self.max_hp:
                self.dura += 0.07
                self.activated[i] = False

class QuickSilverAbility(ItemAbility):
    def activate(self, i, **kwargs):
        pass

class StatikkShivAbility(ItemAbility):
    def activate(self, i, **kwargs):
        pass

class BloodthirsterAbility(ItemAbility):
    """Grants a shield when the holder's HP falls below 40% (once per combat)."""
    def activate(self, i, **kwargs):
        projectedHP = kwargs.get("projectedHP", None)
        if projectedHP != None:
            if not self.activated[i]:
                if (projectedHP < 0.4 * self.max_hp):
                    self.shielded = True
                    self.shield = 0.25 * self.max_hp
                    print(f"{self.name} on {self.team} gained a Bloodthirster shield for {self.shield} hp")
                    self.activated[i] = True
        
