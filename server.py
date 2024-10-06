from google.protobuf.json_format import Parse, ParseDict, MessageToJson, MessageToDict
import grpc
import time
import random
import json
import secrets
import uuid
from concurrent import futures
from classes import ck_user
from classes import ck_cookie

from util.uuids import strUUID
from util.unixtime import getTime, ckTime

import prot.common_entities_pb2
import prot.common_entities_pb2_grpc
import prot.game.entities_pb2
import prot.game.entities_pb2_grpc
import prot.game.kingdom_pb2
import prot.game.kingdom_pb2_grpc
import prot.game.routing_pb2
import prot.game.routing_pb2_grpc
import prot.game.time_pb2
import prot.game.time_pb2_grpc
import prot.game.user_pb2
import prot.game.user_pb2_grpc
import prot.game.shop_pb2
import prot.game.shop_pb2_grpc
import prot.game.mail_pb2
import prot.game.mail_pb2_grpc
import prot.game.adventure_pb2
import prot.game.adventure_pb2_grpc
import prot.game.pvp_pb2
import prot.game.pvp_pb2_grpc
import prot.game.cutscene_pb2
import prot.game.cutscene_pb2_grpc

def MakeKAEV():
    with open('./resources/kaev.json') as json_data:
        d = json_data.read()
    return Parse(d, prot.game.entities_pb2.KingdomAdditionalEvents())

users = {user.mid: user for user in [
    ck_user.generateUser(":3"),
    ck_user.generateUser("whale")
        .addCookie(ck_cookie.Cookie(ck_cookie.idFromResName("cookie0602"), grade=6))
        .addCookie(ck_cookie.Cookie(ck_cookie.idFromResName("cookie0613")))
        .addCookie(ck_cookie.Cookie(ck_cookie.idFromResName("cookie0070")))
        .addCookie(ck_cookie.Cookie(ck_cookie.idFromResName("cookie0601"), grade=6))
        .addCookie(ck_cookie.Cookie(ck_cookie.idFromResName("cookie0508"))),
    ck_user.generateUser(":33")
]}

class RoutingServiceServicer(prot.game.routing_pb2_grpc.RoutingServiceServicer):
    def GetServerGroups(self, request, context):
        return ParseDict({
            "serverGroupInfos": [
                {
                "serverGroup": "pv",
                "serverGroupComment": {
                    "noComment": {}
                }
                },
                {
                "serverGroup": "hb",
                "serverGroupComment": {
                    "noComment": {}
                }
                },
                {
                "serverGroup": "dc",
                "serverGroupComment": {
                    "noComment": {}
                }
                }
            ]}, prot.game.routing_pb2.GetServerGroupsResponse())
    def GetCorrespondingServerGroup(self, request, context):
        return ParseDict({
            "serverGroupValue": "dc"
            }, prot.game.routing_pb2.GetCorrespondingServerGroupResponse())

class TimeServiceServicer(prot.game.time_pb2_grpc.TimeServiceServicer):
    def GetDateTime(self, request, context):
        return ParseDict({
            "dateTime": ckTime(getTime())
            }, prot.game.time_pb2.GetDateTimeResponse())

import queue

class UserServiceServicer(prot.game.user_pb2_grpc.UserServiceServicer):
    def GetNotificationStream(self, request, context):
        for i in range(100):
            pass
            yield ParseDict({}, prot.common_entities_pb2.Empty())

