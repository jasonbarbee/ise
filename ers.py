from ise import ERS
from dotenv import load_dotenv
from os import getenv
# import mac
import time
import datetime

start_time = datetime.datetime.now()
# print("Start Time:")

# load_dotenv()
# instance = {"mac_address": '1234:1234:1234:1234'}

# valid = mac.isValidMACAddress(instance.mac_address)
# print("Valid MAC Address " + str(valid))
ise = ERS(ise_node='csbise01.csbproserve.cm', ers_user='admi1n', ers_pass='Cisco123!', verify=False, disable_warnings=True)
# version = ise.get_version()
print(ise.version)
elapsed = datetime.datetime.now() - start_time
print(int(elapsed.total_seconds()*1000))
# groups = ise.get_identity_groups()['response']
# for group in groups:
    # print(group[0] + " - " + group[2])
