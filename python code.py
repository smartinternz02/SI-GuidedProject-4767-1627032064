import wiotp.sdk.device
import time
import random
import requests
myConfig = { 
    "identity": {
        "orgId": "1bjhlu",
        "typeId": "VITDEVICE",
        "deviceId":"63021"
    },
    "auth": {
        "token": "9876543210"
    }
}
def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    print()      
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()
while True:
    temp=random.randint(10,50)
    ph=random.randint(3,12)
    con=random.randint(400,1000)
    oxi=random.randint(650,800)
    tur=random.randint(0,5)
    if((6<=ph<=9)and(20<temp<40)and(500<con<1000) and(650<oxi<800)and(0<tur<5)):
        sms=1
        print("drink that water")
    else:
        sms=0
        print("not to drink that water")
    myData={'Temperature':temp,'PH_Value':ph,'Conductivity':con,'Oxidation_Reduction_Potential':oxi,'Turbidity':tur,'sms':sms}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
r = requests.get('https://www.fast2sms.com/dev/bulkV2?authorization=NegxEnouG4SH0iXbVzDyBQIWFpa7m86RlKAqZ52Udtsvc1YCOkkuhIfbGpKrMyVgxo3svneHa0Wz587E&route=q&message=%20prefer%20%20not%20to%20Drink%20water&language=english&flash=0&numbers=6302197483')
print(r.text)


