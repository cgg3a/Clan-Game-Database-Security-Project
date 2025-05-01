CREATE INDEX idx_player_email
ON Player(email);


ALTER TABLE LoginActivity MODIFY COLUMN DeviceName VARCHAR(200);