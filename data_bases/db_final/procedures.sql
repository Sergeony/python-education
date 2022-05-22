-- insert
create or replace procedure create_rent(
    new_customer_id integer,
    new_car_id integer,
    new_rental_date date,
    new_period interval
)
language plpgsql
as $$
declare
    last_rent record;
begin
    select rental_date, period
    into last_rent
    from rent
    where car_id = new_car_id
    order by rental_date DESC
    LIMIT 1;

    if last_rent.rental_date + last_rent.period > now() then
        raise exception 'the car with id % still in the rent for now', new_car_id;
    else
        insert into rent(customer_id, car_id, rental_date, period) VALUES
            (new_customer_id, new_car_id, new_rental_date, new_period);
    end if;

    commit;
end
$$;



-- update
create or replace procedure extend_rent(
    cur_rent_id integer,
    new_period interval
)
language plpgsql
as $$
declare
    rental_time record;
begin
    select rental_date, period
    into rental_time
    from rent
    where rent_id = cur_rent_id;

    if rental_time.rental_date + rental_time.period <= now() then
        raise exception 'the rent already finished.';
    else
        update rent
        set period = new_period
        where rent_id = cur_rent_id;
    end if;

    commit;
end
$$;



-- delete
create or replace procedure remove_old_car(count_to_remove integer)
language plpgsql
as $$
declare i integer;
begin
    for i in (
        select car_id
        from rent
        group by car_id
        having count(car_id) >= count_to_remove)
    loop
        delete
        from car
        where car_id = i;
    end loop;

    commit;
end
$$;
