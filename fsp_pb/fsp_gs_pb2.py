# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fsp-gs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import fsp_common_pb2 as fsp__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fsp-gs.proto',
  package='com.fsmeeting.fsp.proto.gs',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x66sp-gs.proto\x12\x1a\x63om.fsmeeting.fsp.proto.gs\x1a\x10\x66sp-common.proto\"\x99\x02\n\x13NotifyPublishStream\x12\x11\n\tstream_id\x18\x01 \x01(\t\x12\x1c\n\x14stream_publish_token\x18\x02 \x01(\t\x12\x10\n\x08group_id\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\t\x12\x10\n\x08media_id\x18\x05 \x01(\x05\x12=\n\nmedia_type\x18\x06 \x01(\x0e\x32).com.fsmeeting.fsp.proto.common.MediaType\x12J\n\x10\x63ommonInvokeInfo\x18\x07 \x01(\x0b\x32\x30.com.fsmeeting.fsp.proto.common.CommonInvokeInfo\x12\x11\n\tmedia_id2\x18\x08 \x01(\t\"Z\n\x16NotifyPublishStreamRsp\x12@\n\x08response\x18\x01 \x01(\x0b\x32..com.fsmeeting.fsp.proto.common.CommonResponse\"\x91\x01\n\x18NotifyStreamSendingStart\x12\x16\n\x0erecv_client_id\x18\x01 \x01(\t\x12\x11\n\tstream_id\x18\x02 \x01(\t\x12J\n\x10\x63ommonInvokeInfo\x18\x03 \x01(\x0b\x32\x30.com.fsmeeting.fsp.proto.common.CommonInvokeInfo\"_\n\x1bNotifyStreamSendingStartRsp\x12@\n\x08response\x18\x01 \x01(\x0b\x32..com.fsmeeting.fsp.proto.common.CommonResponse\"D\n\x17NotifyStreamSendingStop\x12\x11\n\tstream_id\x18\x01 \x01(\t\x12\x16\n\x0erecv_client_id\x18\x02 \x01(\t\"^\n\x1aNotifyStreamSendingStopRsp\x12@\n\x08response\x18\x01 \x01(\x0b\x32..com.fsmeeting.fsp.proto.common.CommonResponse\"\xc9\x01\n\x18NotifySelectStreamServer\x12\x11\n\tstream_id\x18\x01 \x01(\t\x12\x13\n\x0b\x63onnect_str\x18\x02 \x01(\t\x12\x11\n\tpub_token\x18\x03 \x01(\t\x12\x10\n\x08group_id\x18\x04 \x01(\t\x12\x0f\n\x07user_id\x18\x05 \x01(\t\x12=\n\nmedia_type\x18\x06 \x01(\x0e\x32).com.fsmeeting.fsp.proto.common.MediaType\x12\x10\n\x08media_id\x18\x07 \x01(\t\"_\n\x1bNotifySelectStreamServerRsp\x12@\n\x08response\x18\x01 \x01(\x0b\x32..com.fsmeeting.fsp.proto.common.CommonResponse\"\xa6\x01\n\x1dNotifyCleanStreamSourceServer\x12\x11\n\tstream_id\x18\x01 \x01(\t\x12\x10\n\x08group_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12=\n\nmedia_type\x18\x04 \x01(\x0e\x32).com.fsmeeting.fsp.proto.common.MediaType\x12\x10\n\x08media_id\x18\x05 \x01(\t\"d\n NotifyCleanStreamSourceServerRsp\x12@\n\x08response\x18\x01 \x01(\x0b\x32..com.fsmeeting.fsp.proto.common.CommonResponse*\xa1\x03\n\x0fProtoDictionary\x12\x19\n\x15\x45num2UnknownInterface\x10\x00\x12\x1d\n\x18\x45num2NotifyPublishStream\x10\xa0\x1f\x12 \n\x1b\x45num2NotifyPublishStreamRsp\x10\xa1\x1f\x12\"\n\x1d\x45num2NotifyStreamSendingStart\x10\xa2\x1f\x12%\n Enum2NotifyStreamSendingStartRsp\x10\xa3\x1f\x12!\n\x1c\x45num2NotifyStreamSendingStop\x10\xa4\x1f\x12$\n\x1f\x45num2NotifyStreamSendingStopRsp\x10\xa5\x1f\x12\"\n\x1d\x45num2NotifySelectStreamServer\x10\xa6\x1f\x12%\n Enum2NotifySelectStreamServerRsp\x10\xa7\x1f\x12\'\n\"Enum2NotifyCleanStreamSourceServer\x10\xa8\x1f\x12*\n%Enum2NotifyCleanStreamSourceServerRsp\x10\xa9\x1f\x42\'\n\x1a\x63om.fsmeeting.fsp.proto.gsP\x01\xf8\x01\x01\xa2\x02\x03GPBb\x06proto3')
  ,
  dependencies=[fsp__common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_PROTODICTIONARY = _descriptor.EnumDescriptor(
  name='ProtoDictionary',
  full_name='com.fsmeeting.fsp.proto.gs.ProtoDictionary',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Enum2UnknownInterface', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2NotifyPublishStream', index=1, number=4000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2NotifyPublishStreamRsp', index=2, number=4001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2NotifyStreamSendingStart', index=3, number=4002,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2NotifyStreamSendingStartRsp', index=4, number=4003,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2NotifyStreamSendingStop', index=5, number=4004,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2NotifyStreamSendingStopRsp', index=6, number=4005,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2NotifySelectStreamServer', index=7, number=4006,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2NotifySelectStreamServerRsp', index=8, number=4007,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2NotifyCleanStreamSourceServer', index=9, number=4008,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2NotifyCleanStreamSourceServerRsp', index=10, number=4009,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1422,
  serialized_end=1839,
)
_sym_db.RegisterEnumDescriptor(_PROTODICTIONARY)

ProtoDictionary = enum_type_wrapper.EnumTypeWrapper(_PROTODICTIONARY)
Enum2UnknownInterface = 0
Enum2NotifyPublishStream = 4000
Enum2NotifyPublishStreamRsp = 4001
Enum2NotifyStreamSendingStart = 4002
Enum2NotifyStreamSendingStartRsp = 4003
Enum2NotifyStreamSendingStop = 4004
Enum2NotifyStreamSendingStopRsp = 4005
Enum2NotifySelectStreamServer = 4006
Enum2NotifySelectStreamServerRsp = 4007
Enum2NotifyCleanStreamSourceServer = 4008
Enum2NotifyCleanStreamSourceServerRsp = 4009



_NOTIFYPUBLISHSTREAM = _descriptor.Descriptor(
  name='NotifyPublishStream',
  full_name='com.fsmeeting.fsp.proto.gs.NotifyPublishStream',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream_id', full_name='com.fsmeeting.fsp.proto.gs.NotifyPublishStream.stream_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stream_publish_token', full_name='com.fsmeeting.fsp.proto.gs.NotifyPublishStream.stream_publish_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_id', full_name='com.fsmeeting.fsp.proto.gs.NotifyPublishStream.group_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='com.fsmeeting.fsp.proto.gs.NotifyPublishStream.user_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='media_id', full_name='com.fsmeeting.fsp.proto.gs.NotifyPublishStream.media_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='media_type', full_name='com.fsmeeting.fsp.proto.gs.NotifyPublishStream.media_type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='commonInvokeInfo', full_name='com.fsmeeting.fsp.proto.gs.NotifyPublishStream.commonInvokeInfo', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='media_id2', full_name='com.fsmeeting.fsp.proto.gs.NotifyPublishStream.media_id2', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=344,
)


_NOTIFYPUBLISHSTREAMRSP = _descriptor.Descriptor(
  name='NotifyPublishStreamRsp',
  full_name='com.fsmeeting.fsp.proto.gs.NotifyPublishStreamRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='com.fsmeeting.fsp.proto.gs.NotifyPublishStreamRsp.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=346,
  serialized_end=436,
)


_NOTIFYSTREAMSENDINGSTART = _descriptor.Descriptor(
  name='NotifyStreamSendingStart',
  full_name='com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='recv_client_id', full_name='com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStart.recv_client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stream_id', full_name='com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStart.stream_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='commonInvokeInfo', full_name='com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStart.commonInvokeInfo', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=439,
  serialized_end=584,
)


_NOTIFYSTREAMSENDINGSTARTRSP = _descriptor.Descriptor(
  name='NotifyStreamSendingStartRsp',
  full_name='com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStartRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStartRsp.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=586,
  serialized_end=681,
)


_NOTIFYSTREAMSENDINGSTOP = _descriptor.Descriptor(
  name='NotifyStreamSendingStop',
  full_name='com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream_id', full_name='com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStop.stream_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recv_client_id', full_name='com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStop.recv_client_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=683,
  serialized_end=751,
)


_NOTIFYSTREAMSENDINGSTOPRSP = _descriptor.Descriptor(
  name='NotifyStreamSendingStopRsp',
  full_name='com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStopRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStopRsp.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=753,
  serialized_end=847,
)


_NOTIFYSELECTSTREAMSERVER = _descriptor.Descriptor(
  name='NotifySelectStreamServer',
  full_name='com.fsmeeting.fsp.proto.gs.NotifySelectStreamServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream_id', full_name='com.fsmeeting.fsp.proto.gs.NotifySelectStreamServer.stream_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='connect_str', full_name='com.fsmeeting.fsp.proto.gs.NotifySelectStreamServer.connect_str', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pub_token', full_name='com.fsmeeting.fsp.proto.gs.NotifySelectStreamServer.pub_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_id', full_name='com.fsmeeting.fsp.proto.gs.NotifySelectStreamServer.group_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='com.fsmeeting.fsp.proto.gs.NotifySelectStreamServer.user_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='media_type', full_name='com.fsmeeting.fsp.proto.gs.NotifySelectStreamServer.media_type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='media_id', full_name='com.fsmeeting.fsp.proto.gs.NotifySelectStreamServer.media_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=850,
  serialized_end=1051,
)


_NOTIFYSELECTSTREAMSERVERRSP = _descriptor.Descriptor(
  name='NotifySelectStreamServerRsp',
  full_name='com.fsmeeting.fsp.proto.gs.NotifySelectStreamServerRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='com.fsmeeting.fsp.proto.gs.NotifySelectStreamServerRsp.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1053,
  serialized_end=1148,
)


_NOTIFYCLEANSTREAMSOURCESERVER = _descriptor.Descriptor(
  name='NotifyCleanStreamSourceServer',
  full_name='com.fsmeeting.fsp.proto.gs.NotifyCleanStreamSourceServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream_id', full_name='com.fsmeeting.fsp.proto.gs.NotifyCleanStreamSourceServer.stream_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_id', full_name='com.fsmeeting.fsp.proto.gs.NotifyCleanStreamSourceServer.group_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='com.fsmeeting.fsp.proto.gs.NotifyCleanStreamSourceServer.user_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='media_type', full_name='com.fsmeeting.fsp.proto.gs.NotifyCleanStreamSourceServer.media_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='media_id', full_name='com.fsmeeting.fsp.proto.gs.NotifyCleanStreamSourceServer.media_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1151,
  serialized_end=1317,
)


_NOTIFYCLEANSTREAMSOURCESERVERRSP = _descriptor.Descriptor(
  name='NotifyCleanStreamSourceServerRsp',
  full_name='com.fsmeeting.fsp.proto.gs.NotifyCleanStreamSourceServerRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='com.fsmeeting.fsp.proto.gs.NotifyCleanStreamSourceServerRsp.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1319,
  serialized_end=1419,
)

_NOTIFYPUBLISHSTREAM.fields_by_name['media_type'].enum_type = fsp__common__pb2._MEDIATYPE
_NOTIFYPUBLISHSTREAM.fields_by_name['commonInvokeInfo'].message_type = fsp__common__pb2._COMMONINVOKEINFO
_NOTIFYPUBLISHSTREAMRSP.fields_by_name['response'].message_type = fsp__common__pb2._COMMONRESPONSE
_NOTIFYSTREAMSENDINGSTART.fields_by_name['commonInvokeInfo'].message_type = fsp__common__pb2._COMMONINVOKEINFO
_NOTIFYSTREAMSENDINGSTARTRSP.fields_by_name['response'].message_type = fsp__common__pb2._COMMONRESPONSE
_NOTIFYSTREAMSENDINGSTOPRSP.fields_by_name['response'].message_type = fsp__common__pb2._COMMONRESPONSE
_NOTIFYSELECTSTREAMSERVER.fields_by_name['media_type'].enum_type = fsp__common__pb2._MEDIATYPE
_NOTIFYSELECTSTREAMSERVERRSP.fields_by_name['response'].message_type = fsp__common__pb2._COMMONRESPONSE
_NOTIFYCLEANSTREAMSOURCESERVER.fields_by_name['media_type'].enum_type = fsp__common__pb2._MEDIATYPE
_NOTIFYCLEANSTREAMSOURCESERVERRSP.fields_by_name['response'].message_type = fsp__common__pb2._COMMONRESPONSE
DESCRIPTOR.message_types_by_name['NotifyPublishStream'] = _NOTIFYPUBLISHSTREAM
DESCRIPTOR.message_types_by_name['NotifyPublishStreamRsp'] = _NOTIFYPUBLISHSTREAMRSP
DESCRIPTOR.message_types_by_name['NotifyStreamSendingStart'] = _NOTIFYSTREAMSENDINGSTART
DESCRIPTOR.message_types_by_name['NotifyStreamSendingStartRsp'] = _NOTIFYSTREAMSENDINGSTARTRSP
DESCRIPTOR.message_types_by_name['NotifyStreamSendingStop'] = _NOTIFYSTREAMSENDINGSTOP
DESCRIPTOR.message_types_by_name['NotifyStreamSendingStopRsp'] = _NOTIFYSTREAMSENDINGSTOPRSP
DESCRIPTOR.message_types_by_name['NotifySelectStreamServer'] = _NOTIFYSELECTSTREAMSERVER
DESCRIPTOR.message_types_by_name['NotifySelectStreamServerRsp'] = _NOTIFYSELECTSTREAMSERVERRSP
DESCRIPTOR.message_types_by_name['NotifyCleanStreamSourceServer'] = _NOTIFYCLEANSTREAMSOURCESERVER
DESCRIPTOR.message_types_by_name['NotifyCleanStreamSourceServerRsp'] = _NOTIFYCLEANSTREAMSOURCESERVERRSP
DESCRIPTOR.enum_types_by_name['ProtoDictionary'] = _PROTODICTIONARY

NotifyPublishStream = _reflection.GeneratedProtocolMessageType('NotifyPublishStream', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYPUBLISHSTREAM,
  __module__ = 'fsp_gs_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.gs.NotifyPublishStream)
  ))
