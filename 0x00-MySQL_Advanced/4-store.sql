-- create a trigger that decrease the quantity of an item after adding a new order
CREATE TRIGGER decrease_qty
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items SET quantity = quantity - NEW.quantity WHERE item_name=NEW.item_name;
END
