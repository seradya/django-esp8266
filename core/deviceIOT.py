import wiotp.sdk.device
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


def command_callback(cmd):
    print("Command received: %s" % cmd.data)


def send_command():
    dat = {'status' : 'ligado'}
    client.publishEvent(eventId="status", msgFormat="json", data=dat, qos=0, onPublish=None)
    client.commandCallback = command_callback


client = wiotp.sdk.device.DeviceClient(config=config)
client.connect()


while True:
    dat = {'status' : 'ligado'}
    client.publishEvent(eventId="status", msgFormat="json", data=dat, qos=0, onPublish=None)
    client.commandCallback = command_callback
    time.sleep(2)


