CREATE OR REPLACE FUNCTION having_admin(u RECORD)
RETURNS RECORD AS $$
BEGIN
  IF ((SELECT COUNT(*) FROM Users WHERE RoleId = 3) > 1) THEN
    RETURN u;
  ELSE
    RAISE EXCEPTION 'Cant execute operation because there must be at least one admin';
  END IF;
END
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION having_admin_after_delete()
RETURNS TRIGGER AS $$
	BEGIN RETURN having_admin(OLD); END
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER having_admin_after_delete
	BEFORE DELETE ON Users
	FOR EACH ROW
	WHEN (OLD.RoleId = 3)
	EXECUTE FUNCTION having_admin_after_delete();
	

CREATE OR REPLACE FUNCTION having_admin_after_update()
RETURNS TRIGGER AS $$
	BEGIN RETURN having_admin(NEW); END
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER having_admin_after_update
	BEFORE UPDATE ON Users
	FOR EACH ROW
	WHEN (OLD.RoleId = 3 AND NEW.RoleId != 3)
	EXECUTE FUNCTION having_admin_after_update();
	
	
CREATE OR REPLACE FUNCTION add_user_cart_if_not_exists()
RETURNS TRIGGER AS $$
BEGIN
  IF NOT EXISTS(SELECT * FROM Carts AS c WHERE c.UserId = NEW.id) THEN
    INSERT INTO Carts (UserId)
  	VALUES (NEW.id);
  	RETURN NEW;
  END IF;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER add_to_another_table
	AFTER INSERT ON Users
	FOR EACH ROW
	EXECUTE FUNCTION add_user_cart_if_not_exists();