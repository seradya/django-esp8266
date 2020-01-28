import wiotp.sdk.application
import asyncio.events 

appConfig = { 
    "auth": {
        "key": "a-0k740p-6un1ebkdpy",
        "token": "T7(mGuyfFWzPH263)7",
    }
}

data_event = None 

def EventCallback(event):
    global data_event 
    data_event = event.data

def get_data_device():
    client.deviceEventCallback = EventCallback
    return data_event

client = wiotp.sdk.application.ApplicationClient(config=appConfig)
client.connect()
client.subscribeToDeviceEvents(msgFormat="json")
