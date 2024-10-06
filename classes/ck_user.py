from google.protobuf.json_format import Parse, ParseDict
import prot.common_entities_pb2
import prot.game.entities_pb2
import random
import string
import json
from classes import ck_cookie

class User:
    def __init__(self, name, mid="".join(random.choices(string.ascii_uppercase, k=5)) + f'{random.randint(0, 9999):04}'):
        self.mid = mid
        self.name = name
        self.level = 1
        self.kingdom_points = 0
        self.is_kingdom_pass_activated = False
        
        # Inventory
        self.cookies = {}
        
        # Arena
        self.tier = 1411815840
        self.rating = 0
        self.win_count = 0
        self.defense_power = 0
        self.arena_defense_team = []
        self.arena_defense_team = list(self.cookies.keys())[:5] # tmp
    
    def addCookie(self, cookie):
        if not cookie.data_id in self.cookies:
            self.cookies[cookie.data_id] = cookie
        self.arena_defense_team = list(self.cookies.keys())[:5]
        return self

    def toJson(self):
        return json.dumps(
                self,
                default = lambda o: o.__dict__,
                sort_keys=True,
                indent=4
            )

    def toUserSummary(self):
        d = {
            "id": self.mid,
            "name": self.name,
            "level": self.level,
            "kingdom_points": self.kingdom_points,
            #"profile_image": {"data_id": },
            #"user_cake_tower_summary": {...},
            "guild_join_state_summary": {"not_joined": {}},
            "is_kingdom_pass_activated": self.is_kingdom_pass_activated,
            "attending_event_data_ids": [],
            "no_profile_title": {},
            "no_profile_frame": {},
            "no_custom_cookie_summary": {},
        }
        return ParseDict(d, prot.game.entities_pb2.UserSummary())

def generateUser(name):
    a = User(name)
    return a

class Player(User):
    def __init__(self, name, mid):
        super().__init__(name, mid)
        