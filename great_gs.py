import struct
from time import sleep

import redis
from kafka import KafkaProducer

from fsp_pb import fsp_common_pb2 as pb_common
from fsp_pb import fsp_gc_pb2 as pb_gc
from fsp_pb import fsp_gs_pb2 as pb_gs
from fsp_pb import fsp_sc_pb2 as pb_sc



def CreateGroup(messageSequence, app_id, service_type, room_id, response_topic):
    creategroup = getattr(pb_gc,"CreateGroup")()
    creategroup.app_id = app_id
    creategroup.service_type = service_type
    creategroup.room_id = room_id
    print creategroup
    creategroup_msg = creategroup.SerializeToString()
    messageNumber = pb_gc.ProtoDictionary.Value("Enum2CreateGroup")
    fmt = "!BBqB%dsi" % (len(response_topic))
    msgprefix = struct.pack(fmt, 1, 1, messageSequence, len(
        response_topic), response_topic, messageNumber)
    buf = msgprefix + creategroup_msg
    print buf
    return buf


def GetGroupServers(messageSequence, group_id, client_ip, response_topic):
    getgroupserver = pb_gc.GetGroupServers()
    getgroupserver.group_id = group_id
    getgroupserver.client_ip = client_ip

    getgroupserver_msg = getgroupserver.SerializeToString()
    messageNumber = pb_gc.ProtoDictionary.Value("Enum2GetGroupServers")
    gc_topic = response_topic
    fmt = "!BBqB%dsi" % (len(gc_topic))
    msgprefix = struct.pack(fmt, 1, 1, messageSequence,
                            len(gc_topic), gc_topic, messageNumber)
    buf = msgprefix + getgroupserver_msg
    print buf
    return buf


def ClientConnected(messageSequence, client_id, service_instance_id, app_id, client_name, commonInvokeInfo, response_topic):
    clientconnected = pb_sc.ClientConnected()
    clientconnected.client_id = client_id
    clientconnected.service_instance_id = service_instance_id
    clientconnected.app_id = app_id
    clientconnected.client_name = client_name
    info = pb_common.CommonInvokeInfo()
    info.trace_id = "{461c87c9-f62f-4769-3f7a-95d0c3280d5b}"
    info.invoke_order = "DFD"

    clientconnected_msg = clientconnected.SerializeToString()
    messageNumber = pb_sc.ProtoDictionary.Value('Enum2ClientConnected')
    sc_topic = response_topic
    fmt = "!BBqB%dsi" % (len(sc_topic))
    # here the topic is for produce, not for consumer
    msgprefix = struct.pack(fmt, 1, 1, messageSequence,
                            len(sc_topic), sc_topic, messageNumber)

    buf = msgprefix+clientconnected_msg
    print buf
    return buf

def fun_b(args):
    print locals()
    mydict = {}
    for key, value in args.items():
        mydict[key] = value
    print mydict
def myfunc(a=1,b=2,c=3):
    args = locals()
    print type(args)
    fun_b(args)



if __name__ == '__main__':
    import inspect
    print hasattr(pb_gc, "CreateGroup")
    print getattr(pb_gc, "CreateGroup")
    obj = getattr(pb_gc, "CreateGroup")()
    print dir(obj)
    print [i for i in dir(obj) if inspect.isbuiltin(getattr(obj,i))]
    print [i for i in dir(obj) if inspect.isfunction(getattr(obj, i))]
    print [i for i in dir(obj) if not inspect.ismethod(getattr(obj, i))]
    print "_______________________"
    # print inspect.getmembers(obj)
    print [i for i in dir(obj) if not callable(getattr(obj, i))]
    print getattr(getattr(pb_gc, "ProtoDictionary"), "Value")("Enum2CreateGroup")

    myfunc()
    print inspect.getargspec(myfunc).args
    # r = redis.StrictRedis(host="192.168.7.114", port=6379, db="0")
    # query_result = r.get(
    #     'client_proxy:' + '{57180811-a0c1-4a77-bb64-e35ee9daf8a0};1431854')
    # print query_result
    # kafkaCluster = '192.168.7.111:9092,192.168.7.113:9092,192.168.7.114:9092'
    # producer = KafkaProducer(bootstrap_servers=kafkaCluster)
    # buf = CreateGroup(1, 'app_hj', 0, '80664', 'lizzietest')
    # print buf
    # print pb_gc.ProtoDictionary.items()
    # print pb_gc.ProtoDictionary.Name(3004)
    # print pb_gc.ProtoDictionary.keys(),pb_gc.ProtoDictionary.values()
    # producer.send("gc_group_01", buf)
    # buf = GetGroupServers(1,"80664","192.168.5.168","lizzietest")
    # producer.send("gc_instance_01",buf)

    # fmt = "!bbqb%dsi%ds" % (len("gc_instance_01"), (len(buf) - 14 - len("gc_instance_01")))
    # aa = struct.unpack(fmt, buf)
    # print aa
    # sleep(5)
    # query_result = r.smembers("group_set:app_hj")
    # # query_result = r.get('group_set:app_hj')
    # print query_result
    # group_id = [i for i in query_result][-1]

    # buf = GetGroupServers(2, group_id, "192.168.5.168", "lizzietest")
    # producer.send("gc_group_01", buf)
    # sleep(5)

    # buf = ClientConnected(3, group_id+";1431856", "gs1",
    #                       "app_hj", "gs1", '', "gs1")
    # producer.send("sc_group_01", buf)
    # sleep(5)
