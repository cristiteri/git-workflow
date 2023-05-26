from datetime import datetime
from scrapli.driver.core import IOSXEDriver

my_time = datetime.now().strftime("%H:%M:%S")
print (my_time)


command_to_send = input ("enter command:")

with open ("hosts", "r") as f:
    devices = f.readlines()

my_dev=[]
for each in devices:
    my_dev.append(each.rstrip('\n'))


"""
MY_DEVICES = [ 
    {
        "host": "172.17.0.199",
        "auth_username":"teri",
        "auth_password": "teri0x2102",
        "port": 22,
        "auth_strict_key": False,
    }
]
"""
MY_DEVICES = []

for ip in my_dev:
    MY_DEVICES.append({"host": ip, "auth_username":"teri", "auth_password": "teri0x2102", "port": 22, "auth_strict_key": False})




#print (MY_DEVICES)
#for i in MY_DEVICES:
#    print (i)
for device in MY_DEVICES:
    with IOSXEDriver(**device) as conn:
         result = conn.send_command (command_to_send)

    my_list = result.result.splitlines()
    with open (f"{command_to_send}-{my_time}.txt", "a") as f:
        f.write (f"\n\n\n {device.get('host')} rutele OSPF \n\n")
        for line in my_list:
            f.write (line+ "\n")
