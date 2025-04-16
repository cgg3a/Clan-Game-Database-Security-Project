from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db import connection


class Player:
    def __init__(self, email):
        self.email = email.lower().strip()

    def save(self):
        print(f"saving to database: {self.email}")
        try:
            with connection.cursor() as cursor:
                sql = f"INSERT IGNORE INTO Player(email) VALUES ('{self.email}')";
                cursor.execute(sql)
                rows = cursor.fetchall()
                print(f"{cursor.rowcount} row(s) returned")
        except Exception as e:
             print(f"An error occurred: {e}")

        