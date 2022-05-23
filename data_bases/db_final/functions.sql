-- uses cursor & loop
create or replace function customer_rented_cars(c_id integer)
returns text
as $$
declare
    cur_car cursor(c_id integer)
        for
        select
               brand.title as b_title,
               model.title as m_title,
               car.plate_number
        from rent
            join car using (car_id)
            join model using (model_id)
            join brand using (brand_id)
        where customer_id = c_id;

    rented_cars text default '';
    car_rec record;
begin
    select first_name || ' ' || customer.last_name
    into rented_cars
    from customer
    where customer_id = c_id;
    rented_cars = upper(rented_cars) || ': ';

    open cur_car(c_id);
    loop
        fetch cur_car into car_rec;

        exit when not FOUND;

        rented_cars := rented_cars || ','
                       || car_rec.b_title || ' '
                       || car_rec.m_title || ' '
                       || car_rec.plate_number;

    end loop;
    close cur_car;

    rented_cars = rented_cars || ';';

    return rented_cars;
end
$$
language plpgsql;

select customer_rented_cars(2);


-- returns table
create or replace function top_rented_models(top integer)
returns table(
    model varchar,
    rents_count bigint)
language plpgsql
as $$
begin
    return query
        select model.title, count(model_id)
        from rent
            join car using (car_id)
            join model using (model_id)
        group by model.title
        order by count(model_id) DESC
        limit top;
end
$$;

select * from top_rented_models(10);