class KingdomServiceServicer(prot.game.kingdom_pb2_grpc.KingdomServiceServicer):
    def SignUp(self, request, context):
        with open('signup.json') as json_data:
            d = json_data.read()
        SignUpResponse = Parse(d, prot.game.kingdom_pb2.SignUpResponse())
        a = {
            "data_id": 1286231486,
            "experience": 12796230,
            "skill_level": 80,
            "grade": 5,
            "skin_data_id": 1531390254,
        }
        SignUpResponse.kingdom_state.cookies.acquired.extend([ParseDict(a, prot.game.entities_pb2.Cookie())])
        SignUpResponse.kingdom_state.mileage_points = 100000
        SignUpResponse.kingdom_state.rainbow_cubes = 100000
        SignUpResponse.kingdom_state.rainbow_crystals = 100000
        SignUpResponse.kingdom_state.stamina.points = 100000
        SignUpResponse.kingdom_state.crystals = 100000
        SignUpResponse.kingdom_state.coins = 100000
        SignUpResponse.guild_activity_state.join_state.joined.guild.name = "I love MariahPS"
        aaa = {
            "1927523849": 1446035896,
            "1506290305": 1902304035,
            "1121542873": 1978689293,
            "2005175968": 1580384064,
        }
        for cookie in SignUpResponse.kingdom_state.cookies.acquired:
            if str(cookie.data_id) in aaa:
                cookie.skin_data_id = aaa[str(cookie.data_id)]
        return SignUpResponse
    def CheckKingdomNameExists(self, request, context):
        CheckNameExistsRsp = ParseDict({"exists": False}, prot.game.kingdom_pb2.CheckKingdomNameExistsResponse())
        return CheckNameExistsRsp
    def ChangeKingdomName(self, request, context):
        ChangeKingdomNameRsp = ParseDict({
            "changed_kingdom_name": request.kingdom_name,
            "payments": [],
        }, prot.game.kingdom_pb2.ChangeKingdomNameResponse())
        ChangeKingdomNameRsp.additional_events.CopyFrom(MakeKAEV())
        return ChangeKingdomNameRsp
    def SetBattleTeam(self, request, context):
        SetBattleTeamRsp = prot.game.kingdom_pb2.SetBattleTeamResponse()
        SetBattleTeamRsp.additional_events.CopyFrom(MakeKAEV())
        SetBattleTeamRsp.battle_team_index = request.battle_team_index
        SetBattleTeamRsp.battle_team.CopyFrom(request.battle_team)
        SetBattleTeamRsp.battle_type = request.battle_type
        return SetBattleTeamRsp

class AdventureServiceServicer(prot.game.adventure_pb2_grpc.AdventureServiceServicer):
    def UpdateAdventureInfo(self, request, context):
        d = {
            "updated_daily_dungeon_state": {
                "no_ongoing_dungeon": {},
                "opened_dungeons": [],
                "play_limit_state": {"remaining_play_count": 10, "remaining_charge_count": 1},
                "expires_at": ckTime(getTime(10000)),
                "records": [],
                "bounty_states": []
            },
            "pvp_summary": {"activated": {"tier": 1411815840, "pvp_season_data_id_value": 1886241899, "tickets": "69"}},
            "guild_battle_ticket_state": {"battle_season_data_id_value": 1968080620, "tickets": "95", "expires_at": ckTime(getTime(694200))},
            "pending_smash_season_data_ids": [],
            "pending_pvp_season_data_ids": [],
            "pending_beast_raid_season_data_ids": [],
            "updated_jam_stone_dungeon_state": {"no_ongoing_dungeon": {}, "play_limit_state": {"remaining_play_count": 7, "max_play_count": 69, "expires_at": ckTime(getTime(694200))}, "records": []},
            "social_raids": {"seasons": [], "no_ongoing_battle": {}}
        }
        updateAdventureInfoRsp = ParseDict(d, prot.game.adventure_pb2.UpdateAdventureInfoResponse())
        updateAdventureInfoRsp.additional_events.CopyFrom(MakeKAEV())
        return updateAdventureInfoRsp

