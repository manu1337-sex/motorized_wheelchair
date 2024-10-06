from ast import List
from dataclasses import dataclass
from google.protobuf.json_format import Parse, ParseDict, MessageToJson, MessageToDict
import prot.common_entities_pb2
import prot.game.entities_pb2
from util.uuids import strUUID
from util.unixtime import getTime, ckTime
import random
import string
from classes import ck_cookie
from typing import Self

class Structure:
    def __init__(self, data_id):
        self.id = strUUID(12)
        self.data_id = data_id
        self.level = 0
        self.craft_queue_expansion_count = 0
        self.was_broken = False
        self.fountain_production = {}
        self.auto_production = {}
        self.merged_structures = []
        self.last_updated_at = ckTime(getTime())
        self.construction_status = {}
        self.first_placed_at = ckTime(getTime())

# :sob:
class RewardElement:
    def __init__(self):
        self.reward = {}
    def coin(self, amount: int) -> Self:
        self.reward['coin'] = amount
        return self
    def crystal(self, amount: int) -> Self:
        self.reward['crystal'] = amount
        return self
    def rainbow_cube(self, amount: int) -> Self:
        self.reward['rainbow_cube'] = amount
        return self
    def rainbow_crystal(self, amount: int) -> Self:
        self.reward['rainbow_crystal'] = amount
        return self
    def kingdom_point(self, amount: int) -> Self:
        self.reward['kingdom_point'] = amount
        return self
    def kingdom_pass_mission_point(self, amount: int) -> Self:
        self.reward['kingdom_pass_mission_point'] = amount
        return self
    def stamina(self, amount: int) -> Self:
        self.reward['stamina'] = amount
        return self
    def pvp_ticket(self, amount: int) -> Self:
        self.reward['pvp_ticket'] = amount
        return self
    def pvp_smash_ticket(self, amount: int) -> Self:
        self.reward['pvp_smash_ticket'] = amount
        return self
    def pvp_reset_ticket(self, amount: int) -> Self:
        self.reward['pvp_reset_ticket'] = amount
        return self
    def pvp_medal(self, amount: int) -> Self:
        self.reward['pvp_medal'] = amount
        return self
    def mileage_point(self, amount: int) -> Self:
        self.reward['mileage_point'] = amount
        return self
    def guild_battle_ticket(self, amount: int) -> Self:
        self.reward['guild_battle_ticket'] = amount
        return self
    def guild_battle_medal(self, amount: int) -> Self:
        self.reward['guild_battle_medal'] = amount
        return self
    def cookie_look_gacha_item(self, data_id: int) -> Self:
        self.reward['cookie_look_gacha_item'] = data_id
        return self
    def treasure(self, new_treasure: bool, data_id: int, count: int, level: int | None) -> Self:
        if new_treasure:
            self.reward['treasure'] = {
                 'new_treasure': {
                     'data_id': data_id,    
                     'level': level,    
                     'count': count   
                 }
            }
        else:
            self.reward['preexisting_treasure'] = {
                 'new_treasure': {
                     'data_id': data_id,    
                     'amount': count
                 }
            }
        return self
    def cookie(self, cookie: ck_cookie.Cookie) -> Self:
        if cookie:
            self.reward['cookie'] = {
                 'new_cookie': {
                     'cookie': cookie.toDictSummary()
                 }
            }
        return self
    def structure(self, structure_data_id: int, structure: Structure | int) -> Self:
        if isinstance(structure, int):
            return {
                'structure_data_id': structure_data_id,
                'fallback_crystal': structure
            }
        else:
            return {
                'structure_data_id': structure_data_id,
                'structure': structure
            }
        return self

class Reward:
    def __init__(self, name):
        self.origin_reward = {}
        self.converted_reward = {}
        self.additional_rewards = []
    
    def toReward(self) -> dict:
        d = {
            "additional_rewards": self.additional_rewards
        }
        origin_reward_oneof_fieldname = 'origin_reward_value' if self.origin_reward else 'no_reward'
        converted_reward_oneof_fieldname = 'converted_reward_value' if self.converted_reward else 'no_converted_reward'
        d[origin_reward_oneof_fieldname] = self.origin_reward
        d[converted_reward_oneof_fieldname] = self.converted_reward
        return d
    
    def setOriginReward(self, reward: RewardElement) -> Self:
        self.origin_reward = reward
        self.converted_reward = {}
        return self
    
    def setConvertedReward(self, rewards: List[RewardElement], replaced_origin_quantity: int, replaced_origin_data_id: int) -> Self:
        self.converted_reward = {
            'rewards': rewards,
            'replaced_origin_quantity': replaced_origin_quantity,
            'replaced_origin_data_id': replaced_origin_data_id
        }
        self.origin_reward = {}
        return self
    
    def addAdditionalReward(self, origin_data_id: int, reward: RewardElement) -> Self:
        self.additional_rewards.append({
            "origin_data_id": origin_data_id,
            "reward": reward,
        })
        return self

    def serialize(self):
        return ParseDict(self.toReward(), prot.game.entities_pb2.Reward())