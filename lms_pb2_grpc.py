# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import lms_pb2 as lms__pb2

GRPC_GENERATED_VERSION = '1.66.1'
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
        + f' but the generated code in lms_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class LMSServiceStub(object):
    """LMS Service for login, logout, posting, and getting data
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Login = channel.unary_unary(
                '/LMSService/Login',
                request_serializer=lms__pb2.LoginRequest.SerializeToString,
                response_deserializer=lms__pb2.LoginResponse.FromString,
                _registered_method=True)
        self.Logout = channel.unary_unary(
                '/LMSService/Logout',
                request_serializer=lms__pb2.LogoutRequest.SerializeToString,
                response_deserializer=lms__pb2.StatusResponse.FromString,
                _registered_method=True)
        self.Post = channel.unary_unary(
                '/LMSService/Post',
                request_serializer=lms__pb2.PostRequest.SerializeToString,
                response_deserializer=lms__pb2.StatusResponse.FromString,
                _registered_method=True)
        self.Get = channel.unary_unary(
                '/LMSService/Get',
                request_serializer=lms__pb2.GetRequest.SerializeToString,
                response_deserializer=lms__pb2.GetResponse.FromString,
                _registered_method=True)
        self.getLLMAnswer = channel.unary_unary(
                '/LMSService/getLLMAnswer',
                request_serializer=lms__pb2.getLLMAnswerRequest.SerializeToString,
                response_deserializer=lms__pb2.getLLMAnswerResponse.FromString,
                _registered_method=True)


class LMSServiceServicer(object):
    """LMS Service for login, logout, posting, and getting data
    """

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Logout(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Post(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getLLMAnswer(self, request, context):
        """New RPC for LLM-based query response
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LMSServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=lms__pb2.LoginRequest.FromString,
                    response_serializer=lms__pb2.LoginResponse.SerializeToString,
            ),
            'Logout': grpc.unary_unary_rpc_method_handler(
                    servicer.Logout,
                    request_deserializer=lms__pb2.LogoutRequest.FromString,
                    response_serializer=lms__pb2.StatusResponse.SerializeToString,
            ),
            'Post': grpc.unary_unary_rpc_method_handler(
                    servicer.Post,
                    request_deserializer=lms__pb2.PostRequest.FromString,
                    response_serializer=lms__pb2.StatusResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=lms__pb2.GetRequest.FromString,
                    response_serializer=lms__pb2.GetResponse.SerializeToString,
            ),
            'getLLMAnswer': grpc.unary_unary_rpc_method_handler(
                    servicer.getLLMAnswer,
                    request_deserializer=lms__pb2.getLLMAnswerRequest.FromString,
                    response_serializer=lms__pb2.getLLMAnswerResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'LMSService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('LMSService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class LMSService(object):
    """LMS Service for login, logout, posting, and getting data
    """

    @staticmethod
    def Login(request,
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
            '/LMSService/Login',
            lms__pb2.LoginRequest.SerializeToString,
            lms__pb2.LoginResponse.FromString,
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
    def Logout(request,
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
            '/LMSService/Logout',
            lms__pb2.LogoutRequest.SerializeToString,
            lms__pb2.StatusResponse.FromString,
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
    def Post(request,
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
            '/LMSService/Post',
            lms__pb2.PostRequest.SerializeToString,
            lms__pb2.StatusResponse.FromString,
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
    def Get(request,
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
            '/LMSService/Get',
            lms__pb2.GetRequest.SerializeToString,
            lms__pb2.GetResponse.FromString,
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
    def getLLMAnswer(request,
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
            '/LMSService/getLLMAnswer',
            lms__pb2.getLLMAnswerRequest.SerializeToString,
            lms__pb2.getLLMAnswerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class TutoringServerStub(object):
    """Tutoring service for handling LLM queries
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getLLMAnswer = channel.unary_unary(
                '/TutoringServer/getLLMAnswer',
                request_serializer=lms__pb2.getLLMAnswerRequest.SerializeToString,
                response_deserializer=lms__pb2.getLLMAnswerResponse.FromString,
                _registered_method=True)


class TutoringServerServicer(object):
    """Tutoring service for handling LLM queries
    """

    def getLLMAnswer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TutoringServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getLLMAnswer': grpc.unary_unary_rpc_method_handler(
                    servicer.getLLMAnswer,
                    request_deserializer=lms__pb2.getLLMAnswerRequest.FromString,
                    response_serializer=lms__pb2.getLLMAnswerResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TutoringServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('TutoringServer', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TutoringServer(object):
    """Tutoring service for handling LLM queries
    """

    @staticmethod
    def getLLMAnswer(request,
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
            '/TutoringServer/getLLMAnswer',
            lms__pb2.getLLMAnswerRequest.SerializeToString,
            lms__pb2.getLLMAnswerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class LMSRaftServiceStub(object):
    """Raft consensus service to handle leader election and log replication
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RequestVote = channel.unary_unary(
                '/LMSRaftService/RequestVote',
                request_serializer=lms__pb2.RequestVoteRequest.SerializeToString,
                response_deserializer=lms__pb2.RequestVoteReply.FromString,
                _registered_method=True)
        self.AppendEntries = channel.unary_unary(
                '/LMSRaftService/AppendEntries',
                request_serializer=lms__pb2.AppendEntriesRequest.SerializeToString,
                response_deserializer=lms__pb2.AppendEntriesReply.FromString,
                _registered_method=True)
        self.Login = channel.unary_unary(
                '/LMSRaftService/Login',
                request_serializer=lms__pb2.LoginRequest.SerializeToString,
                response_deserializer=lms__pb2.LoginResponse.FromString,
                _registered_method=True)
        self.Logout = channel.unary_unary(
                '/LMSRaftService/Logout',
                request_serializer=lms__pb2.LogoutRequest.SerializeToString,
                response_deserializer=lms__pb2.StatusResponse.FromString,
                _registered_method=True)
        self.Post = channel.unary_unary(
                '/LMSRaftService/Post',
                request_serializer=lms__pb2.PostRequest.SerializeToString,
                response_deserializer=lms__pb2.StatusResponse.FromString,
                _registered_method=True)
        self.Get = channel.unary_unary(
                '/LMSRaftService/Get',
                request_serializer=lms__pb2.GetRequest.SerializeToString,
                response_deserializer=lms__pb2.GetResponse.FromString,
                _registered_method=True)
        self.GetLeader = channel.unary_unary(
                '/LMSRaftService/GetLeader',
                request_serializer=lms__pb2.GetLeaderRequest.SerializeToString,
                response_deserializer=lms__pb2.GetLeaderReply.FromString,
                _registered_method=True)
        self.AddSession = channel.unary_unary(
                '/LMSRaftService/AddSession',
                request_serializer=lms__pb2.AddSessionRequest.SerializeToString,
                response_deserializer=lms__pb2.StatusResponse.FromString,
                _registered_method=True)
        self.ReplicateDataStore = channel.unary_unary(
                '/LMSRaftService/ReplicateDataStore',
                request_serializer=lms__pb2.ReplicateDataStoreRequest.SerializeToString,
                response_deserializer=lms__pb2.StatusResponse.FromString,
                _registered_method=True)


class LMSRaftServiceServicer(object):
    """Raft consensus service to handle leader election and log replication
    """

    def RequestVote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AppendEntries(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Logout(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Post(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLeader(self, request, context):
        """New RPC to get leader information
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplicateDataStore(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LMSRaftServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RequestVote': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestVote,
                    request_deserializer=lms__pb2.RequestVoteRequest.FromString,
                    response_serializer=lms__pb2.RequestVoteReply.SerializeToString,
            ),
            'AppendEntries': grpc.unary_unary_rpc_method_handler(
                    servicer.AppendEntries,
                    request_deserializer=lms__pb2.AppendEntriesRequest.FromString,
                    response_serializer=lms__pb2.AppendEntriesReply.SerializeToString,
            ),
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=lms__pb2.LoginRequest.FromString,
                    response_serializer=lms__pb2.LoginResponse.SerializeToString,
            ),
            'Logout': grpc.unary_unary_rpc_method_handler(
                    servicer.Logout,
                    request_deserializer=lms__pb2.LogoutRequest.FromString,
                    response_serializer=lms__pb2.StatusResponse.SerializeToString,
            ),
            'Post': grpc.unary_unary_rpc_method_handler(
                    servicer.Post,
                    request_deserializer=lms__pb2.PostRequest.FromString,
                    response_serializer=lms__pb2.StatusResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=lms__pb2.GetRequest.FromString,
                    response_serializer=lms__pb2.GetResponse.SerializeToString,
            ),
            'GetLeader': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLeader,
                    request_deserializer=lms__pb2.GetLeaderRequest.FromString,
                    response_serializer=lms__pb2.GetLeaderReply.SerializeToString,
            ),
            'AddSession': grpc.unary_unary_rpc_method_handler(
                    servicer.AddSession,
                    request_deserializer=lms__pb2.AddSessionRequest.FromString,
                    response_serializer=lms__pb2.StatusResponse.SerializeToString,
            ),
            'ReplicateDataStore': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicateDataStore,
                    request_deserializer=lms__pb2.ReplicateDataStoreRequest.FromString,
                    response_serializer=lms__pb2.StatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'LMSRaftService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('LMSRaftService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class LMSRaftService(object):
    """Raft consensus service to handle leader election and log replication
    """

    @staticmethod
    def RequestVote(request,
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
            '/LMSRaftService/RequestVote',
            lms__pb2.RequestVoteRequest.SerializeToString,
            lms__pb2.RequestVoteReply.FromString,
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
    def AppendEntries(request,
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
            '/LMSRaftService/AppendEntries',
            lms__pb2.AppendEntriesRequest.SerializeToString,
            lms__pb2.AppendEntriesReply.FromString,
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
    def Login(request,
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
            '/LMSRaftService/Login',
            lms__pb2.LoginRequest.SerializeToString,
            lms__pb2.LoginResponse.FromString,
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
    def Logout(request,
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
            '/LMSRaftService/Logout',
            lms__pb2.LogoutRequest.SerializeToString,
            lms__pb2.StatusResponse.FromString,
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
    def Post(request,
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
            '/LMSRaftService/Post',
            lms__pb2.PostRequest.SerializeToString,
            lms__pb2.StatusResponse.FromString,
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
    def Get(request,
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
            '/LMSRaftService/Get',
            lms__pb2.GetRequest.SerializeToString,
            lms__pb2.GetResponse.FromString,
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
    def GetLeader(request,
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
            '/LMSRaftService/GetLeader',
            lms__pb2.GetLeaderRequest.SerializeToString,
            lms__pb2.GetLeaderReply.FromString,
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
    def AddSession(request,
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
            '/LMSRaftService/AddSession',
            lms__pb2.AddSessionRequest.SerializeToString,
            lms__pb2.StatusResponse.FromString,
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
    def ReplicateDataStore(request,
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
            '/LMSRaftService/ReplicateDataStore',
            lms__pb2.ReplicateDataStoreRequest.SerializeToString,
            lms__pb2.StatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
