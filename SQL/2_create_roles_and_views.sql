# Create roles.
CREATE ROLE DBAAdmin;
CREATE ROLE IdentityService;
CREATE ROLE GameService;
CREATE ROLE MessengerService;
CREATE ROLE BillingService;
CREATE ROLE DataEngineering;
CREATE ROLE ProductSales;

# Create PlayerView and grant permissions.
DROP VIEW IF EXISTS PlayerView;
CREATE VIEW PlayerView AS
SELECT Player.UserId, Player.Username, LoginActivity.Time, LoginActivity.Location, LoginActivity.DeviceName
FROM Player
INNER JOIN LoginActivity ON Player.UserId = LoginActivity.UserId;

GRANT SELECT ON PlayerView TO DBAAdmin;
GRANT SELECT ON PlayerView TO IdentityService;

# Create ProductPurchaseView and grant permissions.
DROP VIEW IF EXISTS ProductPurchaseView;
CREATE VIEW ProductPurchaseView AS
SELECT Product.DisplayName, PurchaseHistory.UserId, PurchaseHistory.Time
FROM Product
INNER JOIN PurchaseHistory ON Product.ProductId = PurchaseHistory.ProductId;

GRANT SELECT ON ProductPurchaseView TO DBAAdmin;
GRANT SELECT ON ProductPurchaseView TO GameService;
GRANT SELECT ON ProductPurchaseView TO BillingService;
GRANT SELECT ON ProductPurchaseView TO DataEngineering;

# Create ClanMessageView and grant permissions.
DROP VIEW IF EXISTS ClanMessageView;
CREATE VIEW ClanMessageView AS
SELECT Clan.DisplayName, ClanMessage.UserId, ClanMessage.Time, ClanMessage.Body
FROM Clan
INNER JOIN ClanMessage ON Clan.ClanId = ClanMessage.ClanId;

GRANT SELECT ON ClanMessageView TO DBAAdmin;
GRANT SELECT ON ClanMessageView TO MessengerService;

# Create BillingView and grant permissions.
DROP VIEW IF EXISTS BillingView;
CREATE VIEW BillingView AS
SELECT *
FROM Billing;

GRANT SELECT ON BillingView TO DBAAdmin;
GRANT SELECT ON BillingView TO BillingService;