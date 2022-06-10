from ipaddress import IPv4Address
from pyairmore.request import AirmoreSession
from pyairmore.services.device import DeviceService
from decouple import config

D_IP=config("IP") #Reading IP from .env

ip = IPv4Address(f'{D_IP}')  # whatever server's address is
session = AirmoreSession(ip)  # port is default to 2333
service = DeviceService(session) #starts a session
