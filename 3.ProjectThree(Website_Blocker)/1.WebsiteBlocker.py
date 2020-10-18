import time

from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1"

website_list = ["www.facebook.com", "facebook.com", "www.learncpp.com", "learncpp.com"]

while True:
    if dt(2020,7,26,8)<dt.now()<dt(2020,7,26,16):
        print("Working hours. No funny business!")
    else:
        print("You are released from all your duties for the day!")
    time.sleep(3)
