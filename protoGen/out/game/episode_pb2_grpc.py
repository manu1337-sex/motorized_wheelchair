# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import prot.game.episode_pb2 as game_dot_episode__pb2

GRPC_GENERATED_VERSION = '1.66.2'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in game/episode_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class EpisodeServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ClearNode = channel.unary_unary(
                '/ck.game.EpisodeService/ClearNode',
                request_serializer=game_dot_episode__pb2.ClearNodeRequest.SerializeToString,
                response_deserializer=game_dot_episode__pb2.ClearNodeResponse.FromString,
                _registered_method=True)
        self.SelectBranch = channel.unary_unary(
                '/ck.game.EpisodeService/SelectBranch',
                request_serializer=game_dot_episode__pb2.SelectBranchRequest.SerializeToString,
                response_deserializer=game_dot_episode__pb2.SelectBranchResponse.FromString,
                _registered_method=True)
        self.CompleteLandNode = channel.unary_unary(
                '/ck.game.EpisodeService/CompleteLandNode',
                request_serializer=game_dot_episode__pb2.CompleteLandNodeRequest.SerializeToString,
                response_deserializer=game_dot_episode__pb2.CompleteLandNodeResponse.FromString,
                _registered_method=True)
        self.ReceiveAccumulatedStarReward = channel.unary_unary(
                '/ck.game.EpisodeService/ReceiveAccumulatedStarReward',
                request_serializer=game_dot_episode__pb2.ReceiveAccumulatedStarRewardRequest.SerializeToString,
                response_deserializer=game_dot_episode__pb2.ReceiveAccumulatedStarRewardResponse.FromString,
                _registered_method=True)
        self.UnlockEpisodeGroupCollectionEntry = channel.unary_unary(
                '/ck.game.EpisodeService/UnlockEpisodeGroupCollectionEntry',
                request_serializer=game_dot_episode__pb2.UnlockEpisodeGroupCollectionEntryRequest.SerializeToString,
                response_deserializer=game_dot_episode__pb2.UnlockEpisodeGroupCollectionEntryResponse.FromString,
                _registered_method=True)
        self.CompleteEpisodeGroupCollection = channel.unary_unary(
                '/ck.game.EpisodeService/CompleteEpisodeGroupCollection',
                request_serializer=game_dot_episode__pb2.CompleteEpisodeGroupCollectionRequest.SerializeToString,
                response_deserializer=game_dot_episode__pb2.CompleteEpisodeGroupCollectionResponse.FromString,
                _registered_method=True)
        self.ClearStoryCollectionBookMission = channel.unary_unary(
                '/ck.game.EpisodeService/ClearStoryCollectionBookMission',
                request_serializer=game_dot_episode__pb2.ClearStoryCollectionBookMissionRequest.SerializeToString,
                response_deserializer=game_dot_episode__pb2.ClearStoryCollectionBookMissionResponse.FromString,
                _registered_method=True)
        self.OpenEpisodeGroup = channel.unary_unary(
                '/ck.game.EpisodeService/OpenEpisodeGroup',
                request_serializer=game_dot_episode__pb2.OpenEpisodeGroupRequest.SerializeToString,
                response_deserializer=game_dot_episode__pb2.OpenEpisodeGroupResponse.FromString,
                _registered_method=True)
        self.UpdateEpisodeLandMutation = channel.unary_unary(
                '/ck.game.EpisodeService/UpdateEpisodeLandMutation',
                request_serializer=game_dot_episode__pb2.UpdateEpisodeLandMutationRequest.SerializeToString,
                response_deserializer=game_dot_episode__pb2.UpdateEpisodeLandMutationResponse.FromString,
                _registered_method=True)


class EpisodeServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ClearNode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SelectBranch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CompleteLandNode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReceiveAccumulatedStarReward(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnlockEpisodeGroupCollectionEntry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CompleteEpisodeGroupCollection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearStoryCollectionBookMission(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OpenEpisodeGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateEpisodeLandMutation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EpisodeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ClearNode': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearNode,
                    request_deserializer=game_dot_episode__pb2.ClearNodeRequest.FromString,
                    response_serializer=game_dot_episode__pb2.ClearNodeResponse.SerializeToString,
            ),
            'SelectBranch': grpc.unary_unary_rpc_method_handler(
                    servicer.SelectBranch,
                    request_deserializer=game_dot_episode__pb2.SelectBranchRequest.FromString,
                    response_serializer=game_dot_episode__pb2.SelectBranchResponse.SerializeToString,
            ),
            'CompleteLandNode': grpc.unary_unary_rpc_method_handler(
                    servicer.CompleteLandNode,
                    request_deserializer=game_dot_episode__pb2.CompleteLandNodeRequest.FromString,
                    response_serializer=game_dot_episode__pb2.CompleteLandNodeResponse.SerializeToString,
            ),
            'ReceiveAccumulatedStarReward': grpc.unary_unary_rpc_method_handler(
                    servicer.ReceiveAccumulatedStarReward,
                    request_deserializer=game_dot_episode__pb2.ReceiveAccumulatedStarRewardRequest.FromString,
                    response_serializer=game_dot_episode__pb2.ReceiveAccumulatedStarRewardResponse.SerializeToString,
            ),
            'UnlockEpisodeGroupCollectionEntry': grpc.unary_unary_rpc_method_handler(
                    servicer.UnlockEpisodeGroupCollectionEntry,
                    request_deserializer=game_dot_episode__pb2.UnlockEpisodeGroupCollectionEntryRequest.FromString,
                    response_serializer=game_dot_episode__pb2.UnlockEpisodeGroupCollectionEntryResponse.SerializeToString,
            ),
            'CompleteEpisodeGroupCollection': grpc.unary_unary_rpc_method_handler(
                    servicer.CompleteEpisodeGroupCollection,
                    request_deserializer=game_dot_episode__pb2.CompleteEpisodeGroupCollectionRequest.FromString,
                    response_serializer=game_dot_episode__pb2.CompleteEpisodeGroupCollectionResponse.SerializeToString,
            ),
            'ClearStoryCollectionBookMission': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearStoryCollectionBookMission,
                    request_deserializer=game_dot_episode__pb2.ClearStoryCollectionBookMissionRequest.FromString,
                    response_serializer=game_dot_episode__pb2.ClearStoryCollectionBookMissionResponse.SerializeToString,
            ),
            'OpenEpisodeGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.OpenEpisodeGroup,
                    request_deserializer=game_dot_episode__pb2.OpenEpisodeGroupRequest.FromString,
                    response_serializer=game_dot_episode__pb2.OpenEpisodeGroupResponse.SerializeToString,
            ),
            'UpdateEpisodeLandMutation': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateEpisodeLandMutation,
                    request_deserializer=game_dot_episode__pb2.UpdateEpisodeLandMutationRequest.FromString,
                    response_serializer=game_dot_episode__pb2.UpdateEpisodeLandMutationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ck.game.EpisodeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ck.game.EpisodeService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class EpisodeService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ClearNode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ck.game.EpisodeService/ClearNode',
            game_dot_episode__pb2.ClearNodeRequest.SerializeToString,
            game_dot_episode__pb2.ClearNodeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SelectBranch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ck.game.EpisodeService/SelectBranch',
            game_dot_episode__pb2.SelectBranchRequest.SerializeToString,
            game_dot_episode__pb2.SelectBranchResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CompleteLandNode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ck.game.EpisodeService/CompleteLandNode',
            game_dot_episode__pb2.CompleteLandNodeRequest.SerializeToString,
            game_dot_episode__pb2.CompleteLandNodeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ReceiveAccumulatedStarReward(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ck.game.EpisodeService/ReceiveAccumulatedStarReward',
            game_dot_episode__pb2.ReceiveAccumulatedStarRewardRequest.SerializeToString,
            game_dot_episode__pb2.ReceiveAccumulatedStarRewardResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UnlockEpisodeGroupCollectionEntry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ck.game.EpisodeService/UnlockEpisodeGroupCollectionEntry',
            game_dot_episode__pb2.UnlockEpisodeGroupCollectionEntryRequest.SerializeToString,
            game_dot_episode__pb2.UnlockEpisodeGroupCollectionEntryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CompleteEpisodeGroupCollection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ck.game.EpisodeService/CompleteEpisodeGroupCollection',
            game_dot_episode__pb2.CompleteEpisodeGroupCollectionRequest.SerializeToString,
            game_dot_episode__pb2.CompleteEpisodeGroupCollectionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ClearStoryCollectionBookMission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ck.game.EpisodeService/ClearStoryCollectionBookMission',
            game_dot_episode__pb2.ClearStoryCollectionBookMissionRequest.SerializeToString,
            game_dot_episode__pb2.ClearStoryCollectionBookMissionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def OpenEpisodeGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ck.game.EpisodeService/OpenEpisodeGroup',
            game_dot_episode__pb2.OpenEpisodeGroupRequest.SerializeToString,
            game_dot_episode__pb2.OpenEpisodeGroupResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateEpisodeLandMutation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ck.game.EpisodeService/UpdateEpisodeLandMutation',
            game_dot_episode__pb2.UpdateEpisodeLandMutationRequest.SerializeToString,
            game_dot_episode__pb2.UpdateEpisodeLandMutationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
