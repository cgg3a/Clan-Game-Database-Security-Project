USE LocalClans;

-- Week
INSERT INTO Week (WeekNumber, StartDate)
VALUES
(1, "2025-04-06"),
(2, "2025-04-13");

-- Clan
INSERT INTO Clan (ClanId, DisplayName, Description, ImageId)
VALUES
(3, "Test Clan", "This is a clan created as a test.", "image0"),
(4, "MyCoolClan", "A clan for really cool people :)", "image0");

-- Player
INSERT INTO Player (UserId, ClanId, DisplayName, Username, Score, Role, Password, Email)
VALUES
(7, 3, "Test", "TestAccount", 0, "Leader", "pass4321", "fake-email@mail.org"),
(8, 4, "Cool Guy", "CoolDude1", 100, "Leader", "awes0mep@ss", "cooldude1@gmail.com"),
(9, 4, "Cool Guy's Friend", "OkayDude1", 50, "Member", "coolguy1iscool!", "uncoolguy@gmail.com");

-- ClanMessage
INSERT INTO ClanMessage (MessageId, UserId, ClanId, Time, Body)
VALUES
(1, 8, 4, TIMESTAMP("2025-04-07", "13:30:05"), "hey man welcome to the clan"),
(2, 9, 4, TIMESTAMP("2025-04-07", "13:30:28"), "Thank you so much for the invite! I'm a big fan!"),
(3, 8, 4, TIMESTAMP("2025-04-07", "13:31:12"), "okay settle down"),
(4, 9, 4, TIMESTAMP("2025-04-07", "13:31:40"), "I'm sorry."),
(5, 9, 4, TIMESTAMP("2025-04-07", "13:32:03"), "Are you mad at me?"),
(6, 9, 4, TIMESTAMP("2025-04-07", "13:35:34"), "Hello?");

-- Product
INSERT INTO Product (ProductId, DisplayName, Description)
VALUES
(1, "100 Gems", "Purchase 100 gems at a time."),
(2, "500 Gems", "Purchase 500 gems at a time."),
(3, "1100 Gems", "Purchase 1000 gems, get 100 free!");

-- LoginActivity
INSERT INTO LoginActivity (LoginId, UserId, Time, DeviceName, Location)
VALUES
(1, 7, TIMESTAMP("2025-04-06", "08:30:12"), "IPhone", "USA"),
(2, 8, TIMESTAMP("2025-04-07", "11:10:00"), "PC", "USA"),
(3, 8, TIMESTAMP("2025-04-07", "13:16:02"), "PC", "USA"),
(4, 9, TIMESTAMP("2025-04-07", "12:21:43"), "PC", "USA");

-- Billing
INSERT INTO Billing (BillingId, UserId, CVC, CardHolder)
VALUES
(1, 8, 123, "John A. Doe");

-- PurchaseHistory
INSERT INTO PurchaseHistory (PurchaseId, UserId, BillingId, ProductId, Time)
VALUES
(1, 8, 1, 3, TIMESTAMP("2025-04-07", "11:12:47")),
(2, 8, 1, 2, TIMESTAMP("2025-04-09", "4:09:13"));

-- WeeklyClanPlacement
INSERT INTO WeeklyClanPlacement (PlacementId, WeekNumber, ClanId, Score, `Rank`)
VALUES
(1, 1, 3, 0, 2),
(2, 1, 4, 50, 1),
(3, 2, 3, 0, 2),
(4, 2, 4, 150, 1);

-- WeeklyPlayerPrize
INSERT INTO WeeklyPlayerPrize (WeekNumber, UserId, Category, IsClaimed)
VALUES
(1, 7, "Clan Second", FALSE),
(1, 8, "Clan First", TRUE),
(1, 9, "Clan First", TRUE),
(2, 7, "Clan Second", FALSE),
(2, 8, "Clan First", FALSE),
(2, 9, "Clan First", TRUE);