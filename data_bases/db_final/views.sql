--
CREATE OR REPLACE VIEW full_car_info AS
    SELECT *
    FROM car
        JOIN model USING (model_id)
        JOIN brand USING (brand_id);

DROP VIEW full_car_info;


--
CREATE OR REPLACE VIEW full_address AS
    SELECT c.title,
           s.title,
           a.house_number
    FROM address a
        JOIN city c USING (city_id)
        JOIN street s USING (street_id);

DROP VIEW full_address;


--
CREATE MATERIALIZED VIEW top_rental_cities AS
    SELECT c.title,
           count(rent_id) AS rents_in_city
    FROM rent
        JOIN car USING (car_id)
        JOIN branch b USING (branch_id)
        JOIN address a USING (address_id)
        JOIN city c USING (city_id)
    GROUP BY c.city_id
    ORDER BY count(rent_id)
WITH NO DATA;

DROP MATERIALIZED VIEW top_rental_cities;

REFRESH MATERIALIZED VIEW top_rental_cities;
SELECT * FROM top_rental_cities;
