# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: game/town.proto
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
    'game/town.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import prot.common_entities_pb2 as common__entities__pb2
import prot.game.entities_pb2 as game_dot_entities__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fgame/town.proto\x12\x07\x63k.game\x1a\x15\x63ommon_entities.proto\x1a\x13game/entities.proto\"2\n\x1a\x41pproveConstructionRequest\x12\x14\n\x0cstructure_id\x18\x01 \x01(\t\"\xa3\x01\n\x1b\x41pproveConstructionResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12%\n\tstructure\x18\x02 \x01(\x0b\x32\x12.ck.game.Structure\x12 \n\x07rewards\x18\x04 \x03(\x0b\x32\x0f.ck.game.Reward\"\x7f\n\"InstantCompleteConstructionRequest\x12\x14\n\x0cstructure_id\x18\x01 \x01(\t\x12\x43\n\x19instant_completion_method\x18\x02 \x01(\x0b\x32 .ck.game.InstantCompletionMethod\"\x89\x02\n#InstantCompleteConstructionResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12%\n\tstructure\x18\x02 \x01(\x0b\x32\x12.ck.game.Structure\x12\"\n\x08payments\x18\x04 \x03(\x0b\x32\x10.ck.game.Payment\x12 \n\x07rewards\x18\x05 \x03(\x0b\x32\x0f.ck.game.Reward\x12\x38\n\x13\x61\x64vertisement_state\x18\x06 \x01(\x0b\x32\x1b.ck.game.AdvertisementState\"\xd5\x02\n\x1d\x41\x63\x63\x65lerateConstructionRequest\x12\x14\n\x0cstructure_id\x18\x01 \x01(\t\x12Z\n\x13time_reducer_spends\x18\x02 \x03(\x0b\x32=.ck.game.AccelerateConstructionRequest.TimeReducerSpendsEntry\x12\x42\n\x1aviewed_advertisement_value\x18\x04 \x01(\x0b\x32\x1c.ck.game.ViewedAdvertisementH\x00\x12,\n\x17no_viewed_advertisement\x18\x05 \x01(\x0b\x32\t.ck.EmptyH\x00\x1a\x38\n\x16TimeReducerSpendsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x42\x16\n\x14viewed_advertisement\"\xee\x01\n\x1e\x41\x63\x63\x65lerateConstructionResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x31\n\x15\x61\x63\x63\x65lerated_structure\x18\x02 \x01(\x0b\x32\x12.ck.game.Structure\x12\"\n\x08payments\x18\x03 \x03(\x0b\x32\x10.ck.game.Payment\x12\x38\n\x13\x61\x64vertisement_state\x18\x04 \x01(\x0b\x32\x1b.ck.game.AdvertisementState\"/\n\x17\x45xpandCraftQueueRequest\x12\x14\n\x0cstructure_id\x18\x01 \x01(\t\"\xa2\x01\n\x18\x45xpandCraftQueueResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\"\n\x08payments\x18\x02 \x03(\x0b\x32\x10.ck.game.Payment\x12%\n\tstructure\x18\x03 \x01(\x0b\x32\x12.ck.game.Structure\"A\n\x17LevelUpStructureRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1a\n\x12use_event_material\x18\x02 \x01(\x08\"\xcc\x01\n\x18LevelUpStructureResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12-\n\x11updated_structure\x18\x02 \x01(\x0b\x32\x12.ck.game.Structure\x12\"\n\x08payments\x18\x04 \x03(\x0b\x32\x10.ck.game.Payment\x12 \n\x07rewards\x18\x05 \x03(\x0b\x32\x0f.ck.game.Reward\":\n\"SupplyConstructionMaterialsRequest\x12\x14\n\x0cstructure_id\x18\x01 \x01(\t\"\xcf\x01\n#SupplyConstructionMaterialsResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12%\n\tstructure\x18\x02 \x01(\x0b\x32\x12.ck.game.Structure\x12\"\n\x08payments\x18\x03 \x03(\x0b\x32\x10.ck.game.Payment\x12 \n\x07rewards\x18\x04 \x03(\x0b\x32\x0f.ck.game.Reward\"0\n\x18\x44\x65molishStructureRequest\x12\x14\n\x0cstructure_id\x18\x01 \x01(\t\"\x97\x01\n\x19\x44\x65molishStructureResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x14\n\x0cstructure_id\x18\x02 \x01(\t\x12\'\n\x0erefund_rewards\x18\x03 \x03(\x0b\x32\x0f.ck.game.Reward\"9\n\x0f\x45\x64itTownRequest\x12&\n\x08\x63ommands\x18\x01 \x03(\x0b\x32\x14.ck.game.EditCommand\"\xd7\x02\n\x10\x45\x64itTownResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12)\n\x0ctown_changes\x18\x02 \x03(\x0b\x32\x13.ck.game.TownChange\x12\"\n\x08payments\x18\x03 \x03(\x0b\x32\x10.ck.game.Payment\x12 \n\x07rewards\x18\x04 \x03(\x0b\x32\x0f.ck.game.Reward\x12W\n\x19structure_ids_by_dummy_id\x18\x05 \x03(\x0b\x32\x34.ck.game.EditTownResponse.StructureIdsByDummyIdEntry\x1a<\n\x1aStructureIdsByDummyIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"8\n\x1dStartTownSegmentUnlockRequest\x12\x17\n\x0fsegment_data_id\x18\x01 \x01(\x05\"\xc6\x01\n\x1eStartTownSegmentUnlockResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x43\n\x17segment_unlock_progress\x18\x02 \x01(\x0b\x32\".ck.game.TownSegmentUnlockProgress\x12\"\n\x08payments\x18\x03 \x03(\x0b\x32\x10.ck.game.Payment\"9\n\x1e\x46inishTownSegmentUnlockRequest\x12\x17\n\x0fsegment_data_id\x18\x01 \x01(\x05\"\xb0\x01\n\x1f\x46inishTownSegmentUnlockResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12.\n\x10unlocked_segment\x18\x02 \x01(\x0b\x32\x14.ck.game.TownSegment\x12 \n\x07rewards\x18\x03 \x03(\x0b\x32\x0f.ck.game.Reward\"\x87\x01\n\'InstantCompleteTownSegmentUnlockRequest\x12\x17\n\x0fsegment_data_id\x18\x01 \x01(\x05\x12\x43\n\x19instant_completion_method\x18\x02 \x01(\x0b\x32 .ck.game.InstantCompletionMethod\"\x97\x02\n(InstantCompleteTownSegmentUnlockResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12.\n\x10unlocked_segment\x18\x02 \x01(\x0b\x32\x14.ck.game.TownSegment\x12\"\n\x08payments\x18\x03 \x03(\x0b\x32\x10.ck.game.Payment\x12 \n\x07rewards\x18\x04 \x03(\x0b\x32\x0f.ck.game.Reward\x12\x38\n\x13\x61\x64vertisement_state\x18\x05 \x01(\x0b\x32\x1b.ck.game.AdvertisementState\"\xe2\x02\n\"AccelerateTownSegmentUnlockRequest\x12\x17\n\x0fsegment_data_id\x18\x01 \x01(\x05\x12_\n\x13time_reducer_spends\x18\x02 \x03(\x0b\x32\x42.ck.game.AccelerateTownSegmentUnlockRequest.TimeReducerSpendsEntry\x12\x42\n\x1aviewed_advertisement_value\x18\x04 \x01(\x0b\x32\x1c.ck.game.ViewedAdvertisementH\x00\x12,\n\x17no_viewed_advertisement\x18\x05 \x01(\x0b\x32\t.ck.EmptyH\x00\x1a\x38\n\x16TimeReducerSpendsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x42\x16\n\x14viewed_advertisement\"\x85\x02\n#AccelerateTownSegmentUnlockResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x43\n\x17segment_unlock_progress\x18\x02 \x01(\x0b\x32\".ck.game.TownSegmentUnlockProgress\x12\"\n\x08payments\x18\x03 \x03(\x0b\x32\x10.ck.game.Payment\x12\x38\n\x13\x61\x64vertisement_state\x18\x04 \x01(\x0b\x32\x1b.ck.game.AdvertisementState\"9\n\x1eUnlockBattleTownSegmentRequest\x12\x17\n\x0fsegment_data_id\x18\x01 \x01(\x05\"\xb0\x01\n\x1fUnlockBattleTownSegmentResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12.\n\x10unlocked_segment\x18\x02 \x01(\x0b\x32\x14.ck.game.TownSegment\x12 \n\x07rewards\x18\x03 \x03(\x0b\x32\x0f.ck.game.Reward\"F\n-ReceiveCumulativeAutoProductionsRewardRequest\x12\x15\n\rstructure_ids\x18\x01 \x03(\t\"\xbd\x03\n.ReceiveCumulativeAutoProductionsRewardResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12)\n\x0ctown_changes\x18\x02 \x03(\x0b\x32\x13.ck.game.TownChange\x12r\n\x17rewards_by_structure_id\x18\x03 \x03(\x0b\x32Q.ck.game.ReceiveCumulativeAutoProductionsRewardResponse.RewardsByStructureIdEntry\x1a\x7f\n\x19RewardsByStructureIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12Q\n\x05value\x18\x02 \x01(\x0b\x32\x42.ck.game.ReceiveCumulativeAutoProductionsRewardResponse.RewardList:\x02\x38\x01\x1a.\n\nRewardList\x12 \n\x07rewards\x18\x03 \x03(\x0b\x32\x0f.ck.game.Reward\">\n&RefreshFountainProductionRewardRequest\x12\x14\n\x0cstructure_id\x18\x01 \x01(\t\"\xb6\x01\n\'RefreshFountainProductionRewardResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x14\n\x0cstructure_id\x18\x02 \x01(\t\x12\x38\n\x13\x66ountain_production\x18\x03 \x01(\x0b\x32\x1b.ck.game.FountainProduction\">\n&ReceiveFountainProductionRewardRequest\x12\x14\n\x0cstructure_id\x18\x01 \x01(\t\"\xd8\x01\n\'ReceiveFountainProductionRewardResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x14\n\x0cstructure_id\x18\x02 \x01(\t\x12\x38\n\x13\x66ountain_production\x18\x03 \x01(\x0b\x32\x1b.ck.game.FountainProduction\x12 \n\x07rewards\x18\x04 \x03(\x0b\x32\x0f.ck.game.Reward\">\n&ReceiveLandmarkProductionRewardRequest\x12\x14\n\x0cstructure_id\x18\x01 \x01(\t\"\xc9\x01\n\'ReceiveLandmarkProductionRewardResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x14\n\x0cstructure_id\x18\x02 \x01(\t\x12)\n\x0ctown_changes\x18\x03 \x03(\x0b\x32\x13.ck.game.TownChange\x12 \n\x07rewards\x18\x04 \x03(\x0b\x32\x0f.ck.game.Reward\"O\n&ChangeAutoProductionCanActivateRequest\x12\x14\n\x0cstructure_id\x18\x01 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\"\xae\x01\n\'ChangeAutoProductionCanActivateResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x14\n\x0cstructure_id\x18\x02 \x01(\t\x12\x30\n\x0f\x61uto_production\x18\x03 \x01(\x0b\x32\x17.ck.game.AutoProduction\"\\\n\x15SaveTownPresetRequest\x12\x13\n\x0bpreset_slot\x18\x01 \x01(\x05\x12\x13\n\x0bpreset_name\x18\x02 \x01(\t\x12\x19\n\x11screenshot_binary\x18\x03 \x01(\x0c\"\x99\x01\n\x16SaveTownPresetResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12*\n\npreset_ref\x18\x02 \x01(\x0b\x32\x16.ck.game.TownPresetRef\x12\x16\n\x0escreenshot_url\x18\x03 \x01(\t\"*\n\x15LoadTownPresetRequest\x12\x11\n\tpreset_id\x18\x01 \x01(\t\"\xfe\x01\n\x16LoadTownPresetResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12.\n\x0etown_placement\x18\x02 \x01(\x0b\x32\x16.ck.game.TownPlacement\x12)\n\x0ctown_changes\x18\x05 \x03(\x0b\x32\x13.ck.game.TownChange\x12 \n\x07rewards\x18\x03 \x03(\x0b\x32\x0f.ck.game.Reward\x12*\n\npreset_ref\x18\x04 \x01(\x0b\x32\x16.ck.game.TownPresetRef\"E\n\x17RenameTownPresetRequest\x12\x11\n\tpreset_id\x18\x01 \x01(\t\x12\x17\n\x0fnew_preset_name\x18\x02 \x01(\t\"\x9a\x01\n\x18RenameTownPresetResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x11\n\tpreset_id\x18\x02 \x01(\t\x12.\n\x0enew_preset_ref\x18\x03 \x01(\x0b\x32\x16.ck.game.TownPresetRef\",\n\x17\x44\x65leteTownPresetRequest\x12\x11\n\tpreset_id\x18\x01 \x01(\t\"j\n\x18\x44\x65leteTownPresetResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x11\n\tpreset_id\x18\x02 \x01(\t\"`\n\x10\x43learTownRequest\x12\x16\n\x0ekeep_landmarks\x18\x01 \x01(\x08\x12\x18\n\x10keep_productions\x18\x02 \x01(\x08\x12\x1a\n\x12keep_cookie_houses\x18\x03 \x01(\x08\"\xcd\x01\n\x11\x43learTownResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12.\n\x0etown_placement\x18\x02 \x01(\x0b\x32\x16.ck.game.TownPlacement\x12)\n\x0ctown_changes\x18\x04 \x03(\x0b\x32\x13.ck.game.TownChange\x12 \n\x07rewards\x18\x03 \x03(\x0b\x32\x0f.ck.game.Reward\"!\n\x1fUpgradeTownPresetStorageRequest\"\xa6\x01\n UpgradeTownPresetStorageResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12!\n\x19town_preset_storage_level\x18\x02 \x01(\x05\x12\"\n\x08payments\x18\x03 \x03(\x0b\x32\x10.ck.game.Payment\"N\n\x1dSetStructureBookmarkedRequest\x12\x19\n\x11structure_data_id\x18\x01 \x01(\x05\x12\x12\n\nbookmarked\x18\x02 \x01(\x08\"\x8c\x01\n\x1eSetStructureBookmarkedResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x19\n\x11structure_data_id\x18\x02 \x01(\x05\x12\x12\n\nbookmarked\x18\x03 \x01(\x08\"E\n\x1cSetHouseIdsBookmarkedRequest\x12\x11\n\thouse_ids\x18\x01 \x03(\t\x12\x12\n\nbookmarked\x18\x02 \x01(\x08\"\x83\x01\n\x1dSetHouseIdsBookmarkedResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x11\n\thouse_ids\x18\x02 \x03(\t\x12\x12\n\nbookmarked\x18\x03 \x01(\x08\"6\n\x1cUnlockSkyGardenIslandRequest\x12\x16\n\x0eisland_data_id\x18\x01 \x01(\x05\"\x98\x01\n\x1dUnlockSkyGardenIslandResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x16\n\x0eisland_data_id\x18\x02 \x01(\x05\x12\"\n\x08payments\x18\x03 \x03(\x0b\x32\x10.ck.game.Payment\")\n\x14GetTownPresetRequest\x12\x11\n\tpreset_id\x18\x01 \x01(\t\"\x92\x02\n\x15GetTownPresetResponse\x12(\n\x0btown_preset\x18\x01 \x01(\x0b\x32\x13.ck.game.TownPreset\x12+\n\rowner_summary\x18\x02 \x01(\x0b\x32\x14.ck.game.UserSummary\x12\x34\n\x13guild_summary_value\x18\x03 \x01(\x0b\x32\x15.ck.game.GuildSummaryH\x00\x12%\n\x10no_guild_summary\x18\x04 \x01(\x0b\x32\t.ck.EmptyH\x00\x12\x34\n\x16selected_profile_decos\x18\x05 \x03(\x0b\x32\x14.ck.game.ProfileDecoB\x0f\n\rguild_summary2\xb8\x17\n\x0bTownService\x12`\n\x13\x41pproveConstruction\x12#.ck.game.ApproveConstructionRequest\x1a$.ck.game.ApproveConstructionResponse\x12x\n\x1bInstantCompleteConstruction\x12+.ck.game.InstantCompleteConstructionRequest\x1a,.ck.game.InstantCompleteConstructionResponse\x12i\n\x16\x41\x63\x63\x65lerateConstruction\x12&.ck.game.AccelerateConstructionRequest\x1a\'.ck.game.AccelerateConstructionResponse\x12W\n\x10\x45xpandCraftQueue\x12 .ck.game.ExpandCraftQueueRequest\x1a!.ck.game.ExpandCraftQueueResponse\x12W\n\x10LevelUpStructure\x12 .ck.game.LevelUpStructureRequest\x1a!.ck.game.LevelUpStructureResponse\x12x\n\x1bSupplyConstructionMaterials\x12+.ck.game.SupplyConstructionMaterialsRequest\x1a,.ck.game.SupplyConstructionMaterialsResponse\x12Z\n\x11\x44\x65molishStructure\x12!.ck.game.DemolishStructureRequest\x1a\".ck.game.DemolishStructureResponse\x12?\n\x08\x45\x64itTown\x12\x18.ck.game.EditTownRequest\x1a\x19.ck.game.EditTownResponse\x12i\n\x16StartTownSegmentUnlock\x12&.ck.game.StartTownSegmentUnlockRequest\x1a\'.ck.game.StartTownSegmentUnlockResponse\x12l\n\x17\x46inishTownSegmentUnlock\x12\'.ck.game.FinishTownSegmentUnlockRequest\x1a(.ck.game.FinishTownSegmentUnlockResponse\x12\x87\x01\n InstantCompleteTownSegmentUnlock\x12\x30.ck.game.InstantCompleteTownSegmentUnlockRequest\x1a\x31.ck.game.InstantCompleteTownSegmentUnlockResponse\x12x\n\x1b\x41\x63\x63\x65lerateTownSegmentUnlock\x12+.ck.game.AccelerateTownSegmentUnlockRequest\x1a,.ck.game.AccelerateTownSegmentUnlockResponse\x12l\n\x17UnlockBattleTownSegment\x12\'.ck.game.UnlockBattleTownSegmentRequest\x1a(.ck.game.UnlockBattleTownSegmentResponse\x12\x99\x01\n&ReceiveCumulativeAutoProductionsReward\x12\x36.ck.game.ReceiveCumulativeAutoProductionsRewardRequest\x1a\x37.ck.game.ReceiveCumulativeAutoProductionsRewardResponse\x12\x84\x01\n\x1fRefreshFountainProductionReward\x12/.ck.game.RefreshFountainProductionRewardRequest\x1a\x30.ck.game.RefreshFountainProductionRewardResponse\x12\x84\x01\n\x1fReceiveFountainProductionReward\x12/.ck.game.ReceiveFountainProductionRewardRequest\x1a\x30.ck.game.ReceiveFountainProductionRewardResponse\x12\x84\x01\n\x1fReceiveLandmarkProductionReward\x12/.ck.game.ReceiveLandmarkProductionRewardRequest\x1a\x30.ck.game.ReceiveLandmarkProductionRewardResponse\x12\x84\x01\n\x1f\x43hangeAutoProductionCanActivate\x12/.ck.game.ChangeAutoProductionCanActivateRequest\x1a\x30.ck.game.ChangeAutoProductionCanActivateResponse\x12Q\n\x0eSaveTownPreset\x12\x1e.ck.game.SaveTownPresetRequest\x1a\x1f.ck.game.SaveTownPresetResponse\x12Q\n\x0eLoadTownPreset\x12\x1e.ck.game.LoadTownPresetRequest\x1a\x1f.ck.game.LoadTownPresetResponse\x12W\n\x10RenameTownPreset\x12 .ck.game.RenameTownPresetRequest\x1a!.ck.game.RenameTownPresetResponse\x12W\n\x10\x44\x65leteTownPreset\x12 .ck.game.DeleteTownPresetRequest\x1a!.ck.game.DeleteTownPresetResponse\x12\x42\n\tClearTown\x12\x19.ck.game.ClearTownRequest\x1a\x1a.ck.game.ClearTownResponse\x12o\n\x18UpgradeTownPresetStorage\x12(.ck.game.UpgradeTownPresetStorageRequest\x1a).ck.game.UpgradeTownPresetStorageResponse\x12i\n\x16SetStructureBookmarked\x12&.ck.game.SetStructureBookmarkedRequest\x1a\'.ck.game.SetStructureBookmarkedResponse\x12\x66\n\x15SetHouseIdsBookmarked\x12%.ck.game.SetHouseIdsBookmarkedRequest\x1a&.ck.game.SetHouseIdsBookmarkedResponse\x12\x66\n\x15UnlockSkyGardenIsland\x12%.ck.game.UnlockSkyGardenIslandRequest\x1a&.ck.game.UnlockSkyGardenIslandResponse\x12N\n\rGetTownPreset\x12\x1d.ck.game.GetTownPresetRequest\x1a\x1e.ck.game.GetTownPresetResponseBC\n(com.devsisters.ck.services.game.protobuf\xaa\x02\x16Services.Game.Protobufb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'game.town_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(com.devsisters.ck.services.game.protobuf\252\002\026Services.Game.Protobuf'
  _globals['_ACCELERATECONSTRUCTIONREQUEST_TIMEREDUCERSPENDSENTRY']._loaded_options = None
  _globals['_ACCELERATECONSTRUCTIONREQUEST_TIMEREDUCERSPENDSENTRY']._serialized_options = b'8\001'
  _globals['_EDITTOWNRESPONSE_STRUCTUREIDSBYDUMMYIDENTRY']._loaded_options = None
  _globals['_EDITTOWNRESPONSE_STRUCTUREIDSBYDUMMYIDENTRY']._serialized_options = b'8\001'
  _globals['_ACCELERATETOWNSEGMENTUNLOCKREQUEST_TIMEREDUCERSPENDSENTRY']._loaded_options = None
  _globals['_ACCELERATETOWNSEGMENTUNLOCKREQUEST_TIMEREDUCERSPENDSENTRY']._serialized_options = b'8\001'
  _globals['_RECEIVECUMULATIVEAUTOPRODUCTIONSREWARDRESPONSE_REWARDSBYSTRUCTUREIDENTRY']._loaded_options = None
  _globals['_RECEIVECUMULATIVEAUTOPRODUCTIONSREWARDRESPONSE_REWARDSBYSTRUCTUREIDENTRY']._serialized_options = b'8\001'
  _globals['_APPROVECONSTRUCTIONREQUEST']._serialized_start=72
  _globals['_APPROVECONSTRUCTIONREQUEST']._serialized_end=122
  _globals['_APPROVECONSTRUCTIONRESPONSE']._serialized_start=125
  _globals['_APPROVECONSTRUCTIONRESPONSE']._serialized_end=288
  _globals['_INSTANTCOMPLETECONSTRUCTIONREQUEST']._serialized_start=290
  _globals['_INSTANTCOMPLETECONSTRUCTIONREQUEST']._serialized_end=417
  _globals['_INSTANTCOMPLETECONSTRUCTIONRESPONSE']._serialized_start=420
  _globals['_INSTANTCOMPLETECONSTRUCTIONRESPONSE']._serialized_end=685
  _globals['_ACCELERATECONSTRUCTIONREQUEST']._serialized_start=688
  _globals['_ACCELERATECONSTRUCTIONREQUEST']._serialized_end=1029
  _globals['_ACCELERATECONSTRUCTIONREQUEST_TIMEREDUCERSPENDSENTRY']._serialized_start=949
  _globals['_ACCELERATECONSTRUCTIONREQUEST_TIMEREDUCERSPENDSENTRY']._serialized_end=1005
  _globals['_ACCELERATECONSTRUCTIONRESPONSE']._serialized_start=1032
  _globals['_ACCELERATECONSTRUCTIONRESPONSE']._serialized_end=1270
  _globals['_EXPANDCRAFTQUEUEREQUEST']._serialized_start=1272
  _globals['_EXPANDCRAFTQUEUEREQUEST']._serialized_end=1319
  _globals['_EXPANDCRAFTQUEUERESPONSE']._serialized_start=1322
  _globals['_EXPANDCRAFTQUEUERESPONSE']._serialized_end=1484
  _globals['_LEVELUPSTRUCTUREREQUEST']._serialized_start=1486
  _globals['_LEVELUPSTRUCTUREREQUEST']._serialized_end=1551
  _globals['_LEVELUPSTRUCTURERESPONSE']._serialized_start=1554
  _globals['_LEVELUPSTRUCTURERESPONSE']._serialized_end=1758
  _globals['_SUPPLYCONSTRUCTIONMATERIALSREQUEST']._serialized_start=1760
  _globals['_SUPPLYCONSTRUCTIONMATERIALSREQUEST']._serialized_end=1818
  _globals['_SUPPLYCONSTRUCTIONMATERIALSRESPONSE']._serialized_start=1821
  _globals['_SUPPLYCONSTRUCTIONMATERIALSRESPONSE']._serialized_end=2028
  _globals['_DEMOLISHSTRUCTUREREQUEST']._serialized_start=2030
  _globals['_DEMOLISHSTRUCTUREREQUEST']._serialized_end=2078
  _globals['_DEMOLISHSTRUCTURERESPONSE']._serialized_start=2081
  _globals['_DEMOLISHSTRUCTURERESPONSE']._serialized_end=2232
  _globals['_EDITTOWNREQUEST']._serialized_start=2234
  _globals['_EDITTOWNREQUEST']._serialized_end=2291
  _globals['_EDITTOWNRESPONSE']._serialized_start=2294
  _globals['_EDITTOWNRESPONSE']._serialized_end=2637
  _globals['_EDITTOWNRESPONSE_STRUCTUREIDSBYDUMMYIDENTRY']._serialized_start=2577
  _globals['_EDITTOWNRESPONSE_STRUCTUREIDSBYDUMMYIDENTRY']._serialized_end=2637
  _globals['_STARTTOWNSEGMENTUNLOCKREQUEST']._serialized_start=2639
  _globals['_STARTTOWNSEGMENTUNLOCKREQUEST']._serialized_end=2695
  _globals['_STARTTOWNSEGMENTUNLOCKRESPONSE']._serialized_start=2698
  _globals['_STARTTOWNSEGMENTUNLOCKRESPONSE']._serialized_end=2896
  _globals['_FINISHTOWNSEGMENTUNLOCKREQUEST']._serialized_start=2898
  _globals['_FINISHTOWNSEGMENTUNLOCKREQUEST']._serialized_end=2955
  _globals['_FINISHTOWNSEGMENTUNLOCKRESPONSE']._serialized_start=2958
  _globals['_FINISHTOWNSEGMENTUNLOCKRESPONSE']._serialized_end=3134
  _globals['_INSTANTCOMPLETETOWNSEGMENTUNLOCKREQUEST']._serialized_start=3137
  _globals['_INSTANTCOMPLETETOWNSEGMENTUNLOCKREQUEST']._serialized_end=3272
  _globals['_INSTANTCOMPLETETOWNSEGMENTUNLOCKRESPONSE']._serialized_start=3275
  _globals['_INSTANTCOMPLETETOWNSEGMENTUNLOCKRESPONSE']._serialized_end=3554
  _globals['_ACCELERATETOWNSEGMENTUNLOCKREQUEST']._serialized_start=3557
  _globals['_ACCELERATETOWNSEGMENTUNLOCKREQUEST']._serialized_end=3911
  _globals['_ACCELERATETOWNSEGMENTUNLOCKREQUEST_TIMEREDUCERSPENDSENTRY']._serialized_start=949
  _globals['_ACCELERATETOWNSEGMENTUNLOCKREQUEST_TIMEREDUCERSPENDSENTRY']._serialized_end=1005
  _globals['_ACCELERATETOWNSEGMENTUNLOCKRESPONSE']._serialized_start=3914
  _globals['_ACCELERATETOWNSEGMENTUNLOCKRESPONSE']._serialized_end=4175
  _globals['_UNLOCKBATTLETOWNSEGMENTREQUEST']._serialized_start=4177
  _globals['_UNLOCKBATTLETOWNSEGMENTREQUEST']._serialized_end=4234
  _globals['_UNLOCKBATTLETOWNSEGMENTRESPONSE']._serialized_start=4237
  _globals['_UNLOCKBATTLETOWNSEGMENTRESPONSE']._serialized_end=4413
  _globals['_RECEIVECUMULATIVEAUTOPRODUCTIONSREWARDREQUEST']._serialized_start=4415
  _globals['_RECEIVECUMULATIVEAUTOPRODUCTIONSREWARDREQUEST']._serialized_end=4485
  _globals['_RECEIVECUMULATIVEAUTOPRODUCTIONSREWARDRESPONSE']._serialized_start=4488
  _globals['_RECEIVECUMULATIVEAUTOPRODUCTIONSREWARDRESPONSE']._serialized_end=4933
  _globals['_RECEIVECUMULATIVEAUTOPRODUCTIONSREWARDRESPONSE_REWARDSBYSTRUCTUREIDENTRY']._serialized_start=4758
  _globals['_RECEIVECUMULATIVEAUTOPRODUCTIONSREWARDRESPONSE_REWARDSBYSTRUCTUREIDENTRY']._serialized_end=4885
  _globals['_RECEIVECUMULATIVEAUTOPRODUCTIONSREWARDRESPONSE_REWARDLIST']._serialized_start=4887
  _globals['_RECEIVECUMULATIVEAUTOPRODUCTIONSREWARDRESPONSE_REWARDLIST']._serialized_end=4933
  _globals['_REFRESHFOUNTAINPRODUCTIONREWARDREQUEST']._serialized_start=4935
  _globals['_REFRESHFOUNTAINPRODUCTIONREWARDREQUEST']._serialized_end=4997
  _globals['_REFRESHFOUNTAINPRODUCTIONREWARDRESPONSE']._serialized_start=5000
  _globals['_REFRESHFOUNTAINPRODUCTIONREWARDRESPONSE']._serialized_end=5182
  _globals['_RECEIVEFOUNTAINPRODUCTIONREWARDREQUEST']._serialized_start=5184
  _globals['_RECEIVEFOUNTAINPRODUCTIONREWARDREQUEST']._serialized_end=5246
  _globals['_RECEIVEFOUNTAINPRODUCTIONREWARDRESPONSE']._serialized_start=5249
  _globals['_RECEIVEFOUNTAINPRODUCTIONREWARDRESPONSE']._serialized_end=5465
  _globals['_RECEIVELANDMARKPRODUCTIONREWARDREQUEST']._serialized_start=5467
  _globals['_RECEIVELANDMARKPRODUCTIONREWARDREQUEST']._serialized_end=5529
  _globals['_RECEIVELANDMARKPRODUCTIONREWARDRESPONSE']._serialized_start=5532
  _globals['_RECEIVELANDMARKPRODUCTIONREWARDRESPONSE']._serialized_end=5733
  _globals['_CHANGEAUTOPRODUCTIONCANACTIVATEREQUEST']._serialized_start=5735
  _globals['_CHANGEAUTOPRODUCTIONCANACTIVATEREQUEST']._serialized_end=5814
  _globals['_CHANGEAUTOPRODUCTIONCANACTIVATERESPONSE']._serialized_start=5817
  _globals['_CHANGEAUTOPRODUCTIONCANACTIVATERESPONSE']._serialized_end=5991
  _globals['_SAVETOWNPRESETREQUEST']._serialized_start=5993
  _globals['_SAVETOWNPRESETREQUEST']._serialized_end=6085
  _globals['_SAVETOWNPRESETRESPONSE']._serialized_start=6088
  _globals['_SAVETOWNPRESETRESPONSE']._serialized_end=6241
  _globals['_LOADTOWNPRESETREQUEST']._serialized_start=6243
  _globals['_LOADTOWNPRESETREQUEST']._serialized_end=6285
  _globals['_LOADTOWNPRESETRESPONSE']._serialized_start=6288
  _globals['_LOADTOWNPRESETRESPONSE']._serialized_end=6542
  _globals['_RENAMETOWNPRESETREQUEST']._serialized_start=6544
  _globals['_RENAMETOWNPRESETREQUEST']._serialized_end=6613
  _globals['_RENAMETOWNPRESETRESPONSE']._serialized_start=6616
  _globals['_RENAMETOWNPRESETRESPONSE']._serialized_end=6770
  _globals['_DELETETOWNPRESETREQUEST']._serialized_start=6772
  _globals['_DELETETOWNPRESETREQUEST']._serialized_end=6816
  _globals['_DELETETOWNPRESETRESPONSE']._serialized_start=6818
  _globals['_DELETETOWNPRESETRESPONSE']._serialized_end=6924
  _globals['_CLEARTOWNREQUEST']._serialized_start=6926
  _globals['_CLEARTOWNREQUEST']._serialized_end=7022
  _globals['_CLEARTOWNRESPONSE']._serialized_start=7025
  _globals['_CLEARTOWNRESPONSE']._serialized_end=7230
  _globals['_UPGRADETOWNPRESETSTORAGEREQUEST']._serialized_start=7232
  _globals['_UPGRADETOWNPRESETSTORAGEREQUEST']._serialized_end=7265
  _globals['_UPGRADETOWNPRESETSTORAGERESPONSE']._serialized_start=7268
  _globals['_UPGRADETOWNPRESETSTORAGERESPONSE']._serialized_end=7434
  _globals['_SETSTRUCTUREBOOKMARKEDREQUEST']._serialized_start=7436
  _globals['_SETSTRUCTUREBOOKMARKEDREQUEST']._serialized_end=7514
  _globals['_SETSTRUCTUREBOOKMARKEDRESPONSE']._serialized_start=7517
  _globals['_SETSTRUCTUREBOOKMARKEDRESPONSE']._serialized_end=7657
  _globals['_SETHOUSEIDSBOOKMARKEDREQUEST']._serialized_start=7659
  _globals['_SETHOUSEIDSBOOKMARKEDREQUEST']._serialized_end=7728
  _globals['_SETHOUSEIDSBOOKMARKEDRESPONSE']._serialized_start=7731
  _globals['_SETHOUSEIDSBOOKMARKEDRESPONSE']._serialized_end=7862
  _globals['_UNLOCKSKYGARDENISLANDREQUEST']._serialized_start=7864
  _globals['_UNLOCKSKYGARDENISLANDREQUEST']._serialized_end=7918
  _globals['_UNLOCKSKYGARDENISLANDRESPONSE']._serialized_start=7921
  _globals['_UNLOCKSKYGARDENISLANDRESPONSE']._serialized_end=8073
  _globals['_GETTOWNPRESETREQUEST']._serialized_start=8075
  _globals['_GETTOWNPRESETREQUEST']._serialized_end=8116
  _globals['_GETTOWNPRESETRESPONSE']._serialized_start=8119
  _globals['_GETTOWNPRESETRESPONSE']._serialized_end=8393
  _globals['_TOWNSERVICE']._serialized_start=8396
  _globals['_TOWNSERVICE']._serialized_end=11396
# @@protoc_insertion_point(module_scope)
