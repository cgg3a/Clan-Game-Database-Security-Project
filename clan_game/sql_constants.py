# Player entity

SQL_SAVE_PLAYER= "INSERT INTO Player(Email, DisplayName) VALUES (%s, %s) ON DUPLICATE KEY UPDATE DisplayName = %s"

SQL_GET_PLAYER = "SELECT UserId, ClanId, Score, DisplayName FROM Player WHERE email= %s"

# Login entity

SQL_SAVE_LOGIN = "INSERT INTO LoginActivity(UserId, DeviceName, Location, Time) VALUES (%s, %s, %s, NOW())" 


SQL_GET_ALL_CLANS = "SELECT ClanId, DisplayName, Description FROM Clan"



