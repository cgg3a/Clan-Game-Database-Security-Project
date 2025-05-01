DROP DATABASE IF EXISTS Clans;
CREATE DATABASE Clans;
USE Clans;

CREATE TABLE Week (
    WeekNumber INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    StartDate TIMESTAMP
);

CREATE TABLE Clan (
    ClanId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    DisplayName VARCHAR(50),
    Description VARCHAR(250),
    ImageId VARCHAR(100)
);

CREATE TABLE Player (
    UserId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ClanId INT,
    DisplayName VARCHAR(20),
    Username VARCHAR(20),
    Score INT,
    Role VARCHAR(20),
    Password VARCHAR(50),
    Email VARCHAR(50),
    FOREIGN KEY (ClanId)
        REFERENCES Clan (ClanId)
);

CREATE TABLE ClanMessage (
    MessageId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    UserId INT,
    ClanId INT,
    Time TIMESTAMP,
    Body VARCHAR(250),
    FOREIGN KEY (UserId)
        REFERENCES Player (UserId),
    FOREIGN KEY (ClanId)
        REFERENCES Clan (ClanId)
);

CREATE TABLE Product (
    ProductId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    DisplayName VARCHAR(50),
    Description VARCHAR(250)
);

CREATE TABLE LoginActivity (
    LoginId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    UserId INT,
    Time TIMESTAMP,
    DeviceName VARCHAR(100),
    Location VARCHAR(50),
    FOREIGN KEY (UserId)
        REFERENCES Player (UserId)
);

CREATE TABLE Billing (
    BillingId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    UserId INT,
    CVC INT,
    CardHolder VARCHAR(50),
    FOREIGN KEY (UserId)
        REFERENCES Player (UserId)
);

CREATE TABLE PurchaseHistory (
    PurchaseId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    UserId INT,
    BillingId INT,
    ProductId INT,
    Time TIMESTAMP,
    FOREIGN KEY (UserId)
        REFERENCES Player (UserId),
    FOREIGN KEY (ProductId)
        REFERENCES Product (ProductId),
    FOREIGN KEY (BillingId)
        REFERENCES Billing (BillingId)
);

CREATE TABLE WeeklyClanPlacement (
    PlacementId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    WeekNumber INT,
    ClanId INT,
    Score INT,
    `Rank` INT,
    FOREIGN KEY (WeekNumber)
        REFERENCES Week (WeekNumber),
    FOREIGN KEY (ClanId)
        REFERENCES Clan (ClanId)
);

CREATE TABLE WeeklyPlayerPrize (
    WeekNumber INT,
    UserId INT,
    Category VARCHAR(20),
    IsClaimed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (WeekNumber)
        REFERENCES Week (WeekNumber),
    FOREIGN KEY (UserId)
        REFERENCES Player (UserId),
    PRIMARY KEY (WeekNumber , UserId , Category)
);
