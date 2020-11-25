# coding: utf-8

#! /usr/bin/python3
# coding: utf-8

import json
import time

from kafka import KafkaProducer
# from test.load_fixtures import FIXTURES

# groups_fixtures = FIXTURES.get('groups')

producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')

if __name__ == '__main__':
    # group_id = groups_fixtures[0]['fields']['id']
    group_id = 20
    data = dict(
        group_id=group_id,
        model_url='http://sensoro.com',
        training_time=int(time.time()*1000)
    )
    producer.send('test', json.dumps(data).encode('utf-8'))
    print("data: {}".format(data))
    producer.flush()

