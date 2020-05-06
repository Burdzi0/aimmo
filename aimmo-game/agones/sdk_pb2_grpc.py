# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from agones import sdk_pb2 as sdk__pb2


class SDKStub(object):
    """SDK service to be used in the GameServer SDK to the Pod Sidecar
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ready = channel.unary_unary(
            "/agones.dev.sdk.SDK/Ready",
            request_serializer=sdk__pb2.Empty.SerializeToString,
            response_deserializer=sdk__pb2.Empty.FromString,
        )
        self.Allocate = channel.unary_unary(
            "/agones.dev.sdk.SDK/Allocate",
            request_serializer=sdk__pb2.Empty.SerializeToString,
            response_deserializer=sdk__pb2.Empty.FromString,
        )
        self.Shutdown = channel.unary_unary(
            "/agones.dev.sdk.SDK/Shutdown",
            request_serializer=sdk__pb2.Empty.SerializeToString,
            response_deserializer=sdk__pb2.Empty.FromString,
        )
        self.Health = channel.stream_unary(
            "/agones.dev.sdk.SDK/Health",
            request_serializer=sdk__pb2.Empty.SerializeToString,
            response_deserializer=sdk__pb2.Empty.FromString,
        )
        self.GetGameServer = channel.unary_unary(
            "/agones.dev.sdk.SDK/GetGameServer",
            request_serializer=sdk__pb2.Empty.SerializeToString,
            response_deserializer=sdk__pb2.GameServer.FromString,
        )
        self.WatchGameServer = channel.unary_stream(
            "/agones.dev.sdk.SDK/WatchGameServer",
            request_serializer=sdk__pb2.Empty.SerializeToString,
            response_deserializer=sdk__pb2.GameServer.FromString,
        )
        self.SetLabel = channel.unary_unary(
            "/agones.dev.sdk.SDK/SetLabel",
            request_serializer=sdk__pb2.KeyValue.SerializeToString,
            response_deserializer=sdk__pb2.Empty.FromString,
        )
        self.SetAnnotation = channel.unary_unary(
            "/agones.dev.sdk.SDK/SetAnnotation",
            request_serializer=sdk__pb2.KeyValue.SerializeToString,
            response_deserializer=sdk__pb2.Empty.FromString,
        )
        self.Reserve = channel.unary_unary(
            "/agones.dev.sdk.SDK/Reserve",
            request_serializer=sdk__pb2.Duration.SerializeToString,
            response_deserializer=sdk__pb2.Empty.FromString,
        )


class SDKServicer(object):
    """SDK service to be used in the GameServer SDK to the Pod Sidecar
    """

    def Ready(self, request, context):
        """Call when the GameServer is ready
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Allocate(self, request, context):
        """Call to self Allocation the GameServer
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Shutdown(self, request, context):
        """Call when the GameServer is shutting down
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Health(self, request_iterator, context):
        """Send a Empty every d Duration to declare that this GameSever is healthy
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetGameServer(self, request, context):
        """Retrieve the current GameServer data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def WatchGameServer(self, request, context):
        """Send GameServer details whenever the GameServer is updated
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SetLabel(self, request, context):
        """Apply a Label to the backing GameServer metadata
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SetAnnotation(self, request, context):
        """Apply a Annotation to the backing GameServer metadata
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Reserve(self, request, context):
        """Marks the GameServer as the Reserved state for Duration
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_SDKServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Ready": grpc.unary_unary_rpc_method_handler(
            servicer.Ready,
            request_deserializer=sdk__pb2.Empty.FromString,
            response_serializer=sdk__pb2.Empty.SerializeToString,
        ),
        "Allocate": grpc.unary_unary_rpc_method_handler(
            servicer.Allocate,
            request_deserializer=sdk__pb2.Empty.FromString,
            response_serializer=sdk__pb2.Empty.SerializeToString,
        ),
        "Shutdown": grpc.unary_unary_rpc_method_handler(
            servicer.Shutdown,
            request_deserializer=sdk__pb2.Empty.FromString,
            response_serializer=sdk__pb2.Empty.SerializeToString,
        ),
        "Health": grpc.stream_unary_rpc_method_handler(
            servicer.Health,
            request_deserializer=sdk__pb2.Empty.FromString,
            response_serializer=sdk__pb2.Empty.SerializeToString,
        ),
        "GetGameServer": grpc.unary_unary_rpc_method_handler(
            servicer.GetGameServer,
            request_deserializer=sdk__pb2.Empty.FromString,
            response_serializer=sdk__pb2.GameServer.SerializeToString,
        ),
        "WatchGameServer": grpc.unary_stream_rpc_method_handler(
            servicer.WatchGameServer,
            request_deserializer=sdk__pb2.Empty.FromString,
            response_serializer=sdk__pb2.GameServer.SerializeToString,
        ),
        "SetLabel": grpc.unary_unary_rpc_method_handler(
            servicer.SetLabel,
            request_deserializer=sdk__pb2.KeyValue.FromString,
            response_serializer=sdk__pb2.Empty.SerializeToString,
        ),
        "SetAnnotation": grpc.unary_unary_rpc_method_handler(
            servicer.SetAnnotation,
            request_deserializer=sdk__pb2.KeyValue.FromString,
            response_serializer=sdk__pb2.Empty.SerializeToString,
        ),
        "Reserve": grpc.unary_unary_rpc_method_handler(
            servicer.Reserve,
            request_deserializer=sdk__pb2.Duration.FromString,
            response_serializer=sdk__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "agones.dev.sdk.SDK", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class SDK(object):
    """SDK service to be used in the GameServer SDK to the Pod Sidecar
    """

    @staticmethod
    def Ready(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/agones.dev.sdk.SDK/Ready",
            sdk__pb2.Empty.SerializeToString,
            sdk__pb2.Empty.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Allocate(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/agones.dev.sdk.SDK/Allocate",
            sdk__pb2.Empty.SerializeToString,
            sdk__pb2.Empty.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Shutdown(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/agones.dev.sdk.SDK/Shutdown",
            sdk__pb2.Empty.SerializeToString,
            sdk__pb2.Empty.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Health(
        request_iterator,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.stream_unary(
            request_iterator,
            target,
            "/agones.dev.sdk.SDK/Health",
            sdk__pb2.Empty.SerializeToString,
            sdk__pb2.Empty.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetGameServer(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/agones.dev.sdk.SDK/GetGameServer",
            sdk__pb2.Empty.SerializeToString,
            sdk__pb2.GameServer.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def WatchGameServer(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/agones.dev.sdk.SDK/WatchGameServer",
            sdk__pb2.Empty.SerializeToString,
            sdk__pb2.GameServer.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SetLabel(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/agones.dev.sdk.SDK/SetLabel",
            sdk__pb2.KeyValue.SerializeToString,
            sdk__pb2.Empty.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SetAnnotation(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/agones.dev.sdk.SDK/SetAnnotation",
            sdk__pb2.KeyValue.SerializeToString,
            sdk__pb2.Empty.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Reserve(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/agones.dev.sdk.SDK/Reserve",
            sdk__pb2.Duration.SerializeToString,
            sdk__pb2.Empty.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
