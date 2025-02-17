from itemAbility import ItemAbility, ProtectorsVowAbility, RedemptionAbility, GuinsoosRagebladeAbility, IonicSparkAbility, SterakGageAbility, DragonClawAbility, GuardBreakerAbility, GargoylesStoneplateAbility, BrambleVestAbility, GiantSlayerAbility, SunfireCapeAbility, HandofJusticeAbility, EdgeofNightAbility, TitansResolveAbility
from itemAbility import RunaansHurricaneAbility, BloodthirsterAbility, ArchangelsStaffAbility, EvenshroudAbility, NashorsToothAbility, MorellonomiconAbility, CrownguardAbility, AdaptiveHelmAbility, BlueBuffAbility, RedBuffAbility, LastWhisperAbility, SteadfastHeartAbility, QuickSilverAbility, StatikkShivAbility, HextechGunbladeAbility

class Item:
    def __init__(self, name, ad=0, ap=0, armor=0, mr=0, speed=0, omni=0, hp = 0, dmgamp=0, mana=0, max_hp=0, unique=False, mana_regen=0, crit=0, dura=0, critdmg=0, abilityCrit=False, ability=ItemAbility):
        self.name = name  
        self.ad = ad  
        self.ap = ap  
        self.armor = armor  
        self.mr = mr  
        self.speed = speed  
        self.omni = omni  
        self.hp = hp
        self.crit = crit
        self.mana = mana
        self.critdmg = critdmg
        self.dura=dura
        self.manaregen = mana_regen
        self.abilityCrit = abilityCrit
        self.unique = unique
        self.max_hp = max_hp
        self.dmgamp = dmgamp  # Damage amplification (e.g., Giant Slayer’s 20% bonus true damage)
        self.ability = ability  # Optional item ability (e.g., Bloodthirster’s lifesteal shield)

    def apply(self, holder):
        holder.ad_multiplier += self.ad
        holder.ap += self.ap
        holder.armor += self.armor
        holder.mr += self.mr
        holder.speed_multiplier += self.speed
        holder.omni += self.omni
        holder.mana += self.mana
        holder.mana_regen += self.manaregen
        holder.hp_multiplier += self.max_hp
        holder.critRate += self.crit
        holder.critDmg += self.critdmg
        if (holder.abilityCrit == False):
            holder.abilityCrit = self.abilityCrit
        holder.dura += self.dura
        holder.dmg_amp += self.dmgamp
        holder.hp += self.hp
    
    def __repr__(self):
        return (f"Item(name={self.name}")
    
class RabadonsDeathcap(Item):
    def __init__(self):
        super().__init__("Rabadon's Deathcap", ap=50, dmgamp=0.15)
class InfinityEdge(Item):
    def __init__(self):
        super().__init__("Infinity Edge", ad=0.35, crit=0.35, critdmg=0.1, abilityCrit=True)
class ProtectorsVow(Item):
    def __init__(self):
        super().__init__("Protector's Vow", armor=20, mana=30, ability=ProtectorsVowAbility)
class Redemption(Item):
    def __init__(self):
        super().__init__("Redemption", hp=150, mana=15, ability=RedemptionAbility)
class GuinsoosRageblade(Item):
    def __init__(self):
        super().__init__("Guinsoo's Rageblade", ap=10, speed=0.1, ability=GuinsoosRagebladeAbility)
class IonicSpark(Item):
    def __init__(self):
        super().__init__("Ionic Spark", ap=15, hp=150, mr=25, ability=IonicSparkAbility)
class SteraksGage(Item):
    def __init__(self):
        super().__init__("Sterak's Gage", hp=150, ad=0.15, ability=SterakGageAbility)
class DragonClaw(Item):
    def __init__(self):
        super().__init__("Dragon's Claw", mr=75, max_hp = 0.09, ability=DragonClawAbility)
class GuardBreaker(Item):
    def __init__(self):
        super().__init__("Guardbreaker", ap=10, speed=0.2, crit=0.2, dmgamp=0.15, hp=150, ability=GuardBreakerAbility)
class GargoylesStoneplate(Item):
    def __init__(self):
        super().__init__("Gargoyle's Stoneplate", armor=25, mr=25, hp=100, ability=GargoylesStoneplateAbility)
class BrambleVest(Item):
    def __init__(self):
        super().__init__("Bramble Vest", armor=65, max_hp=0.07, ability=BrambleVestAbility)
class GiantSlayer(Item):
    def __init__(self):
        super().__init__("Giant Slayer", ad=0.25, ap=25, speed=0.1, dmgamp=0.2, ability=GiantSlayerAbility)
class SunfireCape(Item):
    def __init__(self):
        super().__init__("Sunfire Cape", armor=20, hp=150, max_hp=0.08, unique=True, ability=SunfireCapeAbility)
class HandofJustice(Item):
    def __init__(self):
        super().__init__("Hand of Justice", ad=0.15, ap=15, crit=0.2, mana=15, omni=0.12, ability=HandofJusticeAbility)
class EdgeofNight(Item):
    def __init__(self):
        super().__init__("Edge of Night", ad=0.1, armor=20, ability=EdgeofNightAbility)
