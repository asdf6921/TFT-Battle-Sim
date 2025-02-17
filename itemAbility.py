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
        if not self.activated[i]:
            if (projectedHP < 0.6 * self.max_hp):
                self.hp += 0.25 * self.max_hp
                self.max_hp *= 1.25
                self.ad_multiplier += 0.35
                print(f"{self.name} on {self.team} used sterak's gage")
                self.activated[i] = True

class DragonClawAbility(ItemAbility):
    def activate(self, i, **kwargs):
        pass

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
        pass

class EdgeofNightAbility(ItemAbility):
    def activate(self, i, **kwargs):
        projectedHP = kwargs.get("projectedHP", None)
        if not self.activated[i]:
            if (projectedHP < 0.6 * self.max_hp):
                self.shielded = True
                self.shield = self.hp - projectedHP
                self.targetable = False
                self.speed += 0.15
                self.activated[i] = True

class TitansResolveAbility(ItemAbility):
    def activate(self, i, **kwargs):
        pass

class RunaansHurricaneAbility(ItemAbility):
    def activate(self, i, **kwargs):
        pass

class ArchangelsStaffAbility(ItemAbility):
    def activate(self, i, **kwargs):
        pass

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
        pass

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
        pass

class QuickSilverAbility(ItemAbility):
    def activate(self, i, **kwargs):
        pass

class StatikkShivAbility(ItemAbility):
    def activate(self, i, **kwargs):
        pass

class HextechGunbladeAbility(ItemAbility):
    def activate(self, i, **kwargs):
        pass

class BloodthirsterAbility(ItemAbility):
    """Grants a shield when the holder's HP falls below 40% (once per combat)."""
    def activate(self, i, **kwargs):
        projectedHP = kwargs.get("projectedHP", None)
        if not self.activated[i]:
            if (projectedHP < 0.4 * self.max_hp):
                self.shielded = True
                self.shield = 0.25 * self.max_hp
                print(f"{self.name} on {self.team} gained a Bloodthirster shield for {self.shield} hp")
                self.activated[i] = True