_sym_db.RegisterMessage(NotifyPublishStream)

NotifyPublishStreamRsp = _reflection.GeneratedProtocolMessageType('NotifyPublishStreamRsp', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYPUBLISHSTREAMRSP,
  __module__ = 'fsp_gs_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.gs.NotifyPublishStreamRsp)
  ))
_sym_db.RegisterMessage(NotifyPublishStreamRsp)

NotifyStreamSendingStart = _reflection.GeneratedProtocolMessageType('NotifyStreamSendingStart', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYSTREAMSENDINGSTART,
  __module__ = 'fsp_gs_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStart)
  ))
_sym_db.RegisterMessage(NotifyStreamSendingStart)

NotifyStreamSendingStartRsp = _reflection.GeneratedProtocolMessageType('NotifyStreamSendingStartRsp', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYSTREAMSENDINGSTARTRSP,
  __module__ = 'fsp_gs_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStartRsp)
  ))
_sym_db.RegisterMessage(NotifyStreamSendingStartRsp)

NotifyStreamSendingStop = _reflection.GeneratedProtocolMessageType('NotifyStreamSendingStop', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYSTREAMSENDINGSTOP,
  __module__ = 'fsp_gs_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStop)
  ))
_sym_db.RegisterMessage(NotifyStreamSendingStop)

