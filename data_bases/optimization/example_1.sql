EXPLAIN (ANALYSE)
SELECT users.user_id, count(o.order_id)
FROM users
    JOIN carts c
        ON users.user_id = c.users_user_id
    LEFT JOIN _order o
        ON c.cart_id = o.carts_cart_id
GROUP BY user_id
HAVING count(o.order_id) = 0
LIMIT 5;

--As result: actual run time optimized from 323.601 to 2.495.


-- 1) BEFORE:
-- Limit  (cost=10000000190.22..10000022781.42 rows=5 width=12) (actual time=323.601..324.056 rows=5 loops=1)
--   ->  GroupAggregate  (cost=10000000190.22..10000045372.63 rows=10 width=12) (actual time=176.996..177.450 rows=5 loops=1)
--         Group Key: users.user_id
--         Filter: (count(o.order_id) = 0)
--         Rows Removed by Filter: 1500
--         ->  Nested Loop Left Join  (cost=10000000190.22..10000045337.63 rows=2000 width=8) (actual time=1.519..177.034 rows=1506 loops=1)
--               Join Filter: (c.cart_id = o.carts_cart_id)
--               Rows Removed by Join Filter: 2257500
--               ->  Merge Join  (cost=190.22..305.88 rows=2000 width=8) (actual time=1.506..2.180 rows=1506 loops=1)
--                     Merge Cond: (users.user_id = c.users_user_id)
--                     ->  Index Only Scan using users_pkey on users  (cost=0.28..121.28 rows=3000 width=4) (actual time=0.023..0.244 rows=1506 loops=1)
--                           Heap Fetches: 0
--                     ->  Sort  (cost=189.94..194.94 rows=2000 width=8) (actual time=1.474..1.563 rows=1506 loops=1)
--                           Sort Key: c.users_user_id
--                           Sort Method: quicksort  Memory: 142kB
--                           ->  Index Scan using carts_pkey on carts c  (cost=0.28..80.28 rows=2000 width=8) (actual time=0.427..1.207 rows=2000 loops=1)
--               ->  Materialize  (cost=10000000000.00..10000000035.50 rows=1500 width=8) (actual time=0.000..0.057 rows=1500 loops=1506)
--                     ->  Seq Scan on _order o  (cost=10000000000.00..10000000028.00 rows=1500 width=8) (actual time=0.008..0.183 rows=1500 loops=1)
-- Planning Time: 4.611 ms
-- JIT:
--   Functions: 18
-- "  Options: Inlining true, Optimization true, Expressions true, Deforming true"
-- "  Timing: Generation 2.440 ms, Inlining 8.902 ms, Optimization 78.584 ms, Emission 52.064 ms, Total 141.990 ms"
-- Execution Time: 326.626 ms


-- 2) AFTER:
CREATE INDEX carts_users_user_id_idx ON carts(users_user_id);
CREATE INDEX _order_carts_card_id_idx ON _order(carts_cart_id);
-- Limit  (cost=309.25..321.75 rows=5 width=12) (actual time=2.495..2.501 rows=5 loops=1)
--   ->  HashAggregate  (cost=309.25..334.25 rows=10 width=12) (actual time=2.494..2.498 rows=5 loops=1)
--         Group Key: users.user_id
--         Filter: (count(o.order_id) = 0)
--         Batches: 1  Memory Usage: 369kB
--         Rows Removed by Filter: 12
--         ->  Hash Left Join  (cost=86.09..299.25 rows=2000 width=8) (actual time=0.515..1.966 rows=2000 loops=1)
--               Hash Cond: (c.cart_id = o.carts_cart_id)
--               ->  Merge Join  (cost=0.56..191.22 rows=2000 width=8) (actual time=0.015..1.061 rows=2000 loops=1)
--                     Merge Cond: (users.user_id = c.users_user_id)
--                     ->  Index Only Scan using users_pkey on users  (cost=0.28..121.28 rows=3000 width=4) (actual time=0.007..0.217 rows=2001 loops=1)
--                           Heap Fetches: 0
--                     ->  Index Scan using carts_users_user_id_idx on carts c  (cost=0.28..80.28 rows=2000 width=8) (actual time=0.006..0.374 rows=2000 loops=1)
--               ->  Hash  (cost=66.78..66.78 rows=1500 width=8) (actual time=0.494..0.495 rows=1500 loops=1)
--                     Buckets: 2048  Batches: 1  Memory Usage: 75kB
--                     ->  Index Scan using _order_carts_card_id_idx on _order o  (cost=0.28..66.78 rows=1500 width=8) (actual time=0.006..0.310 rows=1500 loops=1)
-- Planning Time: 0.546 ms
-- Execution Time: 2.550 ms