class TitansResolve(Item):
    def __init__(self):
        super().__init__("Titan's Resolve", armor=20, speed=0.1, ability=TitansResolveAbility)
class RunaansHurricane(Item):
    def __init__(self):
        super().__init__("Runaan's Hurricane", ad=0.25, speed=0.1, mr=20, ability=RunaansHurricaneAbility)
class Bloodthirster(Item):
    def __init__(self):
        super().__init__("Bloodthirster", ad=0.15, ap=15, mr=20, omni=0.2, ability=BloodthirsterAbility)
class ArchangelsStaff(Item):
    def __init__(self):
        super().__init__("Archangel's Staff", ap=20, mana=15, ability=ArchangelsStaffAbility)
class SpearofShojin(Item):
    def __init__(self):
        super().__init__("Spear of Shojin", ad=0.15, ap=15, mana_regen=5, mana=15)
class Evenshroud(Item):
    def __init__(self):
        super().__init__("Evenshroud", hp=150, mr=20, ability=EvenshroudAbility)
class NashorsTooth(Item):
    def __init__(self):
        super().__init__("Nashor's Tooth", ap=10, speed=0.1, hp=150, ability=NashorsToothAbility)
class Morellonomicon(Item):
    def __init__(self):
        super().__init__("Morellonomicon", ap=25, speed=0.1, hp=150, ability=MorellonomiconAbility)
class Crownguard(Item):
    def __init__(self):
        super().__init__("Crownguard", ap=20, armor=20, hp=100, ability=CrownguardAbility)
class AdaptiveHelm(Item):
    def __init__(self):
        super().__init__("Adaptive Helm", ap=10, mr=20, mana=15, ability=AdaptiveHelmAbility)
class BlueBuff(Item):
    def __init__(self):
        super().__init__("Blue Buff", ad=0.15, ap=15, mana=30, unique=True, ability=BlueBuffAbility)
class RedBuff(Item):
    def __init__(self):
        super().__init__("Red Buff", speed=0.35, dmgamp=0.06, ability=RedBuffAbility)
class LastWhisper(Item):
    def __init__(self):
        super().__init__("Last Whisper", ad=0.15, speed=0.2, crit=0.2, unique=True, ability=LastWhisperAbility)
class JeweledGauntlet(Item):
    def __init__(self):
        super().__init__("Jeweled Gauntlet", ap=35, crit=0.35, critdmg=0.1)
class SteadfastHeart(Item):
    def __init__(self):
        super().__init__("Steadfast Heart", hp=200, armor=20, dura=0.08, crit=0.2, ability=SteadfastHeartAbility)
class QuickSilver(Item):
    def __init__(self):
        super().__init__("Quick Silver", speed=0.3, crit=0.2, mr=20, unique=True, ability=QuickSilverAbility)
class Deathblade(Item):
    def __init__(self):
        super().__init__("Deathblade", ad=0.55, dmgamp=0.15)
class WarmogsArmor(Item):
    def __init__(self):
        super().__init__("Warmog's Armor", hp=600, max_hp=0.12)
class StatikkShiv(Item):
    def __init__(self):
        super().__init__("Statikk Shiv", ap=15, speed=0.15, mana=15, ability=StatikkShivAbility)
class HextechGunblade(Item):
    def __init__(self):
        super().__init__("Hextech Gunblade", ad=0.2, ap=20, omni=0.15, ability=HextechGunbladeAbility)


# Factory function to create items by name
def create_item(item_name):
    item_classes = {
        "Rabadon's Deathcap": RabadonsDeathcap,
        "Infinity Edge": InfinityEdge,
        "Protector's Vow": ProtectorsVow,
        "Redemption": Redemption,
        "Guinsoo's Rageblade": GuinsoosRageblade,
        "Ionic Spark": IonicSpark,
        "Sterak's Gage": SteraksGage,
        "Dragon's Claw": DragonClaw,
        "Guardbreaker": GuardBreaker,
        "Gargoyle Stoneplate": GargoylesStoneplate,
        "Bramble Vest": BrambleVest,
        "Giant Slayer": GiantSlayer,
        "Sunfire Cape": SunfireCape,
        "Hand Of Justice": HandofJustice,
        "Edge of Night": EdgeofNight,
        "Titan's Resolve": TitansResolve,
        "Runaan's Hurricane": RunaansHurricane,
        "Bloodthirster": Bloodthirster,
        "Archangel's Staff": ArchangelsStaff,
        "Spear of Shojin": SpearofShojin,
        "Evenshroud": Evenshroud,
        "Nashor's Tooth": NashorsTooth,
        "Morellonomicon": Morellonomicon,
        "Crownguard": Crownguard,
        "Adaptive Helm": AdaptiveHelm,
        "Blue Buff": BlueBuff,
        "Red Buff": RedBuff,
        "Last Whisper": LastWhisper,
        "Jeweled Gauntlet": JeweledGauntlet,
        "Steadfast Heart": SteadfastHeart,
        "Quicksilver": QuickSilver,
        "Deathblade": Deathblade,
        "Warmog's Armor": WarmogsArmor,
        "Statikk Shiv": StatikkShiv,
        "Hextech Gunblade": HextechGunblade
    }
    return item_classes[item_name]()