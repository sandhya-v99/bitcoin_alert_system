import requests
import time
import json
import conf
from boltiot import Bolt


mybolt= Bolt(conf.bolt_api_key,conf.device_id)

def buzzer_on_off(pin,state):
    if state == "on":
        mybolt.analogWrite(pin,'255')
    elif state == "off":
        mybolt.analogWrite(pin,'0')


    
def get_currency():
    url="https://min-api.cryptocompare.com/data/price"
    data={
        "fsym" : "BTC",
        "tsyms" : "USD"
        
        }
    response=requests.request("GET",url,params=data)
    response=json.loads(response.text)
    
    return response["USD"]
while True:   
 current_price=get_currency()
 set_price=300
 if current_price>set_price:
       buzzer_on_off(0,"on")
       time.sleep(4)
       buzzer_on_off(0,"off")
       print("bitcoin price is higher")
 else:
       print("bitcoin price is blala")
 
 time.sleep(10)
