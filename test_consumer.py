import Queue
import struct
import sys
import threading
from time import sleep

import requests
import urllib3
from google.protobuf.json_format import MessageToJson
from kafka import KafkaConsumer
from kafka.structs import TopicPartition

from fsp_pb import fsp_gc_pb2 as pb_gc
from fsp_pb import fsp_gs_pb2 as pb_gs
from fsp_pb import fsp_sc_pb2 as pb_sc
from fsp_pb import fsp_ss_pb2 as pb_ss
from fsp_pb import fsp_ma_pb2 as pb_ma
from fsp_pb import fsp_rule_pb2 as pb_rule
from fsp_pb import fsp_cp_pb2 as pb_cp

kafkaserver = "192.168.7.111:9092,192.168.7.113:9092,192.168.7.114:9092"


class ListenConsumer(threading.Thread):
    modules = [pb_gc,pb_gs,pb_sc,pb_ss,pb_ma,pb_rule,pb_cp]
    def __init__(self, topic, queue, lock):
        super(ListenConsumer, self).__init__()
        self.topic = topic
        self.consumer = KafkaConsumer(topic, bootstrap_servers=kafkaserver)
        self.stop_event = threading.Event()
        self.queue = queue
        self.lock = lock

    def stop(self):
        print 'stop listen thread'
        self.stop_event.set()

    def save(self, aa,funcname, jsdata):

        self.lock.acquire()
        self.queue.put("###########################################")
        self.queue.put('{} -> {} : {}'.format(aa[4], self.topic, funcname))
        self.queue.put(aa)
        self.queue.put(jsdata)
        self.lock.release()

    def run(self):
        super(ListenConsumer, self).run()
        while True:
            raw_messages = self.consumer.poll(
                timeout_ms=1000, max_records=5000)
            if self.stop_event.is_set():
                self.consumer.close()
                break
            if len(raw_messages) == 0:
                continue

            for topic_partition, message in raw_messages.items():
                buf = message[0].value
                topic_len = struct.unpack("b", buf[10:11])[0]
                fmt = "!bbqb%dsi%ds" % (topic_len, (len(buf) - 15 - topic_len))
                aa = struct.unpack(fmt, buf)
                isfind = False

                for module in self.modules:
                    values = getattr(getattr(module, "ProtoDictionary"), "values")()
                    if aa[5] in values:
                        isfind = True
                        funcname = getattr(getattr(module, "ProtoDictionary"), "Name")(aa[5])
                        try:
                            obj = getattr(module, funcname[5:])()
                            obj.ParseFromString(aa[6])
                            resp = MessageToJson(obj)
                            self.save(aa, funcname, resp)
                        except Exception:
                            self.save(aa, funcname,"")
                if not isfind:
                    print "Unknow Protocol %s" % (aa)

if __name__ == '__main__':

    q = Queue.Queue()
    lock = threading.Lock()
    topiclist = ['lizzietest', 'gc_group_01', 'gc_instance_01', 'gc_instance_02', 'gc_instance_03',
                 'sc_group_01', 'sc_instance_01', 'sc_instance_02', 'sc_instance_03',
                 'gs1', 'gs2', 'gs3',
                 'ss1', 'ss2', 'ss3','rule_group_01','rule_instance_01']
    for topic in topiclist:
        t = ListenConsumer(topic, q, lock)
        t.daemon = True
        t.start()
    print 'qqqqq'
    while True:
        sleep(0.005)
        if not q.empty():
            print q.get()

