from datetime import datetime
from scrapli.driver.core import IOSXEDriver

my_time = datetime.now().strftime("%H:%M:%S")
print (my_time)


command_to_send = input ("enter command:")

MY_DEVICE = {
    "host": "172.17.0.199",
    "auth_username":"teri",
    "auth_password": "teri0x2102",
    "port": 22,
    "auth_strict_key": False,
}

with IOSXEDriver(**MY_DEVICE) as conn:
    result = conn.send_command (command_to_send)

my_list = result.result.splitlines()

#print (my_list)
with open (f"{command_to_send}-{my_time}.txt", "x") as f:
    for line in my_list:
        f.write (line+ "\n")