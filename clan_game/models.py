import os
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db import connection
from cryptography.fernet import Fernet
from .sql_constants import *

KEY = os.environ['SALT_KEY'].encode('utf-8')
f = Fernet(KEY)

class Player:
    def __init__(self, email, name=None):
        self.email = email.lower().strip()
        self.name = name
        self.clanId = None
        self.score = None
        self.userId = None

    def save(self):
        print(f"saving player to database: {self.email}")
        try:
            with connection.cursor() as cursor:
                cursor.execute(SQL_SAVE_PLAYER, (self.email, self.name, self.name))
                rows = cursor.fetchall()
                print(f"{cursor.rowcount} row(s) returned")
        except Exception as e:
             print(f"An error occurred while saving player: {e}")

    def get(self):
        print(f"Fetching player data from database: {self.email}")
        try:
            with connection.cursor() as cursor:
                cursor.execute(SQL_GET_PLAYER, str(self.email))
                rows = cursor.fetchall()
                for row in rows:
                    self.userId = row[0]
                    self.clanId = row[1]
                    self.score = row[2]
                    self.name = row[3]
        except Exception as e:
             print(f"An error occurred while fetching player: {e}")

class Login:
    def __init__(self, userId, deviceName, location):
        self.userId = userId
        self.deviceName = deviceName, 
        self.location = location, 

    def save(self):
        print(f"saving login to database ..: {self.userId}")
        try:
            with connection.cursor() as cursor:
                cursor.execute(SQL_SAVE_LOGIN, (self.userId, str(self.deviceName), self.location))
                rows = cursor.fetchall()
                print(f"{cursor.rowcount} row(s) returned")
        except Exception as e:
             print(f"An error occurred while saving login: {e}")
       

class Payment:
    def __init__(self, userId, credit_card_number, cvc, card_holder, address_info):
        self.userId = userId
        self.credit_card_number = credit_card_number
        self.cvc = cvc
        self.card_holder = card_holder
        self.address_info = address_info

    def mask_credit_card(self, number_string):
        return number_string[0:4] + "x"*8 + number_string[-4:] 

    def encrypt(self, field):
        token = f.encrypt(field.encode("utf-8"))
        return token
    
    def save(self):
        payment_token = self.encrypt(self.credit_card_number)
        masked_credit_card = self.mask_credit_card(self.credit_card_number)
        try:
            with connection.cursor() as cursor:
                cursor.execute(SQL_SAVE_PAYMENT, (self.userId, masked_credit_card, payment_token, self.cvc, self.card_holder, self.address_info))
                rows = cursor.fetchall()
                print(f"{cursor.rowcount} row(s) returned")
                print(f"saved payemnt - credit card: {masked_credit_card}")
                
        except Exception as e:
             print(f"An error occurred while saving login: {e}")

class Clan:
    @staticmethod
    def getAllClans():
        try:
            with connection.cursor() as cursor:
                cursor.execute(SQL_GET_ALL_CLANS)
                rows = cursor.fetchall()
                return rows
        except Exception as e:
             print(f"An error occurred: {e}")

        