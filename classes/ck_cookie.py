from google.protobuf.json_format import Parse, ParseDict
import prot.common_entities_pb2
import prot.game.entities_pb2
import random
import json

from util.uuids import strUUID

with open(r".\resources\characterLists.json", "r", encoding="utf-8") as f:
    characterLists = json.loads(f.read())['characterlists']
with open(r".\resources\cookieSkins.json", "r", encoding="utf-8") as f:
    cookieSkins = json.loads(f.read())['skins']
with open(r".\resources\toppingSubOptionPools.json", "r", encoding="utf-8") as f:
    subOptionPools = json.loads(f.read())['SubOptionPools']
subOptionPools = subOptionPools[:15]
with open(r".\resources\toppingMainOptions.json", "r", encoding="utf-8") as f:
    toppingMainOptions = json.loads(f.read())['MainOptions']
mainOptions = []
for i in toppingMainOptions:
    if not i["ID"] in mainOptions:
        mainOptions.append(i["ID"])
nonSetMainOptions = mainOptions[:50]
setMainOptions = mainOptions[50:]

from enum import Enum

class ToppingStatType(str, Enum):
    ATK = 'AttackPointRatio'
    DEF = 'DefencePointRatio'
    MAXHP = 'HealthPointRatio'
    ATKSPD = 'AttackSpeed'
    CRIT = 'CriticalRate'
    CD = 'Cooltime'
    DMGRES = 'DamageReduceRatio'
    CRITRES = 'CriticalDamageReduceRatio'
    BUFFUP = 'BuffIncrease'
    DEBUFFRES = 'DebuffDecrease'

toppingSetSetToppingsTemplate_All = [ToppingStatType.ATK, ToppingStatType.DEF, ToppingStatType.MAXHP, ToppingStatType.ATKSPD, ToppingStatType.CRIT, ToppingStatType.CD, ToppingStatType.DMGRES, ToppingStatType.CRITRES, ToppingStatType.BUFFUP, ToppingStatType.DEBUFFRES]
toppingSetSetToppingsTemplate_Five = [ToppingStatType.ATK, ToppingStatType.CD, ToppingStatType.CRIT, ToppingStatType.DMGRES, ToppingStatType.ATKSPD]

class ToppingSet(Enum):
    MOONKISSED = 0, toppingSetSetToppingsTemplate_All
    TRIPLE_CONE_CUP = 1, toppingSetSetToppingsTemplate_Five
    DRAGON = 2, toppingSetSetToppingsTemplate_Five
    ROCK_FESTA = 3, toppingSetSetToppingsTemplate_Five
    SEA_SALT = 4, toppingSetSetToppingsTemplate_Five
    GOLDEN_CHEESE = 5, toppingSetSetToppingsTemplate_Five
    FROSTED = 6, toppingSetSetToppingsTemplate_Five
    WINDY = 7, toppingSetSetToppingsTemplate_Five
    DESTRUCTION = 8, toppingSetSetToppingsTemplate_Five
    def __init__(self, setId, setToppings):
        self.setId = setId
        self.setToppings = setToppings

class Rarity(Enum):
    Common = 1
    Rare = 2
    Epic = 3
    Legendary = 4
    Ancient = 5
    Special = 6
    SuperEpic = 7
    Guest = 8
    Awakened = 9
    Beast = 10

class Topping:
    def __init__(self, stattype, rarity=Rarity.Epic, set=None):
        self.id = strUUID(10)
        max_grade = min((3 + (3 * rarity.value)), 15)
        self.grade = max_grade
        self.sub_options = []
        self.topping_slot_index = 0
        self.topping_preset_slot_index = 0
        self.cookie_data_id = 0
        if not set:
            index = 5 * [i.value for i in ToppingStatType].index(stattype.value)
            index += rarity.value - 1
            self.data_id = nonSetMainOptions[index]
        else:
            index = len([topping for i in ToppingSet if i.setId < set.setId for topping in i.setToppings]) if not(set.setId == 0) else 0 # number of toppings in prior sets
            index += set.setToppings.index(stattype)
            self.data_id = setMainOptions[index]
    
    def addSubOption(self, stattype, ratio=0.1):
        optionPoolIDs = [subOptionPool["ID"] for subOptionPool in subOptionPools if subOptionPool["PassiveType"] == stattype.value]
        if len(optionPoolIDs) > 0:
            self.sub_options.append({
                "data_id": optionPoolIDs[0],
                "passive_value_ratio": ratio
            })
        return self
    
    def setGrade(self, grade):
        self.grade = grade
        return self
    
    def equipTo(self, cookie, slot, preset=0):
        self.cookie_data_id = cookie
        self.topping_slot_index = slot
        self.topping_preset_slot_index = preset
        return self
    
    def toDictSummary(self):
        a = {
            "id": self.id,
            "data_id": self.data_id,
            "sub_options": self.sub_options,
            "grade": self.grade,
            "upgrade_failure_count": 0,
            "index_value": {"cookie_data_id": self.cookie_data_id, "topping_preset_slot_index": self.topping_preset_slot_index, "topping_slot_index": self.topping_slot_index},
            "no_marker": {},
        }
        return a

class Cookie:
    def __init__(self, data_id, skin_data_id=None, experience=12796230, grade=10, skill_level=80):
        self.data_id = data_id
        self.experience = experience
        self.skill_level = skill_level
        self.grade = grade
        self.toppings = []
        if skin_data_id is None:
            self.skin_data_id = [i['Id'] for i in cookieSkins if i['CookieId'] == data_id][0]
        else:
            self.skin_data_id = skin_data_id
        self.equipped_equipment_items = []
    
    def equipEquipment(self, dataid):
        self.equipped_equipment_items.append({"data_id": dataid})
        return self
    
    def toDictSummary(self):
        return {
            "data_id": self.data_id,
            "experience": self.experience,
            "skill_level": self.skill_level,
            "grade": self.grade,
            "skin_data_id": self.skin_data_id,
            "equipped_equipment_items": self.equipped_equipment_items,
        }

maximumNotShittyCharacterId = 0
for i in characterLists:
    if i["CharId"] == 1441528484:
        break
    maximumNotShittyCharacterId += 1

def idFromResName(resourceName):
    chl = characterLists[1:maximumNotShittyCharacterId]
    search = {i['ResourceName']:i["CharId"] for i in chl if resourceName in i['ResourceName'] and i["CharId"] > 2000000}
    search = {i:search[i] for i in search if len(i) == 10}
    if resourceName in search:
        return search[resourceName]
    return 0