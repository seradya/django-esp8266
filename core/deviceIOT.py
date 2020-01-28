import wiotp.sdk.device
import random
import time

config = { 
    "identity": {
        "orgId": "0k740p,",
        "typeId": "Esp8266,",
        "deviceId": "seradya,",
    },
    "auth": {
        "token": "NDdVf07KBd2vjL(e6d,",
    }
}

def CommandCallback(cmd):
    print("Command received: %s" % cmd.data)

def send_command():
    Data={'status' : 'ligado'}
    client.publishEvent(eventId="status", msgFormat="json", data=Data, qos=0, onPublish=None)
    client.commandCallback = CommandCallback

client = wiotp.sdk.device.DeviceClient(config=config)
client.connect()

while True:
    Data={'status' : 'ligado'}
    client.publishEvent(eventId="status", msgFormat="json", data=Data, qos=0, onPublish=None)
    client.commandCallback = CommandCallback
    time.sleep(2)


