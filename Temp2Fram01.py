import requests
import os
import random

dweetIO = "https://dweet.io/dweet/for/"
myName = "CETdweet"
myKey = "temp"
    
while True:
    tempC=random.randint(1,100)
    #https://dweet.io/dweet/for/CETdweet?temp=68
    rqsString = dweetIO+myName+'?'+myKey+'='+str(tempC)
    print(rqsString)
    rqs = requests.get(rqsString)
    print rqs.status_code
    print rqs.headers
    print rqs.content
