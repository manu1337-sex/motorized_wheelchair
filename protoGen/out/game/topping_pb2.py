# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: game/topping.proto
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
    'game/topping.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import prot.common_entities_pb2 as common__entities__pb2
import prot.game.entities_pb2 as game_dot_entities__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12game/topping.proto\x12\x07\x63k.game\x1a\x15\x63ommon_entities.proto\x1a\x13game/entities.proto\"\x99\x02\n\x16TransferToppingRequest\x12\x18\n\x10moved_topping_id\x18\x01 \x01(\t\x12\x1c\n\x14giver_cookie_data_id\x18\x02 \x01(\x05\x12&\n\x1egiver_cookie_preset_slot_index\x18\x03 \x01(\x05\x12\'\n\x1fgiver_cookie_topping_slot_index\x18\x04 \x01(\x05\x12\x1f\n\x17receiver_cookie_data_id\x18\x05 \x01(\x05\x12)\n!receiver_cookie_preset_slot_index\x18\x06 \x01(\x05\x12*\n\"receiver_cookie_topping_slot_index\x18\x07 \x01(\x05\"\xa6\x02\n\x17TransferToppingResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\'\n\rmoved_topping\x18\x02 \x01(\x0b\x32\x10.ck.game.Topping\x12>\n\x1creceiver_preexisting_topping\x18\x03 \x01(\x0b\x32\x18.ck.game.ToppingOptional\x12\x33\n\x19receiver_unequip_payments\x18\x04 \x03(\x0b\x32\x10.ck.game.Payment\x12\x30\n\x16giver_unequip_payments\x18\x05 \x03(\x0b\x32\x10.ck.game.Payment\"\x8d\x01\n\x13\x45quipToppingRequest\x12\'\n\x07topping\x18\x01 \x01(\x0b\x32\x16.ck.game.TargetTopping\x12\x16\n\x0e\x63ookie_data_id\x18\x02 \x01(\x05\x12\x19\n\x11preset_slot_index\x18\x03 \x01(\x05\x12\x1a\n\x12topping_slot_index\x18\x04 \x01(\x05\"\x94\x02\n\x14\x45quipToppingResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12!\n\x07topping\x18\x02 \x01(\x0b\x32\x10.ck.game.Topping\x12\x35\n\x13preexisting_topping\x18\x03 \x01(\x0b\x32\x18.ck.game.ToppingOptional\x12*\n\x10unequip_payments\x18\x04 \x03(\x0b\x32\x10.ck.game.Payment\x12\x39\n\x17vanilla_topping_payment\x18\x05 \x01(\x0b\x32\x18.ck.game.PaymentOptional\"f\n\x15UnequipToppingRequest\x12\x16\n\x0e\x63ookie_data_id\x18\x01 \x01(\x05\x12\x19\n\x11preset_slot_index\x18\x02 \x01(\x05\x12\x1a\n\x12topping_slot_index\x18\x03 \x01(\x05\"\x9c\x01\n\x16UnequipToppingResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12!\n\x07topping\x18\x02 \x01(\x0b\x32\x10.ck.game.Topping\x12\"\n\x08payments\x18\x03 \x03(\x0b\x32\x10.ck.game.Payment\"Q\n\x15UpgradeToppingRequest\x12\'\n\x07topping\x18\x01 \x01(\x0b\x32\x16.ck.game.TargetTopping\x12\x0f\n\x07is_auto\x18\x02 \x01(\x08\"\xeb\x01\n\x16UpgradeToppingResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12!\n\x07topping\x18\x02 \x01(\x0b\x32\x10.ck.game.Topping\x12\"\n\x08payments\x18\x03 \x03(\x0b\x32\x10.ck.game.Payment\x12\x39\n\x17vanilla_topping_payment\x18\x04 \x01(\x0b\x32\x18.ck.game.PaymentOptional\x12\x12\n\nis_success\x18\x05 \x01(\x08\"\xbd\x01\n\x1a\x44isassembleToppingsRequest\x12\x13\n\x0btopping_ids\x18\x01 \x03(\t\x12R\n\x10vanilla_toppings\x18\x02 \x03(\x0b\x32\x38.ck.game.DisassembleToppingsRequest.VanillaToppingsEntry\x1a\x36\n\x14VanillaToppingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\"\xe7\x01\n\x1b\x44isassembleToppingsResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\"\n\x08payments\x18\x02 \x03(\x0b\x32\x10.ck.game.Payment\x12 \n\x07rewards\x18\x03 \x03(\x0b\x32\x0f.ck.game.Reward\x12\x45\n\x1c\x63hanged_topping_combinations\x18\x04 \x03(\x0b\x32\x1f.ck.game.ToppingCombinationSlot\"f\n\x12MarkToppingRequest\x12\'\n\x07topping\x18\x01 \x01(\x0b\x32\x16.ck.game.TargetTopping\x12\'\n\x06marker\x18\x02 \x01(\x0b\x32\x17.ck.game.FavoriteMarker\"\xb0\x01\n\x13MarkToppingResponse\x12!\n\x07topping\x18\x01 \x01(\x0b\x32\x10.ck.game.Topping\x12\x39\n\x17vanilla_topping_payment\x18\x03 \x01(\x0b\x32\x18.ck.game.PaymentOptional\x12;\n\x11\x61\x64\x64itional_events\x18\x04 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\"*\n\x14UnmarkToppingRequest\x12\x12\n\ntopping_id\x18\x01 \x01(\t\"w\n\x15UnmarkToppingResponse\x12!\n\x07topping\x18\x01 \x01(\x0b\x32\x10.ck.game.Topping\x12;\n\x11\x61\x64\x64itional_events\x18\x03 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\"\x82\x01\n\x1dSaveToppingCombinationRequest\x12 \n\x18\x63ombination_slot_data_id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x16\n\x0e\x63ookie_data_id\x18\x03 \x01(\x05\x12\x19\n\x11preset_slot_index\x18\x04 \x01(\x05\"\x92\x01\n\x1eSaveToppingCombinationResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x33\n\nsaved_slot\x18\x02 \x01(\x0b\x32\x1f.ck.game.ToppingCombinationSlot\"t\n\x1dLoadToppingCombinationRequest\x12 \n\x18\x63ombination_slot_data_id\x18\x01 \x01(\x05\x12\x16\n\x0e\x63ookie_data_id\x18\x02 \x01(\x05\x12\x19\n\x11preset_slot_index\x18\x03 \x01(\x05\"\xdb\x01\n\x1eLoadToppingCombinationResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12+\n\x11\x65quipped_toppings\x18\x02 \x03(\x0b\x32\x10.ck.game.Topping\x12+\n\x11\x64\x65tached_toppings\x18\x03 \x03(\x0b\x32\x10.ck.game.Topping\x12\"\n\x08payments\x18\x04 \x03(\x0b\x32\x10.ck.game.Payment\"Y\n\'ChangeToppingCombinationSlotNameRequest\x12 \n\x18\x63ombination_slot_data_id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x97\x01\n(ChangeToppingCombinationSlotNameResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12 \n\x18\x63ombination_slot_data_id\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\"G\n#UnlockToppingCombinationSlotRequest\x12 \n\x18\x63ombination_slot_data_id\x18\x01 \x01(\x05\"\xbf\x01\n$UnlockToppingCombinationSlotResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x36\n\runlocked_slot\x18\x02 \x01(\x0b\x32\x1f.ck.game.ToppingCombinationSlot\x12\"\n\x08payments\x18\x03 \x03(\x0b\x32\x10.ck.game.Payment\"^\n\x1cUpgradeToppingsAtOnceRequest\x12(\n\x08toppings\x18\x01 \x03(\x0b\x32\x16.ck.game.TargetTopping\x12\x14\n\x0ctarget_grade\x18\x02 \x01(\x05\"(\n\x15ToppingUpgradeResults\x12\x0f\n\x07results\x18\x01 \x03(\x08\"\xc9\x03\n\x1dUpgradeToppingsAtOnceResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\"\n\x08toppings\x18\x02 \x03(\x0b\x32\x10.ck.game.Topping\x12\x0c\n\x04step\x18\x03 \x01(\x05\x12\x37\n\tend_cause\x18\x04 \x01(\x0e\x32$.ck.game.ToppingBatchUpgradeEndCause\x12\"\n\x08payments\x18\x05 \x03(\x0b\x32\x10.ck.game.Payment\x12\x32\n\x18vanilla_topping_payments\x18\x06 \x03(\x0b\x32\x10.ck.game.Payment\x12R\n\x0fresult_per_step\x18\x07 \x03(\x0b\x32\x39.ck.game.UpgradeToppingsAtOnceResponse.ResultPerStepEntry\x1aT\n\x12ResultPerStepEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12-\n\x05value\x18\x02 \x01(\x0b\x32\x1e.ck.game.ToppingUpgradeResults:\x02\x38\x01\"F\n\"ResetToppingCombinationSlotRequest\x12 \n\x18\x63ombination_slot_data_id\x18\x01 \x01(\x05\"`\n#ResetToppingCombinationSlotResponse\x12\x39\n\x10\x63ombination_slot\x18\x01 \x01(\x0b\x32\x1f.ck.game.ToppingCombinationSlot\"Q\n\x1cResetEquippedToppingsRequest\x12\x16\n\x0e\x63ookie_data_id\x18\x01 \x01(\x05\x12\x19\n\x11preset_slot_index\x18\x02 \x01(\x05\"\xa4\x01\n\x1dResetEquippedToppingsResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\"\n\x08toppings\x18\x02 \x03(\x0b\x32\x10.ck.game.Topping\x12\"\n\x08payments\x18\x03 \x03(\x0b\x32\x10.ck.game.Payment2\xfc\n\n\x0eToppingService\x12T\n\x0fTransferTopping\x12\x1f.ck.game.TransferToppingRequest\x1a .ck.game.TransferToppingResponse\x12K\n\x0c\x45quipTopping\x12\x1c.ck.game.EquipToppingRequest\x1a\x1d.ck.game.EquipToppingResponse\x12Q\n\x0eUnequipTopping\x12\x1e.ck.game.UnequipToppingRequest\x1a\x1f.ck.game.UnequipToppingResponse\x12Q\n\x0eUpgradeTopping\x12\x1e.ck.game.UpgradeToppingRequest\x1a\x1f.ck.game.UpgradeToppingResponse\x12`\n\x13\x44isassembleToppings\x12#.ck.game.DisassembleToppingsRequest\x1a$.ck.game.DisassembleToppingsResponse\x12H\n\x0bMarkTopping\x12\x1b.ck.game.MarkToppingRequest\x1a\x1c.ck.game.MarkToppingResponse\x12N\n\rUnmarkTopping\x12\x1d.ck.game.UnmarkToppingRequest\x1a\x1e.ck.game.UnmarkToppingResponse\x12i\n\x16SaveToppingCombination\x12&.ck.game.SaveToppingCombinationRequest\x1a\'.ck.game.SaveToppingCombinationResponse\x12i\n\x16LoadToppingCombination\x12&.ck.game.LoadToppingCombinationRequest\x1a\'.ck.game.LoadToppingCombinationResponse\x12\x87\x01\n ChangeToppingCombinationSlotName\x12\x30.ck.game.ChangeToppingCombinationSlotNameRequest\x1a\x31.ck.game.ChangeToppingCombinationSlotNameResponse\x12{\n\x1cUnlockToppingCombinationSlot\x12,.ck.game.UnlockToppingCombinationSlotRequest\x1a-.ck.game.UnlockToppingCombinationSlotResponse\x12\x66\n\x15UpgradeToppingsAtOnce\x12%.ck.game.UpgradeToppingsAtOnceRequest\x1a&.ck.game.UpgradeToppingsAtOnceResponse\x12x\n\x1bResetToppingCombinationSlot\x12+.ck.game.ResetToppingCombinationSlotRequest\x1a,.ck.game.ResetToppingCombinationSlotResponse\x12\x66\n\x15ResetEquippedToppings\x12%.ck.game.ResetEquippedToppingsRequest\x1a&.ck.game.ResetEquippedToppingsResponseBC\n(com.devsisters.ck.services.game.protobuf\xaa\x02\x16Services.Game.Protobufb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'game.topping_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(com.devsisters.ck.services.game.protobuf\252\002\026Services.Game.Protobuf'
  _globals['_DISASSEMBLETOPPINGSREQUEST_VANILLATOPPINGSENTRY']._loaded_options = None
  _globals['_DISASSEMBLETOPPINGSREQUEST_VANILLATOPPINGSENTRY']._serialized_options = b'8\001'
  _globals['_UPGRADETOPPINGSATONCERESPONSE_RESULTPERSTEPENTRY']._loaded_options = None
  _globals['_UPGRADETOPPINGSATONCERESPONSE_RESULTPERSTEPENTRY']._serialized_options = b'8\001'
  _globals['_TRANSFERTOPPINGREQUEST']._serialized_start=76
  _globals['_TRANSFERTOPPINGREQUEST']._serialized_end=357
  _globals['_TRANSFERTOPPINGRESPONSE']._serialized_start=360
  _globals['_TRANSFERTOPPINGRESPONSE']._serialized_end=654
  _globals['_EQUIPTOPPINGREQUEST']._serialized_start=657
  _globals['_EQUIPTOPPINGREQUEST']._serialized_end=798
  _globals['_EQUIPTOPPINGRESPONSE']._serialized_start=801
  _globals['_EQUIPTOPPINGRESPONSE']._serialized_end=1077
  _globals['_UNEQUIPTOPPINGREQUEST']._serialized_start=1079
  _globals['_UNEQUIPTOPPINGREQUEST']._serialized_end=1181
  _globals['_UNEQUIPTOPPINGRESPONSE']._serialized_start=1184
  _globals['_UNEQUIPTOPPINGRESPONSE']._serialized_end=1340
  _globals['_UPGRADETOPPINGREQUEST']._serialized_start=1342
  _globals['_UPGRADETOPPINGREQUEST']._serialized_end=1423
  _globals['_UPGRADETOPPINGRESPONSE']._serialized_start=1426
  _globals['_UPGRADETOPPINGRESPONSE']._serialized_end=1661
  _globals['_DISASSEMBLETOPPINGSREQUEST']._serialized_start=1664
  _globals['_DISASSEMBLETOPPINGSREQUEST']._serialized_end=1853
  _globals['_DISASSEMBLETOPPINGSREQUEST_VANILLATOPPINGSENTRY']._serialized_start=1799
  _globals['_DISASSEMBLETOPPINGSREQUEST_VANILLATOPPINGSENTRY']._serialized_end=1853
  _globals['_DISASSEMBLETOPPINGSRESPONSE']._serialized_start=1856
  _globals['_DISASSEMBLETOPPINGSRESPONSE']._serialized_end=2087
  _globals['_MARKTOPPINGREQUEST']._serialized_start=2089
  _globals['_MARKTOPPINGREQUEST']._serialized_end=2191
  _globals['_MARKTOPPINGRESPONSE']._serialized_start=2194
  _globals['_MARKTOPPINGRESPONSE']._serialized_end=2370
  _globals['_UNMARKTOPPINGREQUEST']._serialized_start=2372
  _globals['_UNMARKTOPPINGREQUEST']._serialized_end=2414
  _globals['_UNMARKTOPPINGRESPONSE']._serialized_start=2416
  _globals['_UNMARKTOPPINGRESPONSE']._serialized_end=2535
  _globals['_SAVETOPPINGCOMBINATIONREQUEST']._serialized_start=2538
  _globals['_SAVETOPPINGCOMBINATIONREQUEST']._serialized_end=2668
  _globals['_SAVETOPPINGCOMBINATIONRESPONSE']._serialized_start=2671
  _globals['_SAVETOPPINGCOMBINATIONRESPONSE']._serialized_end=2817
  _globals['_LOADTOPPINGCOMBINATIONREQUEST']._serialized_start=2819
  _globals['_LOADTOPPINGCOMBINATIONREQUEST']._serialized_end=2935
  _globals['_LOADTOPPINGCOMBINATIONRESPONSE']._serialized_start=2938
  _globals['_LOADTOPPINGCOMBINATIONRESPONSE']._serialized_end=3157
  _globals['_CHANGETOPPINGCOMBINATIONSLOTNAMEREQUEST']._serialized_start=3159
  _globals['_CHANGETOPPINGCOMBINATIONSLOTNAMEREQUEST']._serialized_end=3248
  _globals['_CHANGETOPPINGCOMBINATIONSLOTNAMERESPONSE']._serialized_start=3251
  _globals['_CHANGETOPPINGCOMBINATIONSLOTNAMERESPONSE']._serialized_end=3402
  _globals['_UNLOCKTOPPINGCOMBINATIONSLOTREQUEST']._serialized_start=3404
  _globals['_UNLOCKTOPPINGCOMBINATIONSLOTREQUEST']._serialized_end=3475
  _globals['_UNLOCKTOPPINGCOMBINATIONSLOTRESPONSE']._serialized_start=3478
  _globals['_UNLOCKTOPPINGCOMBINATIONSLOTRESPONSE']._serialized_end=3669
  _globals['_UPGRADETOPPINGSATONCEREQUEST']._serialized_start=3671
  _globals['_UPGRADETOPPINGSATONCEREQUEST']._serialized_end=3765
  _globals['_TOPPINGUPGRADERESULTS']._serialized_start=3767
  _globals['_TOPPINGUPGRADERESULTS']._serialized_end=3807
  _globals['_UPGRADETOPPINGSATONCERESPONSE']._serialized_start=3810
  _globals['_UPGRADETOPPINGSATONCERESPONSE']._serialized_end=4267
  _globals['_UPGRADETOPPINGSATONCERESPONSE_RESULTPERSTEPENTRY']._serialized_start=4183
  _globals['_UPGRADETOPPINGSATONCERESPONSE_RESULTPERSTEPENTRY']._serialized_end=4267
  _globals['_RESETTOPPINGCOMBINATIONSLOTREQUEST']._serialized_start=4269
  _globals['_RESETTOPPINGCOMBINATIONSLOTREQUEST']._serialized_end=4339
  _globals['_RESETTOPPINGCOMBINATIONSLOTRESPONSE']._serialized_start=4341
  _globals['_RESETTOPPINGCOMBINATIONSLOTRESPONSE']._serialized_end=4437
  _globals['_RESETEQUIPPEDTOPPINGSREQUEST']._serialized_start=4439
  _globals['_RESETEQUIPPEDTOPPINGSREQUEST']._serialized_end=4520
  _globals['_RESETEQUIPPEDTOPPINGSRESPONSE']._serialized_start=4523
  _globals['_RESETEQUIPPEDTOPPINGSRESPONSE']._serialized_end=4687
  _globals['_TOPPINGSERVICE']._serialized_start=4690
  _globals['_TOPPINGSERVICE']._serialized_end=6094
# @@protoc_insertion_point(module_scope)
