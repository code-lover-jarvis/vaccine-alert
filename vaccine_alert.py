import requests
import datetime
import json
from notify_run import Notify
import os
import time
notify=Notify()
count=0

# https://notify.run/c/wHAiJ6eL87leGECJ
while True:
    print(count+1)
    x = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d-%m-%Y")
    response = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=298&date={}".format(x), headers={"content-type":"text", "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0"})
    print(response)
    json_data = json.loads(response.text)
    if(len(json_data["centers"])==0):
        time.sleep(10)
        count+=1
        continue
    for centers in json_data["centers"]:
        if(centers["name"] != "KIMS KOLLAM"):
            for avail in centers["sessions"]:
                if(avail["available_capacity"] != 0):
                    os.system('notify-run send "{}vaccines available at {} for {}" '.format(avail["available_capacity"], centers["name"], avail["date"]))
                    count+=1
                    time.sleep(120)
                else:
                    time.sleep(10)
                    count+=1
                    continue
        else:
            time.sleep(10)
            count+=1
            continue
