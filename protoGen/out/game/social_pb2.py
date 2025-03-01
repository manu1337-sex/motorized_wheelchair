# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: game/social.proto
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
    'game/social.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import prot.common_entities_pb2 as common__entities__pb2
import prot.game.entities_pb2 as game_dot_entities__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11game/social.proto\x12\x07\x63k.game\x1a\x15\x63ommon_entities.proto\x1a\x13game/entities.proto\"\x17\n\x15GetSocialStateRequest\"n\n\x16GetSocialStateResponse\x12*\n\x0csocial_state\x18\x01 \x01(\x0b\x32\x14.ck.game.SocialState\x12(\n\x0bpvp_summary\x18\x02 \x01(\x0b\x32\x13.ck.game.PvpSummary\"+\n\x12SearchUsersRequest\x12\x15\n\rsearch_string\x18\x01 \x01(\t\"E\n\x13SearchUsersResponse\x12.\n\x0esearched_users\x18\x01 \x03(\x0b\x32\x16.ck.game.SocialSummary\"\x1e\n\x1cGetRecommendedFriendsRequest\"R\n\x1dGetRecommendedFriendsResponse\x12\x31\n\x11recommended_users\x18\x01 \x03(\x0b\x32\x16.ck.game.SocialSummary\"(\n\x15GetUserSummaryRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"D\n\x16GetUserSummaryResponse\x12*\n\x0cuser_summary\x18\x01 \x01(\x0b\x32\x14.ck.game.UserSummary\"+\n\x17GetUserSummariesRequest\x12\x10\n\x08user_ids\x18\x01 \x03(\t\"l\n\x18GetUserSummariesResponse\x12\x19\n\x11searched_user_ids\x18\x01 \x03(\t\x12\x35\n\x17\x65xisting_user_summaries\x18\x02 \x03(\x0b\x32\x14.ck.game.UserSummary\"*\n\x17GetSocialSummaryRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"J\n\x18GetSocialSummaryResponse\x12.\n\x0esocial_summary\x18\x01 \x01(\x0b\x32\x16.ck.game.SocialSummary\"-\n\x19GetSocialSummariesRequest\x12\x10\n\x08user_ids\x18\x01 \x03(\t\"N\n\x1aGetSocialSummariesResponse\x12\x30\n\x10social_summaries\x18\x01 \x03(\x0b\x32\x16.ck.game.SocialSummary\"*\n\x17GetFriendProfileRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"S\n\x18GetFriendProfileResponse\x12\x37\n\x16\x66riend_kingdom_profile\x18\x01 \x01(\x0b\x32\x17.ck.game.KingdomProfile\"%\n\x10\x41\x64\x64\x46riendRequest\x12\x11\n\tfriend_id\x18\x01 \x01(\t\"~\n\x11\x41\x64\x64\x46riendResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12,\n\x0csent_request\x18\x02 \x01(\x0b\x32\x16.ck.game.FriendRequest\"(\n\x13\x44\x65leteFriendRequest\x12\x11\n\tfriend_id\x18\x01 \x01(\t\"f\n\x14\x44\x65leteFriendResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x11\n\tfriend_id\x18\x02 \x01(\t\"/\n\x1a\x43\x61ncelFriendRequestRequest\x12\x11\n\tfriend_id\x18\x01 \x01(\t\"m\n\x1b\x43\x61ncelFriendRequestResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x11\n\tfriend_id\x18\x02 \x01(\t\"/\n\x1a\x41\x63\x63\x65ptFriendRequestRequest\x12\x11\n\tfriend_id\x18\x01 \x01(\t\"\x81\x01\n\x1b\x41\x63\x63\x65ptFriendRequestResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12%\n\x0c\x61\x64\x64\x65\x64_friend\x18\x02 \x01(\x0b\x32\x0f.ck.game.Friend\"/\n\x1aRejectFriendRequestRequest\x12\x11\n\tfriend_id\x18\x01 \x01(\t\"m\n\x1bRejectFriendRequestResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x11\n\tfriend_id\x18\x02 \x01(\t\",\n\x17GetFriendKingdomRequest\x12\x11\n\tfriend_id\x18\x01 \x01(\t\"\xa5\x02\n\x18GetFriendKingdomResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x11\n\tfriend_id\x18\x02 \x01(\t\x12!\n\x07kingdom\x18\x03 \x01(\x0b\x32\x10.ck.game.Kingdom\x12(\n\x0bpvp_summary\x18\x04 \x01(\x0b\x32\x13.ck.game.PvpSummary\x12\x34\n\x13guild_summary_value\x18\x05 \x01(\x0b\x32\x15.ck.game.GuildSummaryH\x00\x12%\n\x10no_guild_summary\x18\x06 \x01(\x0b\x32\t.ck.EmptyH\x00\x42\x0f\n\rguild_summary\"&\n\x0fSendLikeRequest\x12\x13\n\x0breceiver_id\x18\x01 \x01(\t\"\xd6\x01\n\x10SendLikeResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x13\n\x0breceiver_id\x18\x02 \x01(\t\x12 \n\x07rewards\x18\x03 \x03(\x0b\x32\x0f.ck.game.Reward\x12(\n receiver_popularity_points_delta\x18\x04 \x01(\x03\x12$\n\x1c\x63hanged_receiver_likes_count\x18\x05 \x01(\x05\"T\n\x1aSendDailyRandomGiftRequest\x12!\n\x19\x64\x61ily_random_gift_data_id\x18\x01 \x01(\x05\x12\x13\n\x0breceiver_id\x18\x02 \x01(\t\"\xc6\x02\n\x1bSendDailyRandomGiftResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x13\n\x0breceiver_id\x18\x02 \x01(\t\x12 \n\x07rewards\x18\x03 \x03(\x0b\x32\x0f.ck.game.Reward\x12$\n\x1csent_daily_random_gift_count\x18\x04 \x01(\x05\x12\x37\n%daily_random_gift_count_next_reset_at\x18\x05 \x01(\x0b\x32\x08.ck.Time\x12\x30\n\x1e\x64\x61ily_random_gift_last_sent_at\x18\x06 \x01(\x0b\x32\x08.ck.Time\x12\"\n\x1areceiver_popularity_points\x18\x07 \x01(\x03\"V\n\x1bSendDailyRandomGiftsRequest\x12!\n\x19\x64\x61ily_random_gift_data_id\x18\x01 \x01(\x05\x12\x14\n\x0creceiver_ids\x18\x02 \x03(\t\"\x90\x03\n\x1cSendDailyRandomGiftsResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12 \n\x07rewards\x18\x02 \x03(\x0b\x32\x0f.ck.game.Reward\x12$\n\x1csent_daily_random_gift_count\x18\x03 \x01(\x05\x12\x37\n%daily_random_gift_count_next_reset_at\x18\x04 \x01(\x0b\x32\x08.ck.Time\x12=\n\x07results\x18\x05 \x03(\x0b\x32,.ck.game.SendDailyRandomGiftsResponse.Result\x1as\n\x06Result\x12\x13\n\x0breceiver_id\x18\x01 \x01(\t\x12\x30\n\x1e\x64\x61ily_random_gift_last_sent_at\x18\x02 \x01(\x0b\x32\x08.ck.Time\x12\"\n\x1areceiver_popularity_points\x18\x03 \x01(\x03\"X\n\x1cSendSpecialRandomGiftRequest\x12#\n\x1bspecial_random_gift_data_id\x18\x01 \x01(\x05\x12\x13\n\x0breceiver_id\x18\x02 \x01(\t\"\x9a\x02\n\x1dSendSpecialRandomGiftResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x13\n\x0breceiver_id\x18\x02 \x01(\t\x12\"\n\x08payments\x18\x03 \x03(\x0b\x32\x10.ck.game.Payment\x12 \n\x07rewards\x18\x04 \x03(\x0b\x32\x0f.ck.game.Reward\x12&\n\x1esent_special_random_gift_count\x18\x05 \x01(\x05\x12\x39\n\'special_random_gift_count_next_reset_at\x18\x06 \x01(\x0b\x32\x08.ck.Time\"a\n\x19SendPopularityGiftRequest\x12\x13\n\x0breceiver_id\x18\x01 \x01(\t\x12\x1f\n\x17popularity_gift_data_id\x18\x02 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\"\x89\x02\n\x1aSendPopularityGiftResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x13\n\x0breceiver_id\x18\x02 \x01(\t\x12\x1f\n\x17popularity_gift_data_id\x18\x03 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x03\x12\"\n\x08payments\x18\x05 \x03(\x0b\x32\x10.ck.game.Payment\x12 \n\x07rewards\x18\x06 \x03(\x0b\x32\x0f.ck.game.Reward\x12\"\n\x1areceiver_popularity_points\x18\x07 \x01(\x03\"A\n\'GetPopularityContributionRankingRequest\x12\x16\n\x0etarget_user_id\x18\x01 \x01(\t\"\x94\x01\n(GetPopularityContributionRankingResponse\x12\x16\n\x0etarget_user_id\x18\x01 \x01(\t\x12\x10\n\x08my_score\x18\x02 \x01(\x03\x12>\n\x0btop_records\x18\x03 \x03(\x0b\x32).ck.game.PopularityContributionRankRecord\" \n\x1eGetPopularityTopRankingRequest\"U\n\x1fGetPopularityTopRankingResponse\x12\x32\n\x0btop_records\x18\x01 \x03(\x0b\x32\x1d.ck.game.PopularityRankRecord\":\n\x1eGetFriendlyPvpMatchInfoRequest\x12\x18\n\x10opponent_user_id\x18\x01 \x01(\t\"V\n\x1fGetFriendlyPvpMatchInfoResponse\x12\x33\n\x0fopponent_detail\x18\x01 \x01(\x0b\x32\x1a.ck.game.PvpOpponentDetail\"n\n!SendFriendlyPvpMatchResultRequest\x12\x18\n\x10opponent_user_id\x18\x01 \x01(\t\x12/\n\rbattle_report\x18\x02 \x01(\x0b\x32\x18.ck.game.PvpBattleReport\"{\n\"SendFriendlyPvpMatchResultResponse\x12;\n\x11\x61\x64\x64itional_events\x18\x01 \x01(\x0b\x32 .ck.game.KingdomAdditionalEvents\x12\x18\n\x10opponent_user_id\x18\x02 \x01(\t\"g\n:ChangeUserVisibilityInPopularityContributionRankingRequest\x12\x16\n\x0etarget_user_id\x18\x01 \x01(\t\x12\x11\n\tis_hidden\x18\x02 \x01(\x08\"h\n;ChangeUserVisibilityInPopularityContributionRankingResponse\x12\x16\n\x0etarget_user_id\x18\x01 \x01(\t\x12\x11\n\tis_hidden\x18\x02 \x01(\x08\"7\n$ChangeOnlyFriendsCanSendGiftsRequest\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\"8\n%ChangeOnlyFriendsCanSendGiftsResponse\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\"^\n&GetSocialSummariesWithPvpRatingRequest\x12\"\n\x08pvp_type\x18\x01 \x01(\x0e\x32\x10.ck.game.PvpType\x12\x10\n\x08user_ids\x18\x02 \x03(\t\"\xdb\x01\n\'GetSocialSummariesWithPvpRatingResponse\x12\x30\n\x10social_summaries\x18\x01 \x03(\x0b\x32\x16.ck.game.SocialSummary\x12N\n\x07ratings\x18\x02 \x03(\x0b\x32=.ck.game.GetSocialSummariesWithPvpRatingResponse.RatingsEntry\x1a.\n\x0cRatingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x32\xd7\x14\n\rSocialService\x12Q\n\x0eGetSocialState\x12\x1e.ck.game.GetSocialStateRequest\x1a\x1f.ck.game.GetSocialStateResponse\x12H\n\x0bSearchUsers\x12\x1b.ck.game.SearchUsersRequest\x1a\x1c.ck.game.SearchUsersResponse\x12\x66\n\x15GetRecommendedFriends\x12%.ck.game.GetRecommendedFriendsRequest\x1a&.ck.game.GetRecommendedFriendsResponse\x12Q\n\x0eGetUserSummary\x12\x1e.ck.game.GetUserSummaryRequest\x1a\x1f.ck.game.GetUserSummaryResponse\x12W\n\x10GetUserSummaries\x12 .ck.game.GetUserSummariesRequest\x1a!.ck.game.GetUserSummariesResponse\x12W\n\x10GetSocialSummary\x12 .ck.game.GetSocialSummaryRequest\x1a!.ck.game.GetSocialSummaryResponse\x12]\n\x12GetSocialSummaries\x12\".ck.game.GetSocialSummariesRequest\x1a#.ck.game.GetSocialSummariesResponse\x12W\n\x10GetFriendProfile\x12 .ck.game.GetFriendProfileRequest\x1a!.ck.game.GetFriendProfileResponse\x12\x42\n\tAddFriend\x12\x19.ck.game.AddFriendRequest\x1a\x1a.ck.game.AddFriendResponse\x12K\n\x0c\x44\x65leteFriend\x12\x1c.ck.game.DeleteFriendRequest\x1a\x1d.ck.game.DeleteFriendResponse\x12`\n\x13\x43\x61ncelFriendRequest\x12#.ck.game.CancelFriendRequestRequest\x1a$.ck.game.CancelFriendRequestResponse\x12`\n\x13\x41\x63\x63\x65ptFriendRequest\x12#.ck.game.AcceptFriendRequestRequest\x1a$.ck.game.AcceptFriendRequestResponse\x12`\n\x13RejectFriendRequest\x12#.ck.game.RejectFriendRequestRequest\x1a$.ck.game.RejectFriendRequestResponse\x12W\n\x10GetFriendKingdom\x12 .ck.game.GetFriendKingdomRequest\x1a!.ck.game.GetFriendKingdomResponse\x12?\n\x08SendLike\x12\x18.ck.game.SendLikeRequest\x1a\x19.ck.game.SendLikeResponse\x12`\n\x13SendDailyRandomGift\x12#.ck.game.SendDailyRandomGiftRequest\x1a$.ck.game.SendDailyRandomGiftResponse\x12\x63\n\x14SendDailyRandomGifts\x12$.ck.game.SendDailyRandomGiftsRequest\x1a%.ck.game.SendDailyRandomGiftsResponse\x12\x66\n\x15SendSpecialRandomGift\x12%.ck.game.SendSpecialRandomGiftRequest\x1a&.ck.game.SendSpecialRandomGiftResponse\x12]\n\x12SendPopularityGift\x12\".ck.game.SendPopularityGiftRequest\x1a#.ck.game.SendPopularityGiftResponse\x12\x87\x01\n GetPopularityContributionRanking\x12\x30.ck.game.GetPopularityContributionRankingRequest\x1a\x31.ck.game.GetPopularityContributionRankingResponse\x12l\n\x17GetPopularityTopRanking\x12\'.ck.game.GetPopularityTopRankingRequest\x1a(.ck.game.GetPopularityTopRankingResponse\x12l\n\x17GetFriendlyPvpMatchInfo\x12\'.ck.game.GetFriendlyPvpMatchInfoRequest\x1a(.ck.game.GetFriendlyPvpMatchInfoResponse\x12u\n\x1aSendFriendlyPvpMatchResult\x12*.ck.game.SendFriendlyPvpMatchResultRequest\x1a+.ck.game.SendFriendlyPvpMatchResultResponse\x12\xc0\x01\n3ChangeUserVisibilityInPopularityContributionRanking\x12\x43.ck.game.ChangeUserVisibilityInPopularityContributionRankingRequest\x1a\x44.ck.game.ChangeUserVisibilityInPopularityContributionRankingResponse\x12~\n\x1d\x43hangeOnlyFriendsCanSendGifts\x12-.ck.game.ChangeOnlyFriendsCanSendGiftsRequest\x1a..ck.game.ChangeOnlyFriendsCanSendGiftsResponse\x12\x84\x01\n\x1fGetSocialSummariesWithPvpRating\x12/.ck.game.GetSocialSummariesWithPvpRatingRequest\x1a\x30.ck.game.GetSocialSummariesWithPvpRatingResponseBC\n(com.devsisters.ck.services.game.protobuf\xaa\x02\x16Services.Game.Protobufb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'game.social_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(com.devsisters.ck.services.game.protobuf\252\002\026Services.Game.Protobuf'
  _globals['_GETSOCIALSUMMARIESWITHPVPRATINGRESPONSE_RATINGSENTRY']._loaded_options = None
  _globals['_GETSOCIALSUMMARIESWITHPVPRATINGRESPONSE_RATINGSENTRY']._serialized_options = b'8\001'
  _globals['_GETSOCIALSTATEREQUEST']._serialized_start=74
  _globals['_GETSOCIALSTATEREQUEST']._serialized_end=97
  _globals['_GETSOCIALSTATERESPONSE']._serialized_start=99
  _globals['_GETSOCIALSTATERESPONSE']._serialized_end=209
  _globals['_SEARCHUSERSREQUEST']._serialized_start=211
  _globals['_SEARCHUSERSREQUEST']._serialized_end=254
  _globals['_SEARCHUSERSRESPONSE']._serialized_start=256
  _globals['_SEARCHUSERSRESPONSE']._serialized_end=325
  _globals['_GETRECOMMENDEDFRIENDSREQUEST']._serialized_start=327
  _globals['_GETRECOMMENDEDFRIENDSREQUEST']._serialized_end=357
  _globals['_GETRECOMMENDEDFRIENDSRESPONSE']._serialized_start=359
  _globals['_GETRECOMMENDEDFRIENDSRESPONSE']._serialized_end=441
  _globals['_GETUSERSUMMARYREQUEST']._serialized_start=443
  _globals['_GETUSERSUMMARYREQUEST']._serialized_end=483
  _globals['_GETUSERSUMMARYRESPONSE']._serialized_start=485
  _globals['_GETUSERSUMMARYRESPONSE']._serialized_end=553
  _globals['_GETUSERSUMMARIESREQUEST']._serialized_start=555
  _globals['_GETUSERSUMMARIESREQUEST']._serialized_end=598
  _globals['_GETUSERSUMMARIESRESPONSE']._serialized_start=600
  _globals['_GETUSERSUMMARIESRESPONSE']._serialized_end=708
  _globals['_GETSOCIALSUMMARYREQUEST']._serialized_start=710
  _globals['_GETSOCIALSUMMARYREQUEST']._serialized_end=752
  _globals['_GETSOCIALSUMMARYRESPONSE']._serialized_start=754
  _globals['_GETSOCIALSUMMARYRESPONSE']._serialized_end=828
  _globals['_GETSOCIALSUMMARIESREQUEST']._serialized_start=830
  _globals['_GETSOCIALSUMMARIESREQUEST']._serialized_end=875
  _globals['_GETSOCIALSUMMARIESRESPONSE']._serialized_start=877
  _globals['_GETSOCIALSUMMARIESRESPONSE']._serialized_end=955
  _globals['_GETFRIENDPROFILEREQUEST']._serialized_start=957
  _globals['_GETFRIENDPROFILEREQUEST']._serialized_end=999
  _globals['_GETFRIENDPROFILERESPONSE']._serialized_start=1001
  _globals['_GETFRIENDPROFILERESPONSE']._serialized_end=1084
  _globals['_ADDFRIENDREQUEST']._serialized_start=1086
  _globals['_ADDFRIENDREQUEST']._serialized_end=1123
  _globals['_ADDFRIENDRESPONSE']._serialized_start=1125
  _globals['_ADDFRIENDRESPONSE']._serialized_end=1251
  _globals['_DELETEFRIENDREQUEST']._serialized_start=1253
  _globals['_DELETEFRIENDREQUEST']._serialized_end=1293
  _globals['_DELETEFRIENDRESPONSE']._serialized_start=1295
  _globals['_DELETEFRIENDRESPONSE']._serialized_end=1397
  _globals['_CANCELFRIENDREQUESTREQUEST']._serialized_start=1399
  _globals['_CANCELFRIENDREQUESTREQUEST']._serialized_end=1446
  _globals['_CANCELFRIENDREQUESTRESPONSE']._serialized_start=1448
  _globals['_CANCELFRIENDREQUESTRESPONSE']._serialized_end=1557
  _globals['_ACCEPTFRIENDREQUESTREQUEST']._serialized_start=1559
  _globals['_ACCEPTFRIENDREQUESTREQUEST']._serialized_end=1606
  _globals['_ACCEPTFRIENDREQUESTRESPONSE']._serialized_start=1609
  _globals['_ACCEPTFRIENDREQUESTRESPONSE']._serialized_end=1738
  _globals['_REJECTFRIENDREQUESTREQUEST']._serialized_start=1740
  _globals['_REJECTFRIENDREQUESTREQUEST']._serialized_end=1787
  _globals['_REJECTFRIENDREQUESTRESPONSE']._serialized_start=1789
  _globals['_REJECTFRIENDREQUESTRESPONSE']._serialized_end=1898
  _globals['_GETFRIENDKINGDOMREQUEST']._serialized_start=1900
  _globals['_GETFRIENDKINGDOMREQUEST']._serialized_end=1944
  _globals['_GETFRIENDKINGDOMRESPONSE']._serialized_start=1947
  _globals['_GETFRIENDKINGDOMRESPONSE']._serialized_end=2240
  _globals['_SENDLIKEREQUEST']._serialized_start=2242
  _globals['_SENDLIKEREQUEST']._serialized_end=2280
  _globals['_SENDLIKERESPONSE']._serialized_start=2283
  _globals['_SENDLIKERESPONSE']._serialized_end=2497
  _globals['_SENDDAILYRANDOMGIFTREQUEST']._serialized_start=2499
  _globals['_SENDDAILYRANDOMGIFTREQUEST']._serialized_end=2583
  _globals['_SENDDAILYRANDOMGIFTRESPONSE']._serialized_start=2586
  _globals['_SENDDAILYRANDOMGIFTRESPONSE']._serialized_end=2912
  _globals['_SENDDAILYRANDOMGIFTSREQUEST']._serialized_start=2914
  _globals['_SENDDAILYRANDOMGIFTSREQUEST']._serialized_end=3000
  _globals['_SENDDAILYRANDOMGIFTSRESPONSE']._serialized_start=3003
  _globals['_SENDDAILYRANDOMGIFTSRESPONSE']._serialized_end=3403
  _globals['_SENDDAILYRANDOMGIFTSRESPONSE_RESULT']._serialized_start=3288
  _globals['_SENDDAILYRANDOMGIFTSRESPONSE_RESULT']._serialized_end=3403
  _globals['_SENDSPECIALRANDOMGIFTREQUEST']._serialized_start=3405
  _globals['_SENDSPECIALRANDOMGIFTREQUEST']._serialized_end=3493
  _globals['_SENDSPECIALRANDOMGIFTRESPONSE']._serialized_start=3496
  _globals['_SENDSPECIALRANDOMGIFTRESPONSE']._serialized_end=3778
  _globals['_SENDPOPULARITYGIFTREQUEST']._serialized_start=3780
  _globals['_SENDPOPULARITYGIFTREQUEST']._serialized_end=3877
  _globals['_SENDPOPULARITYGIFTRESPONSE']._serialized_start=3880
  _globals['_SENDPOPULARITYGIFTRESPONSE']._serialized_end=4145
  _globals['_GETPOPULARITYCONTRIBUTIONRANKINGREQUEST']._serialized_start=4147
  _globals['_GETPOPULARITYCONTRIBUTIONRANKINGREQUEST']._serialized_end=4212
  _globals['_GETPOPULARITYCONTRIBUTIONRANKINGRESPONSE']._serialized_start=4215
  _globals['_GETPOPULARITYCONTRIBUTIONRANKINGRESPONSE']._serialized_end=4363
  _globals['_GETPOPULARITYTOPRANKINGREQUEST']._serialized_start=4365
  _globals['_GETPOPULARITYTOPRANKINGREQUEST']._serialized_end=4397
  _globals['_GETPOPULARITYTOPRANKINGRESPONSE']._serialized_start=4399
  _globals['_GETPOPULARITYTOPRANKINGRESPONSE']._serialized_end=4484
  _globals['_GETFRIENDLYPVPMATCHINFOREQUEST']._serialized_start=4486
  _globals['_GETFRIENDLYPVPMATCHINFOREQUEST']._serialized_end=4544
  _globals['_GETFRIENDLYPVPMATCHINFORESPONSE']._serialized_start=4546
  _globals['_GETFRIENDLYPVPMATCHINFORESPONSE']._serialized_end=4632
  _globals['_SENDFRIENDLYPVPMATCHRESULTREQUEST']._serialized_start=4634
  _globals['_SENDFRIENDLYPVPMATCHRESULTREQUEST']._serialized_end=4744
  _globals['_SENDFRIENDLYPVPMATCHRESULTRESPONSE']._serialized_start=4746
  _globals['_SENDFRIENDLYPVPMATCHRESULTRESPONSE']._serialized_end=4869
  _globals['_CHANGEUSERVISIBILITYINPOPULARITYCONTRIBUTIONRANKINGREQUEST']._serialized_start=4871
  _globals['_CHANGEUSERVISIBILITYINPOPULARITYCONTRIBUTIONRANKINGREQUEST']._serialized_end=4974
  _globals['_CHANGEUSERVISIBILITYINPOPULARITYCONTRIBUTIONRANKINGRESPONSE']._serialized_start=4976
  _globals['_CHANGEUSERVISIBILITYINPOPULARITYCONTRIBUTIONRANKINGRESPONSE']._serialized_end=5080
  _globals['_CHANGEONLYFRIENDSCANSENDGIFTSREQUEST']._serialized_start=5082
  _globals['_CHANGEONLYFRIENDSCANSENDGIFTSREQUEST']._serialized_end=5137
  _globals['_CHANGEONLYFRIENDSCANSENDGIFTSRESPONSE']._serialized_start=5139
  _globals['_CHANGEONLYFRIENDSCANSENDGIFTSRESPONSE']._serialized_end=5195
  _globals['_GETSOCIALSUMMARIESWITHPVPRATINGREQUEST']._serialized_start=5197
  _globals['_GETSOCIALSUMMARIESWITHPVPRATINGREQUEST']._serialized_end=5291
  _globals['_GETSOCIALSUMMARIESWITHPVPRATINGRESPONSE']._serialized_start=5294
  _globals['_GETSOCIALSUMMARIESWITHPVPRATINGRESPONSE']._serialized_end=5513
  _globals['_GETSOCIALSUMMARIESWITHPVPRATINGRESPONSE_RATINGSENTRY']._serialized_start=5467
  _globals['_GETSOCIALSUMMARIESWITHPVPRATINGRESPONSE_RATINGSENTRY']._serialized_end=5513
  _globals['_SOCIALSERVICE']._serialized_start=5516
  _globals['_SOCIALSERVICE']._serialized_end=8163
# @@protoc_insertion_point(module_scope)