class PvpServiceServicer(prot.game.pvp_pb2_grpc.PvpServiceServicer):
    def UpdatePvp(self, request, context):
        d = {
            "pvp": {
                "is_activated": True,
                "tier": 1411815840,
                "rating": 0,
                "win_count": 0,
                "opponent_pool": {
                    "entries": [
                        {
                            "id": strUUID(12),
                            "status": "READY",
                            "pvp_opponent": {
                                "kind": { "user": { "user_summary": MessageToDict(user.toUserSummary()) } },
                                "is_activated": True,
                                "tier": user.tier,
                                "rating": user.rating,
                                "win_count": user.win_count,
                                "defense_power": user.defense_power,
                                "cookies": [
                                    {"public": {
                                        "cookie": user.cookies[cookieId].toDictSummary(),
                                        "location_index": (i%3)+1
                                    }} for i,cookieId in enumerate(user.arena_defense_team)
                                ],
                                "treasures": [],
                                "is_redacted": False,
                                "equipped_equipment_items": [],
                                "attached_podium_parts": {"no_attached_pvp_podium_parts_value": {}},
                                "no_leader_cookie_data_id": {}
                            }
                        }
                    for user in random.choices(list(users.values()), k=1)],
                    "next_reset_at": ckTime(getTime(10000))
                },
                "defense_deck": {
                    "cookies": [
                        {"data_id": 1788308175}
                    ],
                    "treasure_data_ids": [],
                    "no_leader_cookie_data_id": {}
                },
                "tickets": 9,
                "tickets_last_updated_at": ckTime(getTime(-1)),
                "max_rewarded_tier": 1411815840,
                "max_rewardable_tier": 1411815840,
                "last_notified_tier": 1411815840,
                "pvp_season_data_id_value": 1860993160,
                "is_season_notified": True,
                "pvp_opponent_pool_reset_with_crystal_count": {
                    "reset_count": 1,
                    "expires_at": ckTime(getTime(200))
                },
                "season_results": [],
                "season_results_history": [],
                "winning_streak_state": {
                    "wins": 1,
                    "last_updated_at": ckTime(getTime(-200))
                },
                "attached_podium_parts": {"no_attached_pvp_podium_parts_value": {}},
            }
        }
        updatePvpRsp = ParseDict(d, prot.game.pvp_pb2.UpdatePvpResponse())
        updatePvpRsp.additional_events.CopyFrom(MakeKAEV())
        return updatePvpRsp
    def StartPvpBattle(self, request, context):
        d = {
            "ongoing_battle": {
                "id": f"PB{str(uuid.uuid4())}",
                "started_at": ckTime(getTime()),
                "pvp_attack_deck_detail": {
                    "cookies": [
                        {"cookie": ck_cookie.Cookie(1506290305, 1902304035).toDictSummary()},
                        {"cookie": ck_cookie.Cookie(1121542873, 1978689293).toDictSummary()},
                    ],
                    "treasures": [],
                    "leaderCookieDataIdValue": 1506290305,
                },
                "pvp_opponent_detail": {
                    "kind": {
                        "user": {
                            "user_summary": MessageToDict(users[list(users.keys())[0]].toUserSummary())
                        }
                    },
                    "is_activated": True,
                    "tier": 1411815840,
                    "rating": 0,
                    "win_count": 0,
                    "defense_power": 0,
                    "defense_deck": {
                        "cookies": [
                            {
                                "cookie": ck_cookie.Cookie(id, 0, grade=1, experience=1, skill_level=1).toDictSummary(),
                                "selected_topping_preset_index": 0,
                                "selected_beascuit_preset_index": 0,
                            }
                            for id in [ck_cookie.idFromResName("cookie0602"),1540216]
                        ],
                        "cookies": [
                            {
                                "cookie": ck_cookie.Cookie(ck_cookie.idFromResName("cookie0602"), 0, grade=1, experience=1000, skill_level=1).toDictSummary(),
                                "selected_topping_preset_index": 0,
                                "selected_beascuit_preset_index": 0,
                            },
                            {
                                "cookie": ck_cookie.Cookie(1540216, 0, grade=1, experience=1, skill_level=1).toDictSummary(),
                                "selected_topping_preset_index": 0,
                                "selected_beascuit_preset_index": 0,
                            },
                            {
                                "cookie": ck_cookie.Cookie(1311492, 0, grade=1, experience=1, skill_level=1).toDictSummary(),
                                "selected_topping_preset_index": 0,
                                "selected_beascuit_preset_index": 0,
                            },
                            {
                                "cookie": ck_cookie.Cookie(1310441, 0, grade=1, experience=1, skill_level=1).toDictSummary(),
                                "selected_topping_preset_index": 0,
                                "selected_beascuit_preset_index": 0,
                            },
                        ],
                        "treasures": [],
                        "no_leader_cookie_data_id": {}
                    },
                    "battle_passives": {},
                    "cookie_passives": {},
                    "hot_time_battle_buffs": {},
                    "topping_equipments": [],
                    "beascuit_equipments": [],
                    "no_guild_level": {},
                    "equipped_equipment_items": [],
                    "attached_podium_parts": {"no_attached_pvp_podium_parts_value": {}},
                },
                "random_seed": 69420,
                "no_spec_adjustment_group_data_id": {},
            },
            "team_detail": {
                "decks": [
                    {
                        "cookies": [
                            {"my_cookie_detail": 
                                {"cookie": ck_cookie.Cookie(ck_cookie.idFromResName("cookie0024"), 0, grade=10, experience=12796230, skill_level=800).toDictSummary()},
                            },
                        ],
                        "treasures": [
                            {"my_treasure_detail": {"data_id": 1760113461, "level": 1500}},
                            {"my_treasure_detail": {"data_id": 1158110465, "level": 1500}},
                            {"my_treasure_detail": {"data_id": 1399313294, "level": 1500}},
                        ],
                        "leaderCookieDataIdValue": 1506290305,
                    }
                ],
                "battle_passives": {},
                "cookie_passives": {},
                "topping_equipments": [
                    {"cookie_data_id": ck_cookie.idFromResName("cookie0024"), "toppings": [
                        ck_cookie.Topping(ck_cookie.ToppingStatType.CD, ck_cookie.Rarity.Ancient).setGrade(100)
                            .addSubOption(ck_cookie.ToppingStatType.MAXHP, 500)
                            .addSubOption(ck_cookie.ToppingStatType.DMGRES, 500)
                            .addSubOption(ck_cookie.ToppingStatType.ATK, 500)
                            .addSubOption(ck_cookie.ToppingStatType.DEF, 500)
                            .equipTo(ck_cookie.idFromResName("cookie0024"), 0)
                            .toDictSummary(),
                    ]}
                ],
                "beascuit_equipments": [],
                "equipped_equipment_items": [],
                "hot_time_battle_buffs": {},
            },
            "payments": [],
            "my_rank": 212,
            "opponent_rank": 152
        }
        startPvpBattleRsp = ParseDict(d, prot.game.pvp_pb2.StartPvpBattleResponse())
        startPvpBattleRsp.additional_events.CopyFrom(MakeKAEV())
        startPvpBattleRsp.ongoing_battle.kind.CopyFrom(request.battle_kind)
        startPvpBattleRsp.pvp_type = request.pvp_type
        startPvpBattleRsp.battle_team_index = request.battle_team_index
        return startPvpBattleRsp
    def FinishPvpBattle(self, request, context):
        d = {
            "rating": 69420,
            "rating_delta": 69420,
            "rewards": [
                {"origin_reward_value": {"pvp_medal": "10"}, "no_converted_reward": {}},
                {"origin_reward_value": {"kingdom_point": "2000"}, "no_converted_reward": {}}
            ],
            "no_master_league_information": {},
            "winning_streak_bonus": 0,
            "red_flag": False,
        }
        updatePvpRsp = ParseDict(d, prot.game.pvp_pb2.FinishPvpBattleResponse())
        updatePvpRsp.additional_events.CopyFrom(MakeKAEV())
        updatePvpRsp.finished_battle_id = request.battle_id
        updatePvpRsp.pvp_type = request.pvp_type
        return updatePvpRsp
    def PreFinishPvpBattle(self, request, context):
        d = {}
        updatePvpRsp = ParseDict(d, prot.game.pvp_pb2.PreFinishPvpBattleResponse())
        updatePvpRsp.additional_events.CopyFrom(MakeKAEV())
        updatePvpRsp.battle_id = request.battle_id
        return updatePvpRsp
    def CheckPvpTierChangeNotification(self, request, context):
        d = {
            "max_rewarded_tier": 1411815840,
            "max_rewardable_tier": 1411815840,
            "last_notified_tier": 1411815840,
            "tier_rewards": [],
        }
        tierChangePvpRsp = ParseDict(d, prot.game.pvp_pb2.CheckPvpTierChangeNotificationResponse())
        tierChangePvpRsp.additional_events.CopyFrom(MakeKAEV())
        tierChangePvpRsp.pvp_type = request.pvp_type
        return tierChangePvpRsp

