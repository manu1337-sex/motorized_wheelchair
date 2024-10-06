# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: game/episode.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'game/episode.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import prot.common_entities_pb2 as common__entities__pb2
import prot.game.entities_pb2 as game_dot_entities__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12game/episode.proto\x12\x07\x63k.game\x1a\x15\x63ommon_entities.proto\x1a\x13game/entities.proto\"0\n\x10\x43learNodeRequest\x12\x1c\n\x14\x65pisode_node_data_id\x18\x01 \x01(\x05\"\xc1\x01\n\x11\x43learNodeResponse\x12\x1d\n\x15\x65pisode_node_data_ids\x18\x01 \x03(\x05\x12;\n\x11\x61\x64\x64itional_events\x18\x02 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\"\n\x08payments\x18\x03 \x03(\x0b\x32\x10.ck.game.Payment\x12,\n\x13\x66irst_clear_rewards\x18\x04 \x03(\x0b\x32\x0f.ck.game.Reward\"\xf3\x01\n\x17\x43ompleteLandNodeRequest\x12\x16\n\x0eland_battle_id\x18\x01 \x01(\t\x12\x17\n\x0f\x61\x64venture_stars\x18\x02 \x01(\x05\x12\x30\n\rbattle_report\x18\x03 \x01(\x0b\x32\x19.ck.game.LandBattleReport\x12\x16\n\x0eis_restoration\x18\x04 \x01(\x08\x12\x1c\n\x14\x65pisode_node_data_id\x18\x05 \x01(\x05\x12\x15\n\ruser_commands\x18\x06 \x03(\x05\x12(\n is_auto_skill_enabled_when_start\x18\x07 \x01(\x08\"\xac\x06\n\x18\x43ompleteLandNodeResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12 \n\x18\x63ompleted_land_battle_id\x18\x02 \x01(\t\x12(\n\x0bland_record\x18\x03 \x01(\x0b\x32\x13.ck.game.LandRecord\x12-\n\x0cstar_rewards\x18\x04 \x03(\x0b\x32\x17.ck.game.LandStarReward\x12 \n\x07rewards\x18\x05 \x03(\x0b\x32\x0f.ck.game.Reward\x12\x37\n\x15land_play_count_value\x18\x06 \x01(\x0b\x32\x16.ck.game.LandPlayCountH\x00\x12\'\n\x12no_land_play_count\x18\x07 \x01(\x0b\x32\t.ck.EmptyH\x00\x12\x1d\n\x15\x65pisode_node_data_ids\x18\x08 \x03(\x05\x12\"\n\x08payments\x18\t \x03(\x0b\x32\x10.ck.game.Payment\x12_\n\x13\x66irst_clear_rewards\x18\x0b \x03(\x0b\x32\x42.ck.game.CompleteLandNodeResponse.EpisodeLandNodeFirstClearRewards\x12R\n#episode_land_mutation_rewards_value\x18\x0c \x01(\x0b\x32#.ck.game.EpisodeLandMutationRewardsH\x01\x12\x35\n no_episode_land_mutation_rewards\x18\r \x01(\x0b\x32\t.ck.EmptyH\x01\x1aq\n EpisodeLandNodeFirstClearRewards\x12+\n\ndifficulty\x18\x01 \x01(\x0e\x32\x17.ck.game.LandDifficulty\x12 \n\x07rewards\x18\x02 \x03(\x0b\x32\x0f.ck.game.RewardB\x11\n\x0fland_play_countB\x1f\n\x1d\x65pisode_land_mutation_rewards\"Q\n\x13SelectBranchRequest\x12\x1b\n\x13\x62ranch_node_data_id\x18\x01 \x01(\x05\x12\x1d\n\x15selected_node_data_id\x18\x02 \x01(\x05\"\x8f\x01\n\x14SelectBranchResponse\x12\x1b\n\x13\x62ranch_node_data_id\x18\x01 \x01(\x05\x12\x1d\n\x15selected_node_data_id\x18\x02 \x01(\x05\x12;\n\x11\x61\x64\x64itional_events\x18\x03 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\"Z\n(UnlockEpisodeGroupCollectionEntryRequest\x12.\n&episode_group_collection_entry_data_id\x18\x01 \x01(\x05\"\x98\x01\n)UnlockEpisodeGroupCollectionEntryResponse\x12.\n&episode_group_collection_entry_data_id\x18\x01 \x01(\x05\x12;\n\x11\x61\x64\x64itional_events\x18\x02 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\"a\n%CompleteEpisodeGroupCollectionRequest\x12\x1d\n\x15\x65pisode_group_data_id\x18\x01 \x01(\x05\x12\x19\n\x11\x63haracter_data_id\x18\x02 \x01(\x05\"\xc1\x01\n&CompleteEpisodeGroupCollectionResponse\x12\x1d\n\x15\x65pisode_group_data_id\x18\x01 \x01(\x05\x12\x19\n\x11\x63haracter_data_id\x18\x02 \x01(\x05\x12;\n\x11\x61\x64\x64itional_events\x18\x03 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12 \n\x07rewards\x18\x04 \x03(\x0b\x32\x0f.ck.game.Reward\"8\n\x17OpenEpisodeGroupRequest\x12\x1d\n\x15\x65pisode_group_data_id\x18\x01 \x01(\x05\"\xd0\x01\n\x18OpenEpisodeGroupResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\"\n\x08payments\x18\x02 \x03(\x0b\x32\x10.ck.game.Payment\x12\x1d\n\x15\x65pisode_group_data_id\x18\x03 \x01(\x05\x12\x34\n,initially_auto_cleared_episode_node_data_ids\x18\x04 \x03(\x05\"W\n&ClearStoryCollectionBookMissionRequest\x12-\n%story_collection_book_mission_data_id\x18\x01 \x01(\x05\"\xb7\x01\n\'ClearStoryCollectionBookMissionResponse\x12-\n%story_collection_book_mission_data_id\x18\x01 \x01(\x05\x12;\n\x11\x61\x64\x64itional_events\x18\x02 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12 \n\x07rewards\x18\x03 \x03(\x0b\x32\x0f.ck.game.Reward\"]\n#ReceiveAccumulatedStarRewardRequest\x12\x1d\n\x15\x65pisode_group_data_id\x18\x01 \x01(\x05\x12\x17\n\x0f\x65pisode_data_id\x18\x02 \x01(\x05\"\x83\x02\n$ReceiveAccumulatedStarRewardResponse\x12\x1d\n\x15\x65pisode_group_data_id\x18\x01 \x01(\x05\x12\x17\n\x0f\x65pisode_data_id\x18\x02 \x01(\x05\x12;\n\x11\x61\x64\x64itional_events\x18\x03 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12 \n\x07rewards\x18\x04 \x03(\x0b\x32\x0f.ck.game.Reward\x12\x44\n\x1a\x65pisode_star_reward_record\x18\x05 \x01(\x0b\x32 .ck.game.EpisodeStarRewardRecord\"6\n\x1eRestoreEpisodeStructureRequest\x12\x14\n\x0cnode_data_id\x18\x01 \x01(\x05\"\x8a\x02\n\x1fRestoreEpisodeStructureResponse\x12\"\n\x08payments\x18\x01 \x03(\x0b\x32\x10.ck.game.Payment\x12!\n\rends_at_value\x18\x02 \x01(\x0b\x32\x08.ck.TimeH\x00\x12\x1f\n\nno_ends_at\x18\x03 \x01(\x0b\x32\t.ck.EmptyH\x00\x12\x15\n\rnode_data_ids\x18\x04 \x03(\x05\x12 \n\x07rewards\x18\x05 \x03(\x0b\x32\x0f.ck.game.Reward\x12;\n\x11\x61\x64\x64itional_events\x18\x06 \x01(\x0b\x32 .ck.game.KingdomAdditionalEventsB\t\n\x07\x65nds_at\"\xf3\x02\n,AccelerateEpisodeStructureRestorationRequest\x12\x14\n\x0cnode_data_id\x18\x01 \x01(\x05\x12i\n\x13time_reducer_spends\x18\x02 \x03(\x0b\x32L.ck.game.AccelerateEpisodeStructureRestorationRequest.TimeReducerSpendsEntry\x12\x42\n\x1aviewed_advertisement_value\x18\x04 \x01(\x0b\x32\x1c.ck.game.ViewedAdvertisementH\x00\x12,\n\x17no_viewed_advertisement\x18\x05 \x01(\x0b\x32\t.ck.EmptyH\x00\x1a\x38\n\x16TimeReducerSpendsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x42\x16\n\x14viewed_advertisement\"\xff\x01\n-AccelerateEpisodeStructureRestorationResponse\x12\x14\n\x0cnode_data_id\x18\x01 \x01(\x05\x12\"\n\x08payments\x18\x02 \x03(\x0b\x32\x10.ck.game.Payment\x12\x1d\n\x0bnew_ends_at\x18\x03 \x01(\x0b\x32\x08.ck.Time\x12\x38\n\x13\x61\x64vertisement_state\x18\x04 \x01(\x0b\x32\x1b.ck.game.AdvertisementState\x12;\n\x11\x61\x64\x64itional_events\x18\x05 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\"\x8e\x01\n1InstantCompleteEpisodeStructureRestorationRequest\x12\x14\n\x0cnode_data_id\x18\x01 \x01(\x05\x12\x43\n\x19instant_completion_method\x18\x02 \x01(\x0b\x32 .ck.game.InstantCompletionMethod\"\x88\x02\n2InstantCompleteEpisodeStructureRestorationResponse\x12\x15\n\rnode_data_ids\x18\x01 \x03(\x05\x12\"\n\x08payments\x18\x02 \x03(\x0b\x32\x10.ck.game.Payment\x12 \n\x07rewards\x18\x03 \x03(\x0b\x32\x0f.ck.game.Reward\x12\x38\n\x13\x61\x64vertisement_state\x18\x04 \x01(\x0b\x32\x1b.ck.game.AdvertisementState\x12;\n\x11\x61\x64\x64itional_events\x18\x05 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\"\"\n UpdateEpisodeLandMutationRequest\"\x9d\x01\n!UpdateEpisodeLandMutationResponse\x12;\n\x15\x65pisode_land_mutation\x18\x01 \x01(\x0b\x32\x1c.ck.game.EpisodeLandMutation\x12;\n\x11\x61\x64\x64itional_events\x18\x02 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents2\xdc\x07\n\x0e\x45pisodeService\x12\x42\n\tClearNode\x12\x19.ck.game.ClearNodeRequest\x1a\x1a.ck.game.ClearNodeResponse\x12K\n\x0cSelectBranch\x12\x1c.ck.game.SelectBranchRequest\x1a\x1d.ck.game.SelectBranchResponse\x12W\n\x10\x43ompleteLandNode\x12 .ck.game.CompleteLandNodeRequest\x1a!.ck.game.CompleteLandNodeResponse\x12{\n\x1cReceiveAccumulatedStarReward\x12,.ck.game.ReceiveAccumulatedStarRewardRequest\x1a-.ck.game.ReceiveAccumulatedStarRewardResponse\x12\x8a\x01\n!UnlockEpisodeGroupCollectionEntry\x12\x31.ck.game.UnlockEpisodeGroupCollectionEntryRequest\x1a\x32.ck.game.UnlockEpisodeGroupCollectionEntryResponse\x12\x81\x01\n\x1e\x43ompleteEpisodeGroupCollection\x12..ck.game.CompleteEpisodeGroupCollectionRequest\x1a/.ck.game.CompleteEpisodeGroupCollectionResponse\x12\x84\x01\n\x1f\x43learStoryCollectionBookMission\x12/.ck.game.ClearStoryCollectionBookMissionRequest\x1a\x30.ck.game.ClearStoryCollectionBookMissionResponse\x12W\n\x10OpenEpisodeGroup\x12 .ck.game.OpenEpisodeGroupRequest\x1a!.ck.game.OpenEpisodeGroupResponse\x12r\n\x19UpdateEpisodeLandMutation\x12).ck.game.UpdateEpisodeLandMutationRequest\x1a*.ck.game.UpdateEpisodeLandMutationResponseBC\n(com.devsisters.ck.services.game.protobuf\xaa\x02\x16Services.Game.Protobufb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'game.episode_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(com.devsisters.ck.services.game.protobuf\252\002\026Services.Game.Protobuf'
  _globals['_ACCELERATEEPISODESTRUCTURERESTORATIONREQUEST_TIMEREDUCERSPENDSENTRY']._loaded_options = None
  _globals['_ACCELERATEEPISODESTRUCTURERESTORATIONREQUEST_TIMEREDUCERSPENDSENTRY']._serialized_options = b'8\001'
  _globals['_CLEARNODEREQUEST']._serialized_start=75
  _globals['_CLEARNODEREQUEST']._serialized_end=123
  _globals['_CLEARNODERESPONSE']._serialized_start=126
  _globals['_CLEARNODERESPONSE']._serialized_end=319
  _globals['_COMPLETELANDNODEREQUEST']._serialized_start=322
  _globals['_COMPLETELANDNODEREQUEST']._serialized_end=565
  _globals['_COMPLETELANDNODERESPONSE']._serialized_start=568
  _globals['_COMPLETELANDNODERESPONSE']._serialized_end=1380
  _globals['_COMPLETELANDNODERESPONSE_EPISODELANDNODEFIRSTCLEARREWARDS']._serialized_start=1215
  _globals['_COMPLETELANDNODERESPONSE_EPISODELANDNODEFIRSTCLEARREWARDS']._serialized_end=1328
  _globals['_SELECTBRANCHREQUEST']._serialized_start=1382
  _globals['_SELECTBRANCHREQUEST']._serialized_end=1463
  _globals['_SELECTBRANCHRESPONSE']._serialized_start=1466
  _globals['_SELECTBRANCHRESPONSE']._serialized_end=1609
  _globals['_UNLOCKEPISODEGROUPCOLLECTIONENTRYREQUEST']._serialized_start=1611
  _globals['_UNLOCKEPISODEGROUPCOLLECTIONENTRYREQUEST']._serialized_end=1701
  _globals['_UNLOCKEPISODEGROUPCOLLECTIONENTRYRESPONSE']._serialized_start=1704
  _globals['_UNLOCKEPISODEGROUPCOLLECTIONENTRYRESPONSE']._serialized_end=1856
  _globals['_COMPLETEEPISODEGROUPCOLLECTIONREQUEST']._serialized_start=1858
  _globals['_COMPLETEEPISODEGROUPCOLLECTIONREQUEST']._serialized_end=1955
  _globals['_COMPLETEEPISODEGROUPCOLLECTIONRESPONSE']._serialized_start=1958
  _globals['_COMPLETEEPISODEGROUPCOLLECTIONRESPONSE']._serialized_end=2151
  _globals['_OPENEPISODEGROUPREQUEST']._serialized_start=2153
  _globals['_OPENEPISODEGROUPREQUEST']._serialized_end=2209
  _globals['_OPENEPISODEGROUPRESPONSE']._serialized_start=2212
  _globals['_OPENEPISODEGROUPRESPONSE']._serialized_end=2420
  _globals['_CLEARSTORYCOLLECTIONBOOKMISSIONREQUEST']._serialized_start=2422
  _globals['_CLEARSTORYCOLLECTIONBOOKMISSIONREQUEST']._serialized_end=2509
  _globals['_CLEARSTORYCOLLECTIONBOOKMISSIONRESPONSE']._serialized_start=2512
  _globals['_CLEARSTORYCOLLECTIONBOOKMISSIONRESPONSE']._serialized_end=2695
  _globals['_RECEIVEACCUMULATEDSTARREWARDREQUEST']._serialized_start=2697
  _globals['_RECEIVEACCUMULATEDSTARREWARDREQUEST']._serialized_end=2790
  _globals['_RECEIVEACCUMULATEDSTARREWARDRESPONSE']._serialized_start=2793
  _globals['_RECEIVEACCUMULATEDSTARREWARDRESPONSE']._serialized_end=3052
  _globals['_RESTOREEPISODESTRUCTUREREQUEST']._serialized_start=3054
  _globals['_RESTOREEPISODESTRUCTUREREQUEST']._serialized_end=3108
  _globals['_RESTOREEPISODESTRUCTURERESPONSE']._serialized_start=3111
  _globals['_RESTOREEPISODESTRUCTURERESPONSE']._serialized_end=3377
  _globals['_ACCELERATEEPISODESTRUCTURERESTORATIONREQUEST']._serialized_start=3380
  _globals['_ACCELERATEEPISODESTRUCTURERESTORATIONREQUEST']._serialized_end=3751
  _globals['_ACCELERATEEPISODESTRUCTURERESTORATIONREQUEST_TIMEREDUCERSPENDSENTRY']._serialized_start=3671
  _globals['_ACCELERATEEPISODESTRUCTURERESTORATIONREQUEST_TIMEREDUCERSPENDSENTRY']._serialized_end=3727
  _globals['_ACCELERATEEPISODESTRUCTURERESTORATIONRESPONSE']._serialized_start=3754
  _globals['_ACCELERATEEPISODESTRUCTURERESTORATIONRESPONSE']._serialized_end=4009
  _globals['_INSTANTCOMPLETEEPISODESTRUCTURERESTORATIONREQUEST']._serialized_start=4012
  _globals['_INSTANTCOMPLETEEPISODESTRUCTURERESTORATIONREQUEST']._serialized_end=4154
  _globals['_INSTANTCOMPLETEEPISODESTRUCTURERESTORATIONRESPONSE']._serialized_start=4157
  _globals['_INSTANTCOMPLETEEPISODESTRUCTURERESTORATIONRESPONSE']._serialized_end=4421
  _globals['_UPDATEEPISODELANDMUTATIONREQUEST']._serialized_start=4423
  _globals['_UPDATEEPISODELANDMUTATIONREQUEST']._serialized_end=4457
  _globals['_UPDATEEPISODELANDMUTATIONRESPONSE']._serialized_start=4460
  _globals['_UPDATEEPISODELANDMUTATIONRESPONSE']._serialized_end=4617
  _globals['_EPISODESERVICE']._serialized_start=4620
  _globals['_EPISODESERVICE']._serialized_end=5608
# @@protoc_insertion_point(module_scope)
