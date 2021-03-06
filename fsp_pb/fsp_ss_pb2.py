# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fsp-ss.proto

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
  name='fsp-ss.proto',
  package='com.fsmeeting.fsp.proto.ss',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x66sp-ss.proto\x12\x1a\x63om.fsmeeting.fsp.proto.ss\x1a\x10\x66sp-common.proto\"\xac\x01\n\x15LoginReceivingChannel\x12\x11\n\tstream_id\x18\x01 \x01(\t\x12\x1e\n\x16stream_subscribe_token\x18\x02 \x01(\t\x12\x14\n\x0c\x63lient_token\x18\x03 \x01(\t\x12J\n\x10\x63ommonInvokeInfo\x18\x04 \x01(\x0b\x32\x30.com.fsmeeting.fsp.proto.common.CommonInvokeInfo\"\x08\n\x06Logout\"M\n\tLogoutRsp\x12@\n\x08response\x18\x01 \x01(\x0b\x32..com.fsmeeting.fsp.proto.common.CommonResponse\"\\\n\x18LoginReceivingChannelRsp\x12@\n\x08response\x18\x01 \x01(\x0b\x32..com.fsmeeting.fsp.proto.common.CommonResponse\"\\\n\x13LoginSendingChannel\x12\x11\n\tstream_id\x18\x01 \x01(\t\x12\x1c\n\x14stream_publish_token\x18\x02 \x01(\t\x12\x14\n\x0c\x63lient_token\x18\x03 \x01(\t\"m\n\x16LoginSendingChannelRsp\x12@\n\x08response\x18\x01 \x01(\x0b\x32..com.fsmeeting.fsp.proto.common.CommonResponse\x12\x11\n\tclient_id\x18\x02 \x01(\t\"\x91\x01\n\x18NotifyStreamSendingStart\x12\x16\n\x0erecv_client_id\x18\x01 \x01(\t\x12\x11\n\tstream_id\x18\x02 \x01(\t\x12J\n\x10\x63ommonInvokeInfo\x18\x03 \x01(\x0b\x32\x30.com.fsmeeting.fsp.proto.common.CommonInvokeInfo\"_\n\x1bNotifyStreamSendingStartRsp\x12@\n\x08response\x18\x01 \x01(\x0b\x32..com.fsmeeting.fsp.proto.common.CommonResponse\"D\n\x17NotifyStreamSendingStop\x12\x11\n\tstream_id\x18\x01 \x01(\t\x12\x16\n\x0erecv_client_id\x18\x02 \x01(\t\"^\n\x1aNotifyStreamSendingStopRsp\x12@\n\x08response\x18\x01 \x01(\x0b\x32..com.fsmeeting.fsp.proto.common.CommonResponse*\xed\x02\n\x0fProtoDictionary\x12\x19\n\x15\x45num2UnknownInterface\x10\x00\x12\x1f\n\x1a\x45num2LoginReceivingChannel\x10\xd8\x36\x12\"\n\x1d\x45num2LoginReceivingChannelRsp\x10\xd9\x36\x12\x1d\n\x18\x45num2LoginSendingChannel\x10\xdb\x36\x12 \n\x1b\x45num2LoginSendingChannelRsp\x10\xdc\x36\x12\"\n\x1d\x45num2NotifyStreamSendingStart\x10\xdd\x36\x12%\n Enum2NotifyStreamSendingStartRsp\x10\xde\x36\x12!\n\x1c\x45num2NotifyStreamSendingStop\x10\xdf\x36\x12$\n\x1f\x45num2NotifyStreamSendingStopRsp\x10\xe0\x36\x12\x10\n\x0b\x45num2Logout\x10\xe1\x36\x12\x13\n\x0e\x45num2LogoutRsp\x10\xe2\x36\x42\'\n\x1a\x63om.fsmeeting.fsp.proto.ssP\x01\xf8\x01\x01\xa2\x02\x03GPBb\x06proto3')
  ,
  dependencies=[fsp__common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_PROTODICTIONARY = _descriptor.EnumDescriptor(
  name='ProtoDictionary',
  full_name='com.fsmeeting.fsp.proto.ss.ProtoDictionary',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Enum2UnknownInterface', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2LoginReceivingChannel', index=1, number=7000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2LoginReceivingChannelRsp', index=2, number=7001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2LoginSendingChannel', index=3, number=7003,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2LoginSendingChannelRsp', index=4, number=7004,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2NotifyStreamSendingStart', index=5, number=7005,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2NotifyStreamSendingStartRsp', index=6, number=7006,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2NotifyStreamSendingStop', index=7, number=7007,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2NotifyStreamSendingStopRsp', index=8, number=7008,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2Logout', index=9, number=7009,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2LogoutRsp', index=10, number=7010,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1037,
  serialized_end=1402,
)
_sym_db.RegisterEnumDescriptor(_PROTODICTIONARY)

ProtoDictionary = enum_type_wrapper.EnumTypeWrapper(_PROTODICTIONARY)
Enum2UnknownInterface = 0
Enum2LoginReceivingChannel = 7000
Enum2LoginReceivingChannelRsp = 7001
Enum2LoginSendingChannel = 7003
Enum2LoginSendingChannelRsp = 7004
Enum2NotifyStreamSendingStart = 7005
Enum2NotifyStreamSendingStartRsp = 7006
Enum2NotifyStreamSendingStop = 7007
Enum2NotifyStreamSendingStopRsp = 7008
Enum2Logout = 7009
Enum2LogoutRsp = 7010



_LOGINRECEIVINGCHANNEL = _descriptor.Descriptor(
  name='LoginReceivingChannel',
  full_name='com.fsmeeting.fsp.proto.ss.LoginReceivingChannel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream_id', full_name='com.fsmeeting.fsp.proto.ss.LoginReceivingChannel.stream_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stream_subscribe_token', full_name='com.fsmeeting.fsp.proto.ss.LoginReceivingChannel.stream_subscribe_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_token', full_name='com.fsmeeting.fsp.proto.ss.LoginReceivingChannel.client_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='commonInvokeInfo', full_name='com.fsmeeting.fsp.proto.ss.LoginReceivingChannel.commonInvokeInfo', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=63,
  serialized_end=235,
)


_LOGOUT = _descriptor.Descriptor(
  name='Logout',
  full_name='com.fsmeeting.fsp.proto.ss.Logout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=237,
  serialized_end=245,
)


_LOGOUTRSP = _descriptor.Descriptor(
  name='LogoutRsp',
  full_name='com.fsmeeting.fsp.proto.ss.LogoutRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='com.fsmeeting.fsp.proto.ss.LogoutRsp.response', index=0,
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
  serialized_start=247,
  serialized_end=324,
)


_LOGINRECEIVINGCHANNELRSP = _descriptor.Descriptor(
  name='LoginReceivingChannelRsp',
  full_name='com.fsmeeting.fsp.proto.ss.LoginReceivingChannelRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='com.fsmeeting.fsp.proto.ss.LoginReceivingChannelRsp.response', index=0,
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
  serialized_start=326,
  serialized_end=418,
)


_LOGINSENDINGCHANNEL = _descriptor.Descriptor(
  name='LoginSendingChannel',
  full_name='com.fsmeeting.fsp.proto.ss.LoginSendingChannel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream_id', full_name='com.fsmeeting.fsp.proto.ss.LoginSendingChannel.stream_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stream_publish_token', full_name='com.fsmeeting.fsp.proto.ss.LoginSendingChannel.stream_publish_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_token', full_name='com.fsmeeting.fsp.proto.ss.LoginSendingChannel.client_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=420,
  serialized_end=512,
)


_LOGINSENDINGCHANNELRSP = _descriptor.Descriptor(
  name='LoginSendingChannelRsp',
  full_name='com.fsmeeting.fsp.proto.ss.LoginSendingChannelRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='com.fsmeeting.fsp.proto.ss.LoginSendingChannelRsp.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='com.fsmeeting.fsp.proto.ss.LoginSendingChannelRsp.client_id', index=1,
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
  serialized_start=514,
  serialized_end=623,
)


_NOTIFYSTREAMSENDINGSTART = _descriptor.Descriptor(
  name='NotifyStreamSendingStart',
  full_name='com.fsmeeting.fsp.proto.ss.NotifyStreamSendingStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='recv_client_id', full_name='com.fsmeeting.fsp.proto.ss.NotifyStreamSendingStart.recv_client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stream_id', full_name='com.fsmeeting.fsp.proto.ss.NotifyStreamSendingStart.stream_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='commonInvokeInfo', full_name='com.fsmeeting.fsp.proto.ss.NotifyStreamSendingStart.commonInvokeInfo', index=2,
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
  serialized_start=626,
  serialized_end=771,
)


_NOTIFYSTREAMSENDINGSTARTRSP = _descriptor.Descriptor(
  name='NotifyStreamSendingStartRsp',
  full_name='com.fsmeeting.fsp.proto.ss.NotifyStreamSendingStartRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='com.fsmeeting.fsp.proto.ss.NotifyStreamSendingStartRsp.response', index=0,
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
  serialized_start=773,
  serialized_end=868,
)


_NOTIFYSTREAMSENDINGSTOP = _descriptor.Descriptor(
  name='NotifyStreamSendingStop',
  full_name='com.fsmeeting.fsp.proto.ss.NotifyStreamSendingStop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream_id', full_name='com.fsmeeting.fsp.proto.ss.NotifyStreamSendingStop.stream_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recv_client_id', full_name='com.fsmeeting.fsp.proto.ss.NotifyStreamSendingStop.recv_client_id', index=1,
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
  serialized_start=870,
  serialized_end=938,
)


_NOTIFYSTREAMSENDINGSTOPRSP = _descriptor.Descriptor(
  name='NotifyStreamSendingStopRsp',
  full_name='com.fsmeeting.fsp.proto.ss.NotifyStreamSendingStopRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='com.fsmeeting.fsp.proto.ss.NotifyStreamSendingStopRsp.response', index=0,
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
  serialized_start=940,
  serialized_end=1034,
)

_LOGINRECEIVINGCHANNEL.fields_by_name['commonInvokeInfo'].message_type = fsp__common__pb2._COMMONINVOKEINFO
_LOGOUTRSP.fields_by_name['response'].message_type = fsp__common__pb2._COMMONRESPONSE
_LOGINRECEIVINGCHANNELRSP.fields_by_name['response'].message_type = fsp__common__pb2._COMMONRESPONSE
_LOGINSENDINGCHANNELRSP.fields_by_name['response'].message_type = fsp__common__pb2._COMMONRESPONSE
_NOTIFYSTREAMSENDINGSTART.fields_by_name['commonInvokeInfo'].message_type = fsp__common__pb2._COMMONINVOKEINFO
_NOTIFYSTREAMSENDINGSTARTRSP.fields_by_name['response'].message_type = fsp__common__pb2._COMMONRESPONSE
_NOTIFYSTREAMSENDINGSTOPRSP.fields_by_name['response'].message_type = fsp__common__pb2._COMMONRESPONSE
DESCRIPTOR.message_types_by_name['LoginReceivingChannel'] = _LOGINRECEIVINGCHANNEL
DESCRIPTOR.message_types_by_name['Logout'] = _LOGOUT
DESCRIPTOR.message_types_by_name['LogoutRsp'] = _LOGOUTRSP
DESCRIPTOR.message_types_by_name['LoginReceivingChannelRsp'] = _LOGINRECEIVINGCHANNELRSP
DESCRIPTOR.message_types_by_name['LoginSendingChannel'] = _LOGINSENDINGCHANNEL
DESCRIPTOR.message_types_by_name['LoginSendingChannelRsp'] = _LOGINSENDINGCHANNELRSP
DESCRIPTOR.message_types_by_name['NotifyStreamSendingStart'] = _NOTIFYSTREAMSENDINGSTART
DESCRIPTOR.message_types_by_name['NotifyStreamSendingStartRsp'] = _NOTIFYSTREAMSENDINGSTARTRSP
DESCRIPTOR.message_types_by_name['NotifyStreamSendingStop'] = _NOTIFYSTREAMSENDINGSTOP
DESCRIPTOR.message_types_by_name['NotifyStreamSendingStopRsp'] = _NOTIFYSTREAMSENDINGSTOPRSP
DESCRIPTOR.enum_types_by_name['ProtoDictionary'] = _PROTODICTIONARY

LoginReceivingChannel = _reflection.GeneratedProtocolMessageType('LoginReceivingChannel', (_message.Message,), dict(
  DESCRIPTOR = _LOGINRECEIVINGCHANNEL,
  __module__ = 'fsp_ss_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.ss.LoginReceivingChannel)
  ))
_sym_db.RegisterMessage(LoginReceivingChannel)

Logout = _reflection.GeneratedProtocolMessageType('Logout', (_message.Message,), dict(
  DESCRIPTOR = _LOGOUT,
  __module__ = 'fsp_ss_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.ss.Logout)
  ))
_sym_db.RegisterMessage(Logout)

LogoutRsp = _reflection.GeneratedProtocolMessageType('LogoutRsp', (_message.Message,), dict(
  DESCRIPTOR = _LOGOUTRSP,
  __module__ = 'fsp_ss_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.ss.LogoutRsp)
  ))
_sym_db.RegisterMessage(LogoutRsp)

LoginReceivingChannelRsp = _reflection.GeneratedProtocolMessageType('LoginReceivingChannelRsp', (_message.Message,), dict(
  DESCRIPTOR = _LOGINRECEIVINGCHANNELRSP,
  __module__ = 'fsp_ss_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.ss.LoginReceivingChannelRsp)
  ))
_sym_db.RegisterMessage(LoginReceivingChannelRsp)

LoginSendingChannel = _reflection.GeneratedProtocolMessageType('LoginSendingChannel', (_message.Message,), dict(
  DESCRIPTOR = _LOGINSENDINGCHANNEL,
  __module__ = 'fsp_ss_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.ss.LoginSendingChannel)
  ))
_sym_db.RegisterMessage(LoginSendingChannel)

LoginSendingChannelRsp = _reflection.GeneratedProtocolMessageType('LoginSendingChannelRsp', (_message.Message,), dict(
  DESCRIPTOR = _LOGINSENDINGCHANNELRSP,
  __module__ = 'fsp_ss_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.ss.LoginSendingChannelRsp)
  ))
_sym_db.RegisterMessage(LoginSendingChannelRsp)

NotifyStreamSendingStart = _reflection.GeneratedProtocolMessageType('NotifyStreamSendingStart', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYSTREAMSENDINGSTART,
  __module__ = 'fsp_ss_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.ss.NotifyStreamSendingStart)
  ))
_sym_db.RegisterMessage(NotifyStreamSendingStart)

NotifyStreamSendingStartRsp = _reflection.GeneratedProtocolMessageType('NotifyStreamSendingStartRsp', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYSTREAMSENDINGSTARTRSP,
  __module__ = 'fsp_ss_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.ss.NotifyStreamSendingStartRsp)
  ))
_sym_db.RegisterMessage(NotifyStreamSendingStartRsp)

NotifyStreamSendingStop = _reflection.GeneratedProtocolMessageType('NotifyStreamSendingStop', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYSTREAMSENDINGSTOP,
  __module__ = 'fsp_ss_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.ss.NotifyStreamSendingStop)
  ))
_sym_db.RegisterMessage(NotifyStreamSendingStop)

NotifyStreamSendingStopRsp = _reflection.GeneratedProtocolMessageType('NotifyStreamSendingStopRsp', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYSTREAMSENDINGSTOPRSP,
  __module__ = 'fsp_ss_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.ss.NotifyStreamSendingStopRsp)
  ))
_sym_db.RegisterMessage(NotifyStreamSendingStopRsp)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032com.fsmeeting.fsp.proto.ssP\001\370\001\001\242\002\003GPB'))
# @@protoc_insertion_point(module_scope)
