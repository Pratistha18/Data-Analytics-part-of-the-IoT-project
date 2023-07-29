from Adafruit_IO import Client
import random
aio = Client('Pratistha Gaur','aio_JQdf620peu4t13XAuqqPDFC1xIMF')

temp = aio.feeds('temperature')
for i in range(1,4):
    aio.send_data(temp.key, random.uniform(16,50))

humid = aio.feeds('humidity')
for i in range(1,4):
    aio.send_data(humid.key, random.uniform(30,70))

gas1 = aio.feeds('gas1')
for i in range(1,4):
    aio.send_data(gas1.key, random.randint(5,500))

gas2 = aio.feeds('gas2')
for i in range(1,4):
    aio.send_data(gas2.key, random.randint(10,500))

