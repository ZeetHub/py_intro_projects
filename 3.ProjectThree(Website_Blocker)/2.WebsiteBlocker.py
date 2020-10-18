import time

from datetime import datetime as dt

host_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1"

website_list = ["www.facebook.com", "facebook.com", "www.learncpp.com", "learncpp.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8)<dt.now()<dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("Working hours. No funny business!")
        with open(hosts_path, 'r+') as myfile:
            content = myfile.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    myfile.write(redirect+ " " +website+"\n")
    else:
        print("You are released from all your duties for the day!")
        with open(hosts_path, 'r+') as myfile:
            content = myfile.readlines()#Each line is saved as a list.
            myfile.seek(0)
            for line in content:# for each memeber of the list created above
                if not any(website in line for website in website_list):
                    myfile.write(line)
            myfile.truncate()

    time.sleep(3)
