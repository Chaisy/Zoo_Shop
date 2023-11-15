CREATE OR REPLACE PROCEDURE add_good_to_order(_order_id INTEGER, _good_id INTEGER, _count INTEGER DEFAULT 1) 
AS $$
BEGIN
	IF (EXISTS(SELECT * FROM OrderGoods AS og 
			   WHERE og.OrderId = _order_id AND og.GoodId = _good_id)) THEN
    	UPDATE OrderGoods SET "Count" = "Count" + _count WHERE "OrderId" = _order_id AND "GoodId" = _good_id;
	ELSE
		INSERT INTO OrderGoods (OrderId, GoodId, Count) 
		VALUES (_order_id, _good_id, _count);
	END IF;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE add_good_to_cart(_cart_id INTEGER, _good_id INTEGER, _count INTEGER DEFAULT 1) 
AS $$
BEGIN
	IF (EXISTS(SELECT * FROM CartsGoods AS cg 
			   WHERE cg.CartId = _cart_id AND cg.GoodId = _good_id)) THEN
    	UPDATE CartsGoods SET "Count" = "Count" + _count WHERE "CartId" = _cart_id AND "GoodId" = _good_id;
	ELSE
		INSERT INTO CartsGoods (CartId, GoodId, Count) 
		VALUES (_cart_id, _good_id, _count);
	END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE add_order(_user_id INTEGER)
AS $$
DECLARE
	order_time TIMESTAMP := NOW();
	order_good_id INTEGER;
BEGIN
	INSERT INTO Orders (UserId, time)
    VALUES (_user_id, order_time)
    RETURNING id INTO order_good_id;
END;
$$ LANGUAGE plpgsql;