class ShopServiceServicer(prot.game.shop_pb2_grpc.ShopServiceServicer):
    def RegisterShownPackagePopup(self, request, context):
        IDs = request.package_data_ids
        popup = prot.game.shop_pb2.RegisterShownPackagePopupResponse()
        popup = ParseDict({
                "updated_package_states": [{
                    "packageDataId": ID,
                    "lastPurchasedAt": {},
                    "popupLastShownAtValue": ckTime(1727725741813),
                    "purchaseLimitBonus": {"packageDataId": ID},
                    "extensions": [{
                        "timeDeal": {"timeDealBegunAt": ckTime(1727725311512)}
                        }]
                    } for ID in IDs]
                }, popup)
        popup.additional_events.CopyFrom(MakeKAEV())
        return popup
    def PurchaseSummon(self, request, context):
        popup = prot.game.shop_pb2.PurchaseSummonResponse()
        a = {
              "payments": [{"crystal": 0}],
              "rewards": [
                 {
                     "noReward": {},
                     "convertedRewardValue": {
                         "rewards": [
                             {"stackableItem": {"dataId": 1741079847, "amount": "1"}},
                             {"mileagePoint": "10000000000"}
                         ],
                         "replacedOriginQuantity": "1",
                         "replacedOriginDataId": 1286231486
                     }
                 },
                 { 
                    "originRewardValue": {
                        "cookie": {
                            "newCookie": {
                                "cookie": {
                                    "dataId": 1338875233,
                                    "skillLevel": 1,
                                    "skinDataId": 1179453731
                                },
                                "noOverflowedBeyondSoulStoneReward": {}
                            }
                        }
                    },
                    "noConvertedReward": {},
                    "additionalRewards": [{"originDataId": 1169674760, "reward": {"mileagePoint": 0}}]
                 },
              ],
              "noFreeSummon": {},
              "bonusRewards": [{"originRewardValue": {"mileagePoint": 0},"noConvertedReward": {}}],
              "summonStates": {"summonUpperBoundStateCounts": {}, "receivedSummonRewardSteps": {}}
        }
        a = {
              "payments": [{"crystal": 0}],
              "rewards": [
                 {"originRewardValue": {"stackable_item": {"data_id": 1215980795, "amount": 1}}},
              ],
              "noFreeSummon": {},
              "bonusRewards": [{"originRewardValue": {"mileagePoint": 0},"noConvertedReward": {}}],
              "summonStates": {"summonUpperBoundStateCounts": {}, "receivedSummonRewardSteps": {}}
        }
        popup = ParseDict(a, popup)
        popup.additional_events.CopyFrom(MakeKAEV())
        return popup
    
