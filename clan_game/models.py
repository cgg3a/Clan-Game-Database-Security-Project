from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db import connection

class Player:
    def __init__(self, email, name=None):
        self.email = email.lower().strip()
        self.name = name
        self.clanId = None
        self.score = None
        self.userId = None

    def save(self):
        print(f"saving to database: {self.email}")
        try:
            with connection.cursor() as cursor:
                sql = f"""
                    INSERT INTO Player(Email, DisplayName) VALUES ('{self.email}', '{self.name}')
                        ON DUPLICATE KEY UPDATE DisplayName = '{self.name}';
                """;
                cursor.execute(sql)
                rows = cursor.fetchall()
                print(f"{cursor.rowcount} row(s) returned")
        except Exception as e:
             print(f"An error occurred: {e}")

    def get(self):
        print(f"get player data from database: {self.email}")
        try:
            with connection.cursor() as cursor:
                sql = f"""
                    SELECT UserId, ClanId, Score, DisplayName FROM Player WHERE email='{self.email}';
                """;
                cursor.execute(sql)
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
        self.location = location
    
    def save(self):
         print(f"saving login to database ..: {self.userId}")

class Clan:
    @staticmethod
    def getAllClans():
        try:
            with connection.cursor() as cursor:
                sql = f"""
                   SELECT ClanId, DisplayName, Description FROM Clan;
                """;
                cursor.execute(sql)
                rows = cursor.fetchall()
                return rows
        except Exception as e:
             print(f"An error occurred: {e}")

        