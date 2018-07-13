# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fsp-ma.proto

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
  name='fsp-ma.proto',
  package='com.fsmeeting.fsp.proto.ma',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x66sp-ma.proto\x12\x1a\x63om.fsmeeting.fsp.proto.ma\x1a\x10\x66sp-common.proto\"0\n\x0bSendingTask\x12\x0b\n\x03seq\x18\x01 \x01(\t\x12\x14\n\x0c\x61gentServers\x18\x02 \x03(\t\"_\n\x0eSendingTaskRsp\x12\x0b\n\x03seq\x18\x01 \x01(\t\x12@\n\x08response\x18\x02 \x01(\x0b\x32..com.fsmeeting.fsp.proto.common.CommonResponse\"6\n\x11SendingSimpleTask\x12\x0b\n\x03seq\x18\x01 \x01(\t\x12\x14\n\x0c\x61gentServers\x18\x02 \x03(\t\"e\n\x14SendingSimpleTaskRsp\x12\x0b\n\x03seq\x18\x01 \x01(\t\x12@\n\x08response\x18\x02 \x01(\x0b\x32..com.fsmeeting.fsp.proto.common.CommonResponse*\x9a\x01\n\x0fProtoDictionary\x12\x19\n\x15\x45num2UnknownInterface\x10\x00\x12\x15\n\x10\x45num2SendingTask\x10\x90N\x12\x18\n\x13\x45num2SendingTaskRsp\x10\x91N\x12\x1b\n\x16\x45num2SendingSimpleTask\x10\x92N\x12\x1e\n\x19\x45num2SendingSimpleTaskRsp\x10\x93NB\'\n\x1a\x63om.fsmeeting.fsp.proto.maP\x01\xf8\x01\x01\xa2\x02\x03GPBb\x06proto3')
  ,
  dependencies=[fsp__common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_PROTODICTIONARY = _descriptor.EnumDescriptor(
  name='ProtoDictionary',
  full_name='com.fsmeeting.fsp.proto.ma.ProtoDictionary',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Enum2UnknownInterface', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2SendingTask', index=1, number=10000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2SendingTaskRsp', index=2, number=10001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2SendingSimpleTask', index=3, number=10002,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2SendingSimpleTaskRsp', index=4, number=10003,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=369,
  serialized_end=523,
)
_sym_db.RegisterEnumDescriptor(_PROTODICTIONARY)

ProtoDictionary = enum_type_wrapper.EnumTypeWrapper(_PROTODICTIONARY)
Enum2UnknownInterface = 0
Enum2SendingTask = 10000
Enum2SendingTaskRsp = 10001
Enum2SendingSimpleTask = 10002
Enum2SendingSimpleTaskRsp = 10003



_SENDINGTASK = _descriptor.Descriptor(
  name='SendingTask',
  full_name='com.fsmeeting.fsp.proto.ma.SendingTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seq', full_name='com.fsmeeting.fsp.proto.ma.SendingTask.seq', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='agentServers', full_name='com.fsmeeting.fsp.proto.ma.SendingTask.agentServers', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=62,
  serialized_end=110,
)


_SENDINGTASKRSP = _descriptor.Descriptor(
  name='SendingTaskRsp',
  full_name='com.fsmeeting.fsp.proto.ma.SendingTaskRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seq', full_name='com.fsmeeting.fsp.proto.ma.SendingTaskRsp.seq', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='response', full_name='com.fsmeeting.fsp.proto.ma.SendingTaskRsp.response', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=112,
  serialized_end=207,
)


_SENDINGSIMPLETASK = _descriptor.Descriptor(
  name='SendingSimpleTask',
  full_name='com.fsmeeting.fsp.proto.ma.SendingSimpleTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seq', full_name='com.fsmeeting.fsp.proto.ma.SendingSimpleTask.seq', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='agentServers', full_name='com.fsmeeting.fsp.proto.ma.SendingSimpleTask.agentServers', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=209,
  serialized_end=263,
)


_SENDINGSIMPLETASKRSP = _descriptor.Descriptor(
  name='SendingSimpleTaskRsp',
  full_name='com.fsmeeting.fsp.proto.ma.SendingSimpleTaskRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seq', full_name='com.fsmeeting.fsp.proto.ma.SendingSimpleTaskRsp.seq', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='response', full_name='com.fsmeeting.fsp.proto.ma.SendingSimpleTaskRsp.response', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=265,
  serialized_end=366,
)

_SENDINGTASKRSP.fields_by_name['response'].message_type = fsp__common__pb2._COMMONRESPONSE
_SENDINGSIMPLETASKRSP.fields_by_name['response'].message_type = fsp__common__pb2._COMMONRESPONSE
DESCRIPTOR.message_types_by_name['SendingTask'] = _SENDINGTASK
DESCRIPTOR.message_types_by_name['SendingTaskRsp'] = _SENDINGTASKRSP
DESCRIPTOR.message_types_by_name['SendingSimpleTask'] = _SENDINGSIMPLETASK
DESCRIPTOR.message_types_by_name['SendingSimpleTaskRsp'] = _SENDINGSIMPLETASKRSP
DESCRIPTOR.enum_types_by_name['ProtoDictionary'] = _PROTODICTIONARY

SendingTask = _reflection.GeneratedProtocolMessageType('SendingTask', (_message.Message,), dict(
  DESCRIPTOR = _SENDINGTASK,
  __module__ = 'fsp_ma_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.ma.SendingTask)
  ))
_sym_db.RegisterMessage(SendingTask)

SendingTaskRsp = _reflection.GeneratedProtocolMessageType('SendingTaskRsp', (_message.Message,), dict(
  DESCRIPTOR = _SENDINGTASKRSP,
  __module__ = 'fsp_ma_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.ma.SendingTaskRsp)
  ))
_sym_db.RegisterMessage(SendingTaskRsp)

SendingSimpleTask = _reflection.GeneratedProtocolMessageType('SendingSimpleTask', (_message.Message,), dict(
  DESCRIPTOR = _SENDINGSIMPLETASK,
  __module__ = 'fsp_ma_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.ma.SendingSimpleTask)
  ))
_sym_db.RegisterMessage(SendingSimpleTask)

SendingSimpleTaskRsp = _reflection.GeneratedProtocolMessageType('SendingSimpleTaskRsp', (_message.Message,), dict(
  DESCRIPTOR = _SENDINGSIMPLETASKRSP,
  __module__ = 'fsp_ma_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.ma.SendingSimpleTaskRsp)
  ))
_sym_db.RegisterMessage(SendingSimpleTaskRsp)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032com.fsmeeting.fsp.proto.maP\001\370\001\001\242\002\003GPB'))
# @@protoc_insertion_point(module_scope)