from classes import ck_mail

localMails = [
    ck_mail.Mail("Welcome to MariahPS!! <3").addReward(1215980795, 69420)
]

class MailServiceServicer(prot.game.mail_pb2_grpc.MailServiceServicer):
    def GetMailBox(self, request, context):
        popup = prot.game.mail_pb2.GetMailBoxResponse()
        popup = ParseDict({
                "mail_box": {
                    "mails": [mail.toDict() for mail in localMails]
                }
                }, popup)
        return popup
    def ReceiveMailRewards(self, request, context):
        popup = prot.game.mail_pb2.ReceiveMailRewardsResponse()
        for mail in localMails:
            mail.is_rewarded = True
        popup = ParseDict({
                "updated_mails": [mail.toDict() for mail in localMails],
                "rewards": [{
                    "originRewardValue": {
                        "stackableItem": {
                            "dataId": reward["item_data_id"],
                            "amount": reward["amount"]
                        }
                    },
                    "noConvertedReward": {}} for reward in [reward for mail in localMails for reward in mail.rewards]]
                }, popup)
        popup.additional_events.CopyFrom(MakeKAEV())
        return popup

class CutsceneServiceServicer(prot.game.cutscene_pb2_grpc.CutsceneServiceServicer):
    def RegisterPlayedCutscenes(self, request, context):
        RegisterPlayedCutscenesRsp = prot.game.cutscene_pb2.RegisterPlayedCutscenesResponse()
        RegisterPlayedCutscenesRsp.additional_events.CopyFrom(MakeKAEV())
        RegisterPlayedCutscenesRsp.registered_cutscene_ids.CopyFrom(request.cutscene_ids())
        return RegisterPlayedCutscenesRsp
    def CompleteTutorials(self, request, context):
        CompleteTutorialsRsp = prot.game.cutscene_pb2.CompleteTutorialsResponse()
        CompleteTutorialsRsp.additional_events.CopyFrom(MakeKAEV())
        CompleteTutorialsRsp.appended_tutorial_data_ids.CopyFrom(request.tutorial_data_ids())
        CompleteTutorialsRsp.rewards = []
        return CompleteTutorialsRsp

