# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: game/mail.proto
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
    'game/mail.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import prot.common_entities_pb2 as common__entities__pb2
import prot.game.entities_pb2 as game_dot_entities__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fgame/mail.proto\x12\x07\x63k.game\x1a\x15\x63ommon_entities.proto\x1a\x13game/entities.proto\"\x13\n\x11GetMailBoxRequest\"8\n\x12GetMailBoxResponse\x12\"\n\x08mail_box\x18\x01 \x01(\x0b\x32\x10.ck.game.MailBox\"\x1a\n\x18GetMailBoxSummaryRequest\"N\n\x19GetMailBoxSummaryResponse\x12\x31\n\x10mail_box_summary\x18\x01 \x01(\x0b\x32\x17.ck.game.MailBoxSummary\"-\n\x19ReceiveMailRewardsRequest\x12\x10\n\x08mail_ids\x18\x01 \x03(\t\"\xa1\x01\n\x1aReceiveMailRewardsResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12$\n\rupdated_mails\x18\x02 \x03(\x0b\x32\r.ck.game.Mail\x12 \n\x07rewards\x18\x03 \x03(\x0b\x32\x0f.ck.game.Reward2\x8f\x02\n\x0bMailService\x12\x45\n\nGetMailBox\x12\x1a.ck.game.GetMailBoxRequest\x1a\x1b.ck.game.GetMailBoxResponse\x12Z\n\x11GetMailBoxSummary\x12!.ck.game.GetMailBoxSummaryRequest\x1a\".ck.game.GetMailBoxSummaryResponse\x12]\n\x12ReceiveMailRewards\x12\".ck.game.ReceiveMailRewardsRequest\x1a#.ck.game.ReceiveMailRewardsResponseBC\n(com.devsisters.ck.services.game.protobuf\xaa\x02\x16Services.Game.Protobufb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'game.mail_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(com.devsisters.ck.services.game.protobuf\252\002\026Services.Game.Protobuf'
  _globals['_GETMAILBOXREQUEST']._serialized_start=72
  _globals['_GETMAILBOXREQUEST']._serialized_end=91
  _globals['_GETMAILBOXRESPONSE']._serialized_start=93
  _globals['_GETMAILBOXRESPONSE']._serialized_end=149
  _globals['_GETMAILBOXSUMMARYREQUEST']._serialized_start=151
  _globals['_GETMAILBOXSUMMARYREQUEST']._serialized_end=177
  _globals['_GETMAILBOXSUMMARYRESPONSE']._serialized_start=179
  _globals['_GETMAILBOXSUMMARYRESPONSE']._serialized_end=257
  _globals['_RECEIVEMAILREWARDSREQUEST']._serialized_start=259
  _globals['_RECEIVEMAILREWARDSREQUEST']._serialized_end=304
  _globals['_RECEIVEMAILREWARDSRESPONSE']._serialized_start=307
  _globals['_RECEIVEMAILREWARDSRESPONSE']._serialized_end=468
  _globals['_MAILSERVICE']._serialized_start=471
  _globals['_MAILSERVICE']._serialized_end=742
# @@protoc_insertion_point(module_scope)
