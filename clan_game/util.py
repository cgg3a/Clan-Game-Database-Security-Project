import os
from cryptography.fernet import Fernet
from clan_game.models import *

def encrypt(filed):
    #TODO: enenryptcode a field:
    key = os.environ['SALT_KEY'].encode('utf-8')
    f = Fernet(key)
    token = f.encrypt(field)
    print(token)

def decrypt(filed):
    #TODO: decrypt
    print("TODO: decrypt")

def  get_client_agent(request):   
     return request.META.get("HTTP_SEC_CH_UA")

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_player(request):
    if "user_data" not in request.session:
        return None
    user_data = request.session["user_data"]
    player = Player(user_data["email"])
    player.get()
    return player


