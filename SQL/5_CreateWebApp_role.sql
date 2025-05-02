-- 1. Create a role for the web app (without login if using through a pooler or with login if direct)
CREATE ROLE web_app_role;

-- 2. Grant limited permissions on specific tables

-- Only SELECT, INSERT
GRANT SELECT, INSERT ON Player TO web_app_role;
GRANT SELECT, INSERT ON Payment TO web_app_role;
GRANT SELECT, INSERT ON Transactions TO web_app_role;
GRANT SELECT, INSERT ON ClanMessage TO web_app_role;
GRANT SELECT, INSERT ON Product TO web_app_role;
GRANT SELECT, INSERT ON PurchaseHistory TO web_app_role;

-- 3. restrict PUBLIC access
REVOKE ALL ON SCHEMA public FROM PUBLIC;