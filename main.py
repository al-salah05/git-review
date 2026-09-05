import time 
import requests
from datetime import datetime
import subprocess
print("the rasbperry pi is oneline ")
sleep_time = 3
for second in range(sleep_time,0,-1):
    print(second)
    time.sleep(1)
result= subprocess.run(
   ["hostname","-I"],
   capture_output=True,
   text=True
)
ip = result.stdout.strip()
ses = subprocess.run(
    ["hostname"],
    capture_output=True,
    text=True 
)
hostname = ses.stdout.strip()
temp_result = subprocess.run(
    ["vcgencmd","measure_temp"],
    capture_output=True,
    text=True
)
temperature = temp_result.stdout.strip()
now = datetime.now()
time = now.strftime("%H-%M-%S")

current = datetime.now()
date = now.strftime("%Y:%m:%d")

url = "https://ntfy.sh/gh-pi"
message = f""" IP : {ip},
               HOSTNAME : {hostname},
               TIME : {time},
               DATE : {date},
               TEMPERATURE :{temperature}
"""
requests.post(url,data=message)

