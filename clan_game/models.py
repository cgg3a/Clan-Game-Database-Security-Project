import os
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db import connection
from cryptography.fernet import Fernet
from .sql_constants import *

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
             print(f"An error occurred: {e}")

    def get(self):
        print(f"Fetching player data from database: {self.email}")
        try:
            with connection.cursor() as cursor:
                cursor.execute(SQL_GET_PLAYER, self.email)
                rows = cursor.fetchall()
                for row in rows:
                    self.userId = row[0]
                    self.clanId = row[1]
                    self.score = row[2]
                    self.name = row[3]
        except Exception as e:
             print(f"An error occurred: {e}")

class Login:
    def __init__(self, userId, deviceName, location):
        self.userId = userId
        self.deviceName = deviceName, 
        self.location = location, 

    def save(self):
        print(self.deviceName)
        print(f"saving login to database ..: {self.userId}")
        try:
            with connection.cursor() as cursor:
                cursor.execute(SQL_SAVE_LOGIN, (self.userId, self.deviceName, self.location))
                rows = cursor.fetchall()
                print(f"{cursor.rowcount} row(s) returned")
        except Exception as e:
             print(f"An error occurred: {e}")
       

class Payment:
    def __int__(self, credit_card_number):
        self.credit_card_number = credit_card_number
    
    def save(self):
        #TODO:
        print("save payemnt info")


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

        