import prot.game.episode_pb2
import prot.game.episode_pb2_grpc

class EpisodeServiceServicer(prot.game.episode_pb2_grpc.EpisodeServiceServicer):
    def UpdateEpisodeLandMutation(self, request, context):
        UpdateEpisodeLandMutationRsp = ParseDict({"episode_land_mutation": {"no_season": {}}}, prot.game.episode_pb2.UpdateEpisodeLandMutationResponse())
        UpdateEpisodeLandMutationRsp.additional_events.CopyFrom(MakeKAEV())
        return UpdateEpisodeLandMutationRsp

import prot.game.town_pb2
import prot.game.town_pb2_grpc

class TownServiceServicer(prot.game.town_pb2_grpc.TownServiceServicer):
    def EditTown(self, request, context):
        rsp = {
            "payments": [],
            "rewards": [],
            "structure_ids_by_dummy_id": {},
        }
        town_changes = []
        for command in request.commands:
            editCommand = command.WhichOneof('value')
            match editCommand:
                case "stash":
                    town_changes.append({
                        "stashed": {
                            "id": command.stash.structure_id,
                            "data_id": 0,
                            "stashed_at": ckTime(getTime()),
                        }
                    })
                case "update":
                    town_changes.append({
                        "updated": {
                            "id": command.update.structure_id,
                            "placement": MessageToDict(command.update.placement),
                            "data_id": 0,
                            "updated_at": ckTime(getTime()),
                        }
                    })
                case "unstash":
                    town_changes.append({
                        "unstashed": {
                            "id": command.unstash.structure_id,
                            "placement": MessageToDict(command.unstash.placement),
                            "data_id": 0,
                            "unstashed_at": ckTime(getTime()),
                            "first_placed_at": ckTime(getTime()),
                        }
                    })
                case _:
                    return
        
        rsp["town_changes"] = town_changes
        EditTownRsp = ParseDict(rsp, prot.game.town_pb2.EditTownResponse())
        EditTownRsp.additional_events.CopyFrom(MakeKAEV())
        return EditTownRsp

import prot.game.topping_pb2
import prot.game.topping_pb2_grpc

