CREATE INDEX idx_player_email
ON Player(email);


ALTER TABLE Player ADD CONSTRAINT constr_uniq_email UNIQUE (email);