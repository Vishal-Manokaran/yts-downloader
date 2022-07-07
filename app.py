import os
from requests import get

import yts
import torrent_client
import constants


def ipv4_region():
    ip = get('http://ipinfo.io/json').json()
    info = f"{ip['ip']} - {ip['city']}, {ip['region']}, {constants.CC[ip['country']]}"
    is_india = True if ip['country'] == "IN" else False
    return (info,is_india)


os.system('cls' if os.name == 'nt' else "printf '\033c'")

while ipv4_region()[1] == True:
    print(ipv4_region()[0])
    _ = input("Please turn on VPN (or Not be in India) and press enter: ")

os.system('cls' if os.name == 'nt' else "printf '\033c'")

hash = yts.find_yify_torrent()
if hash == None:
    print('Error Finding the movie you were looking for')
    exit()
while ipv4_region()[1] == False:
    print(ipv4_region()[0])
    _ = input("Please turn off VPN and press enter: ")
print("downloading movie")
torrent_client.add_qtorrent(hash)

# vpn = subprocess.Popen('psiphon3.exe')
# while True:
#     time.sleep(5)
#     new_ip = get('http://api.ipify.org').text
#     # new_ip = str(api_req('http://api.ipify.org'))
#     print(new_ip)
#     if new_ip != original_ip:
#         print("VPN is working")
#         break


# print("terminating VPN")
# os.system("taskkill /f /im psiphon-tunnel-core.exe")
# vpn.terminate()
# vpn.kill()

# def api_req(url):
#     request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
#     response = urlopen(request).read().decode()
#     return response