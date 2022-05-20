-- Task 1:
SELECT c.category_title,
       p.product_title,
       p.price,
       AVG(p.price) OVER (
           PARTITION BY c.category_id) AS avg_category_price
FROM products p
    JOIN categories c
        ON p.category_id = c.category_id;



-- Task 2:
--update or set contact info, if it's valid and
--raise exception, if not.
create or replace function check_contact_info()
returns trigger
language plpgsql
as $$
begin
    if NEW.email not like '%@%.%' then
        raise exception 'invalid email: %', NEW.email;
    end if;

    if length(NEW.phone_number) != 11 then
        raise exception 'invalid phone number: %', NEW.phone_number;
    end if;

    return NEW;
end
$$;

--Run each time, when user tries to change their info.
CREATE TRIGGER update_contact_info
    BEFORE INSERT OR UPDATE
    ON users
    FOR EACH ROW
    EXECUTE PROCEDURE check_contact_info();

DROP TRIGGER update_contact_info ON users;

--USAGE:
UPDATE users SET phone_number = '11111111111' WHERE user_id = 2;



-- Task 3:
-- if products in cart of inserted order already out of stock,
-- raise an exception.
create or replace function check_in_stock()
returns trigger
language plpgsql
as
$$
declare
    var record;
begin
    for var in (
        select *
        from carts c
            join cart_product cp on c.cart_id = cp.carts_cart_id
            join products p on cp.products_product_id = p.product_id
        where c.cart_id = NEW.carts_cart_id)
    loop
        if var.in_stock = 0 then
            raise exception 'order can not be created because products in it out of stock.';
        end if;
    end loop;

    return NEW;
end
$$;

--Run for each creation order.
CREATE TRIGGER make_order
    BEFORE INSERT
    ON _order
    FOR EACH ROW
    EXECUTE PROCEDURE check_in_stock();

DROP TRIGGER make_order ON _order;

-- USAGE:
INSERT INTO _order(order_id, carts_cart_id, order_status_order_status_id, shipping_total, total, created_at, updated_at) VALUES
    (1502, 1882, 1, 300, 300, now(), now());
