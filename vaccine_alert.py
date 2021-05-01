import requests
import datetime
from notify_run import Notify
import os
import json

notify=Notify()
# os.system('cmd /k "notify-run configure https://notify.run/c/wHAiJ6eL87leGECJ" ')

x = datetime.date.today().strftime("%d-%m-%Y")
response = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=298&date={}".format(x))
json_data = json.loads(response.text)
for centers in json_data["centers"]:
    for avail in centers["sessions"]:
        if(avail["available_capacity"] != 0):
            os.system('''cmd /k "notify-run send "{} available at {} for {}" " '''.format(avail["available_capacity"], centers["name"], avail["date"]))
