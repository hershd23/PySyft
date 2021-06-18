# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/pycolab/observation.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.lib.numpy import array_pb2 as proto_dot_lib_dot_numpy_dot_array__pb2
from syft.proto.lib.python import dict_pb2 as proto_dot_lib_dot_python_dot_dict__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/pycolab/observation.proto",
    package="",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n#proto/lib/pycolab/observation.proto\x1a\x1bproto/lib/numpy/array.proto\x1a\x1bproto/lib/python/dict.proto"_\n\x0bObservation\x12)\n\x05\x62oard\x18\x01 \x01(\x0b\x32\x1a.syft.lib.numpy.NumpyProto\x12%\n\x06layers\x18\x02 \x01(\x0b\x32\x15.syft.lib.python.Dictb\x06proto3',
    dependencies=[
        proto_dot_lib_dot_numpy_dot_array__pb2.DESCRIPTOR,
        proto_dot_lib_dot_python_dot_dict__pb2.DESCRIPTOR,
    ],
)


_OBSERVATION = _descriptor.Descriptor(
    name="Observation",
    full_name="Observation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="board",
            full_name="Observation.board",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="layers",
            full_name="Observation.layers",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=97,
    serialized_end=192,
)

_OBSERVATION.fields_by_name[
    "board"
].message_type = proto_dot_lib_dot_numpy_dot_array__pb2._NUMPYPROTO
_OBSERVATION.fields_by_name[
    "layers"
].message_type = proto_dot_lib_dot_python_dot_dict__pb2._DICT
DESCRIPTOR.message_types_by_name["Observation"] = _OBSERVATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Observation = _reflection.GeneratedProtocolMessageType(
    "Observation",
    (_message.Message,),
    {
        "DESCRIPTOR": _OBSERVATION,
        "__module__": "proto.lib.pycolab.observation_pb2"
        # @@protoc_insertion_point(class_scope:Observation)
    },
)
_sym_db.RegisterMessage(Observation)


# @@protoc_insertion_point(module_scope)
