from ast import List
from dataclasses import dataclass
from google.protobuf.json_format import Parse, ParseDict, MessageToJson, MessageToDict
import prot.common_entities_pb2
import prot.game.entities_pb2
from util.uuids import strUUID
from util.unixtime import getTime, ckTime, never
import random
import string
from classes import ck_cookie

class Mail:
    def __init__(self, title):
        self.id = strUUID(11)
        self.description = {"title": title, "language_type": "EN"}
        self.rewards = []
        self.created_at = getTime()
        self.is_rewarded = False
    
    def addReward(self, dataId, amount):
        self.rewards.append({
            "item_data_id": dataId,
            "amount": amount
        })
        return self

    def toDict(self):
        return {
            "id": self.id,
            "detail": {
                "normal": {
                    "descriptions": [
                        self.description
                    ]
                }
            },
            "rewards": self.rewards,
            "isRewarded": self.is_rewarded,
            "expiresAt": ckTime(never),
            "receivedAt": ckTime(self.created_at)
        }