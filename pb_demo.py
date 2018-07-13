import struct
from fsp_pb import fsp_gc_pb2 as pb_gc
from google.protobuf.json_format import MessageToJson
from kafka import KafkaConsumer, KafkaProducer


def encodeCreateGroup(messageSequence, app_id, service_type, room_id,
                response_topic):
    creategroup = pb_gc.CreateGroup()
    creategroup.app_id = app_id
    creategroup.service_type = service_type
    creategroup.room_id = room_id

    creategroup_msg = creategroup.SerializeToString()
    messageNumber = pb_gc.ProtoDictionary.Value("Enum2CreateGroup")

    fmt = "!bbqb%dsi" % (len(response_topic))
    msgprefix = struct.pack(fmt, 1, 1, messageSequence, len(response_topic),
                            response_topic, messageNumber)
    buf = msgprefix + creategroup_msg

    return buf

def decodeCreateGroup(buf):

    topic_len = struct.unpack("b", buf[10:11])[0]
    fmt = "!bbqb%dsi%ds" % (topic_len, (len(buf) - 15 - topic_len))
    aa = struct.unpack(fmt, buf)
    print aa
    messageNumber = aa[2]
    response_topic = aa[4]
    command_id = aa[5]
    msg = aa[6]
    creategroup = pb_gc.CreateGroup()
    creategroup.ParseFromString(msg)
    msg_json = MessageToJson(creategroup)
    print msg_json



if __name__ == "__main__":
    buf = encodeCreateGroup(123, "appid", 1, "888888", "as1")
    print buf
    with open("buf", "wb") as f:
        f.write(buf)
    decodeCreateGroup(buf)
    # producer = KafkaProducer(bootstrap_servers="192.168.7.111:9092")
    # producer.send("gc1",buf)

