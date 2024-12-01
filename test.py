import requests
from utils import lookBin,genProxy
from gateway import Tele

r = requests.session()

urlToGet = "http://api.ipify.org/"
r = requests.get(urlToGet, proxies=genProxy())
print(Tele("5239266485227002|11|2024|059"))
