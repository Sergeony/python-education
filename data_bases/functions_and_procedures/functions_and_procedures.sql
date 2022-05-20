-- Task 1:
create or replace function reset_shipping_total(x varchar(255))
returns numeric
language plpgsql
as $$
declare
    orders_total numeric := 0;
    var record;
begin

    for var in (
        select *
        from _order
            join carts c on _order.carts_cart_id = c.cart_id
            join users u on c.users_user_id = u.user_id
        where city = x)
    loop
        orders_total = orders_total + var.total;

        update _order
        set shipping_total = 0
        where carts_cart_id = var.carts_cart_id;
    end loop;

    return orders_total;
end
$$;

DROP FUNCTION reset_shipping_total;

-- USAGE:
SELECT * FROM reset_shipping_total('city 1');



-- Task 2:
-- remove all orders with cancel status, which were created older than specified day interval.
create or replace procedure remove_old_canceled_orders(day_interval_to_remove integer)
language plpgsql
as $$
begin
    delete
    from _order
    where order_status_order_status_id = 5
      and extract(day from now() - created_at) >= day_interval_to_remove;
end
$$;

DROP PROCEDURE remove_old_canceled_orders(day_interval_to_remove integer);

-- USAGE:
CALL remove_old_canceled_orders(1963);



-- Task 3:
-- If some products in the category are almost out of stock,
-- make a discount for them (to buy a new batch faster).
create or replace procedure make_discount(count_to_discount int,
                                          category_to_discount int,
                                          discount_in_per int)
language plpgsql
as $$
begin
    if discount_in_per > 100 then
        raise exception 'discount must be lesser then 100';
    end if;

    update products
    set price = price * discount_in_per
    where in_stock <= count_to_discount
      and category_id = category_to_discount;

    commit;
end
$$;

DROP PROCEDURE make_discount(count_to_discount int, category_to_discount int);

-- USAGE:
CALL make_discount(2, 1, 101);



-- Task 4:
-- update with validation for user's contact info.
create or replace procedure update_contact_info(_user_id int,
                                                new_email varchar(255) default null,
                                                new_phone_number varchar(255) default null)
language plpgsql
as $$
begin
    if new_email is not null then
        if new_email like '%@%.%' then
            update users
            set email = new_email
            where user_id = _user_id;
        else
            raise exception 'invalid email: %', new_email;
        end if;
    end if;

    if new_phone_number is not null then
        if length(new_phone_number) = 11 then
            update users
            set phone_number = new_phone_number
            where user_id = _user_id;
        else
            raise exception 'invalid phone number: %', new_phone_number;
        end if;
    end if;

    commit;
end
$$;

DROP PROCEDURE update_contact_info(_user_id int, new_email varchar(255), new_phone_number varchar(255));

-- USAGE:
CALL update_contact_info(1, 'new_mail@gmail.com', '00000000000');