class ToppingServiceServicer(prot.game.topping_pb2_grpc.ToppingServiceServicer):
    def EquipTopping(self, request, context):
        topping = ck_cookie.Topping(ck_cookie.ToppingStatType.ATK, ck_cookie.Rarity.Common).addSubOption(ck_cookie.ToppingStatType.ATK, 1000).setGrade(50)
        topping.equipTo(request.cookie_data_id, request.topping_slot_index, request.preset_slot_index)
        a = {
            "topping": topping.toDictSummary(),
            "unequip_payments": [],
            "preexisting_topping": {"no_topping_value": {}},
            "vanilla_topping_payment": {"no_payment_value": {}},
        }
        EquipToppingRsp = ParseDict(a, prot.game.topping_pb2.EquipToppingResponse())
        EquipToppingRsp.additional_events.CopyFrom(MakeKAEV())
        return EquipToppingRsp
    def UnequipTopping(self, request, context):
        topping = ck_cookie.Topping(ck_cookie.ToppingStatType.CD, ck_cookie.Rarity.Ancient).addSubOption(ck_cookie.ToppingStatType.ATK, 100)
        topping.equipTo(request.cookie_data_id, request.topping_slot_index, request.preset_slot_index)
        a = {
            "topping": topping.toDictSummary(),
            "payments": [],
        }
        UnequipToppingRsp = ParseDict(a, prot.game.topping_pb2.UnequipToppingResponse())
        UnequipToppingRsp.additional_events.CopyFrom(MakeKAEV())
        return UnequipToppingRsp

import prot.game.cookie_pb2
import prot.game.cookie_pb2_grpc

class CookieServiceServicer(prot.game.cookie_pb2_grpc.CookieServiceServicer):
    def CreateEquipmentItem(self, request, context):
        a = {
            "upgrade_result": "SUCCESS",
            "equipment_item_type": request.equipment_item_type,
            "equipment_item": {
                "data_id": request.equipment_item_data_id,
                "level": 6,
                "upgrade_failure_count": 0,
                "is_next_level_up_success": True,
            },
            "cookie": ck_cookie.Cookie(2026766953).equipEquipment(request.equipment_item_data_id).toDictSummary(),
            "payments": [],
            "rewards": [],
            "no_guild_member_changes": {},
        }
        EquipToppingRsp = ParseDict(a, prot.game.cookie_pb2.CreateEquipmentItemResponse())
        EquipToppingRsp.additional_events.CopyFrom(MakeKAEV())
        return EquipToppingRsp

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    prot.game.routing_pb2_grpc.add_RoutingServiceServicer_to_server(RoutingServiceServicer(), server)
    prot.game.time_pb2_grpc.add_TimeServiceServicer_to_server(TimeServiceServicer(), server)
    prot.game.user_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)
    prot.game.kingdom_pb2_grpc.add_KingdomServiceServicer_to_server(KingdomServiceServicer(), server)
    prot.game.shop_pb2_grpc.add_ShopServiceServicer_to_server(ShopServiceServicer(), server)
    prot.game.mail_pb2_grpc.add_MailServiceServicer_to_server(MailServiceServicer(), server)
    prot.game.adventure_pb2_grpc.add_AdventureServiceServicer_to_server(AdventureServiceServicer(), server)
    prot.game.pvp_pb2_grpc.add_PvpServiceServicer_to_server(PvpServiceServicer(), server)
    prot.game.cutscene_pb2_grpc.add_CutsceneServiceServicer_to_server(CutsceneServiceServicer(), server)
    prot.game.episode_pb2_grpc.add_EpisodeServiceServicer_to_server(EpisodeServiceServicer(), server)
    prot.game.topping_pb2_grpc.add_ToppingServiceServicer_to_server(ToppingServiceServicer(), server)
    prot.game.town_pb2_grpc.add_TownServiceServicer_to_server(TownServiceServicer(), server)
    prot.game.cookie_pb2_grpc.add_CookieServiceServicer_to_server(CookieServiceServicer(), server)
    #server.add_insecure_port('[::]:50051')
    #server.add_insecure_port('[::]:443')
    server.add_insecure_port('[::]:50051')
    server_credentials = grpc.ssl_server_credentials(
        (
            (
                open("certs\\localhost.key", "rb").read(),
                open("certs\\localhost.cer", "rb").read(),
            ),
        )
    )
    options = {
        'grpc.ssl_target_name_override' : 'localhost',
        'grpc.default_authority': 'localhost'
    }
    server.add_secure_port('[::]:443', server_credentials)
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()