EXPLAIN (ANALYSE)
SELECT *
FROM categories
    JOIN products p on categories.category_id = p.category_id
WHERE p.in_stock = 1;

CREATE INDEX products_category_id_idx ON products(category_id);

SET enable_seqscan TO on;

-- 1) WHEN MEMORY LESSER THEN NEED:
SET work_mem = '0.07MB';
-- Hash Right Join  (cost=10000000226.28..10000000516.13 rows=1 width=4) (actual time=43.459..44.898 rows=258 loops=1)
--   Hash Cond: (cp.products_product_id = products.product_id)
--   Filter: (cp.carts_cart_id IS NULL)
--   Rows Removed by Filter: 10995
--   ->  Seq Scan on cart_product cp  (cost=10000000000.00..10000000158.95 rows=10995 width=8) (actual time=0.009..0.888 rows=10995 loops=1)
--   ->  Hash  (cost=160.28..160.28 rows=4000 width=4) (actual time=41.004..41.005 rows=4000 loops=1)
--         Buckets: 4096  Batches: 4  Memory Usage: 68kB
--         ->  Index Only Scan using products_pkey on products  (cost=0.28..160.28 rows=4000 width=4) (actual time=0.010..0.384 rows=4000 loops=1)
--               Heap Fetches: 0
-- Planning Time: 0.142 ms
-- JIT:
--   Functions: 9
-- "  Options: Inlining true, Optimization true, Expressions true, Deforming true"
-- "  Timing: Generation 0.787 ms, Inlining 2.265 ms, Optimization 25.656 ms, Emission 11.989 ms, Total 40.698 ms"
-- Execution Time: 45.759 ms



-- 2) WHEN MEMORY ENOUGH:
SET work_mem = '5MB';
-- Hash Right Join  (cost=10000000210.28..10000000398.13 rows=1 width=4) (actual time=57.116..57.169 rows=258 loops=1)
--   Hash Cond: (cp.products_product_id = products.product_id)
--   Filter: (cp.carts_cart_id IS NULL)
--   Rows Removed by Filter: 10995
--   ->  Seq Scan on cart_product cp  (cost=10000000000.00..10000000158.95 rows=10995 width=8) (actual time=0.008..0.587 rows=10995 loops=1)
--   ->  Hash  (cost=160.28..160.28 rows=4000 width=4) (actual time=55.481..55.482 rows=4000 loops=1)
--         Buckets: 4096  Batches: 1  Memory Usage: 173kB
--         ->  Index Only Scan using products_pkey on products  (cost=0.28..160.28 rows=4000 width=4) (actual time=0.008..0.412 rows=4000 loops=1)
--               Heap Fetches: 0
-- Planning Time: 0.125 ms
-- JIT:
--   Functions: 10
-- "  Options: Inlining true, Optimization true, Expressions true, Deforming true"
-- "  Timing: Generation 0.842 ms, Inlining 2.257 ms, Optimization 33.777 ms, Emission 18.473 ms, Total 55.350 ms"
-- Execution Time: 58.059 ms
