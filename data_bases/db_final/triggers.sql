--after
create or replace function reduce_price()
returns trigger
language plpgsql
as $$
begin
    update car
    set rental_price = rental_price * 0.99
    where car_id = NEW.car_id;

    return NEW;
end
$$;

CREATE TRIGGER update_car_price
    AFTER INSERT
    ON rent
    FOR EACH ROW
    EXECUTE PROCEDURE reduce_price();

DROP TRIGGER update_car_price ON car;



--before
create or replace function check_palindrome()
returns trigger
language plpgsql
as $$
begin
    if NEW.plate_number || '#' = '#' || reverse(NEW.plate_number) then
        NEW.rental_price := NEW.rental_price * 1.15;
    end if;

    return NEW;
end
$$;

CREATE TRIGGER cool_number
    BEFORE INSERT
    ON car
    FOR EACH ROW
    EXECUTE PROCEDURE check_palindrome();

DROP TRIGGER cool_number ON car;
