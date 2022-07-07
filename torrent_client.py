import os

from qbittorrent import Client
from requests import get

def ipv4_region():
    ip = get('http://ipinfo.io/json').json()
    info = f"{ip['ip']} - {ip['city']}, {ip['region']}({ip['country']})"
    is_india = True if ip['country'] == "IN" else False
    return (info,is_india)

def add_qtorrent(hash):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    # hash = "CAEBDB751F2B541C9A420A15FB5C107494544285"
    magnet_link = f"magnet:?xt=urn:btih:{hash}&dn=ez&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Fopentor.org%3A2710&tr=udp%3A%2F%2Ftracker.ccc.de%3A80&tr=udp%3A%2F%2Ftracker.blackunicorn.xyz%3A6969&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969"
    
    qb = Client("http://127.0.0.1:8080/")
    qb.login("vishal", "vishalpassword")
    qb.download_from_link(link = magnet_link,savepath="./downloaded")
    print("succesfully downloading")
    # time.sleep(1)
    # print(qb.torrents())

if __name__ == "__main__":
    add_qtorrent("CAEBDB751F2B541C9A420A15FB5C107494544285")