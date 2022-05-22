--
EXPLAIN ANALYSE
SELECT max(b.title) || ' ' || m.title,
       max(rental_price::numeric)
FROM car
    JOIN model m USING (model_id)
    JOIN brand b USING (brand_id)
GROUP BY m.model_id
ORDER BY max(rental_price) DESC
LIMIT 10;



--
EXPLAIN ANALYSE
SELECT c.first_name,
       c.last_name,
       car.rental_price
FROM rent
    JOIN customer c USING (customer_id)
    JOIN car USING (car_id)
WHERE rental_date = now();



--
EXPLAIN ANALYSE
SELECT c.title, s.title, a.house_number
FROM address a
    JOIN city c USING (city_id)
    JOIN street s USING (street_id)
ORDER BY c.title, s.title;

CREATE INDEX ON address (city_id);
CREATE INDEX ON address (street_id);


-- Sort  (cost=4513.78..4582.53 rows=27500 width=135) (actual time=39.246..40.273 rows=27500 loops=1)
-- "  Sort Key: c.title, s.title"
--   Sort Method: quicksort  Memory: 2915kB
--   ->  Hash Join  (cost=4.36..603.04 rows=27500 width=135) (actual time=0.052..14.172 rows=27500 loops=1)
--         Hash Cond: (a.city_id = c.city_id)
--         ->  Hash Join  (cost=2.24..522.61 rows=27500 width=21) (actual time=0.025..8.869 rows=27500 loops=1)
--               Hash Cond: (a.street_id = s.street_id)
--               ->  Seq Scan on address a  (cost=0.00..440.00 rows=28500 width=12) (actual time=0.003..2.064 rows=28500 loops=1)
--               ->  Hash  (cost=1.55..1.55 rows=55 width=17) (actual time=0.018..0.019 rows=55 loops=1)
--                     Buckets: 1024  Batches: 1  Memory Usage: 11kB
--                     ->  Seq Scan on street s  (cost=0.00..1.55 rows=55 width=17) (actual time=0.003..0.009 rows=55 loops=1)
--         ->  Hash  (cost=1.50..1.50 rows=50 width=122) (actual time=0.023..0.024 rows=50 loops=1)
--               Buckets: 1024  Batches: 1  Memory Usage: 11kB
--               ->  Seq Scan on city c  (cost=0.00..1.50 rows=50 width=122) (actual time=0.008..0.014 rows=50 loops=1)
-- Planning Time: 0.214 ms
-- Execution Time: 41.134 ms

-- Incremental Sort  (cost=82.88..4494.75 rows=27500 width=135) (actual time=0.743..31.096 rows=27500 loops=1)
-- "  Sort Key: c.title, s.title"
--   Presorted Key: c.title
--   Full-sort Groups: 50  Sort Method: quicksort  Average Memory: 30kB  Peak Memory: 30kB
--   Pre-sorted Groups: 50  Sort Method: quicksort  Average Memory: 67kB  Peak Memory: 67kB
--   ->  Nested Loop  (cost=0.58..2117.42 rows=27500 width=135) (actual time=0.028..16.664 rows=27500 loops=1)
--         ->  Nested Loop  (cost=0.43..1403.01 rows=28500 width=126) (actual time=0.020..7.251 rows=28500 loops=1)
--               ->  Index Scan using city_title_key on city c  (cost=0.14..12.89 rows=50 width=122) (actual time=0.006..0.025 rows=50 loops=1)
--               ->  Index Scan using address_city_id_idx on address a  (cost=0.29..22.10 rows=570 width=12) (actual time=0.004..0.083 rows=570 loops=50)
--                     Index Cond: (city_id = c.city_id)
--         ->  Memoize  (cost=0.15..0.17 rows=1 width=17) (actual time=0.000..0.000 rows=1 loops=28500)
--               Cache Key: a.street_id
--               Cache Mode: logical
--               Hits: 28443  Misses: 57  Evictions: 0  Overflows: 0  Memory Usage: 7kB
--               ->  Index Scan using street_pkey on street s  (cost=0.14..0.16 rows=1 width=17) (actual time=0.001..0.001 rows=1 loops=57)
--                     Index Cond: (street_id = a.street_id)
-- Planning Time: 0.351 ms
-- Execution Time: 31.856 ms