NotifyStreamSendingStopRsp = _reflection.GeneratedProtocolMessageType('NotifyStreamSendingStopRsp', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYSTREAMSENDINGSTOPRSP,
  __module__ = 'fsp_gs_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStopRsp)
  ))
_sym_db.RegisterMessage(NotifyStreamSendingStopRsp)

NotifySelectStreamServer = _reflection.GeneratedProtocolMessageType('NotifySelectStreamServer', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYSELECTSTREAMSERVER,
  __module__ = 'fsp_gs_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.gs.NotifySelectStreamServer)
  ))
_sym_db.RegisterMessage(NotifySelectStreamServer)

NotifySelectStreamServerRsp = _reflection.GeneratedProtocolMessageType('NotifySelectStreamServerRsp', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYSELECTSTREAMSERVERRSP,
  __module__ = 'fsp_gs_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.gs.NotifySelectStreamServerRsp)
  ))
_sym_db.RegisterMessage(NotifySelectStreamServerRsp)

NotifyCleanStreamSourceServer = _reflection.GeneratedProtocolMessageType('NotifyCleanStreamSourceServer', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYCLEANSTREAMSOURCESERVER,
  __module__ = 'fsp_gs_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.gs.NotifyCleanStreamSourceServer)
  ))
_sym_db.RegisterMessage(NotifyCleanStreamSourceServer)

NotifyCleanStreamSourceServerRsp = _reflection.GeneratedProtocolMessageType('NotifyCleanStreamSourceServerRsp', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYCLEANSTREAMSOURCESERVERRSP,
  __module__ = 'fsp_gs_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.gs.NotifyCleanStreamSourceServerRsp)
  ))
_sym_db.RegisterMessage(NotifyCleanStreamSourceServerRsp)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032com.fsmeeting.fsp.proto.gsP\001\370\001\001\242\002\003GPB'))
# @@protoc_insertion_point(module_scope)
