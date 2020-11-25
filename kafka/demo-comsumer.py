#! /usr/bin/python3
# coding: utf-8

"""
测试用的一个kafka consumer
"""
import json
from kafka import KafkaConsumer


consumer = KafkaConsumer('test', bootstrap_servers='127.0.0.1:9092')
for msg in consumer:
    print(msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    # 获取到oss_key然后进行解析
    msg = json.loads(msg.value.decode())  # 取出是bytes,需要先decode(), 再转为字典
    print(msg)

