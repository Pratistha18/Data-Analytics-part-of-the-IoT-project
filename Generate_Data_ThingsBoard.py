import time
import paho.mqtt.client as mqtt
import json
import random

THINGSBOARD_HOST = 'thingsboard.cloud'
ACCESS_TOKEN = 'Ubr8VPC8khHflQiLpmTP'

sensor_data = {'temperature' : 0, 'humidity' : 0}

client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)

client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_start()

try:
    while True:
        sendval = random.randrange(16,36)
        sensor_data['temperature'] = sendval
        sendval = random.randrange(30,70)
        sensor_data['humidity'] = sendval
        sendval = random.randrange(5,500)
        sensor_data['gas'] = sendval
        
        client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
        time.sleep(5)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()

