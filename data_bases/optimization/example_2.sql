CREATE TEMPORARY TABLE t_a(
    a_id INT PRIMARY KEY,
    title VARCHAR(255)
);
CREATE INDEX ON t_a(a_id);

INSERT INTO t_a(a_id, title)
SELECT i, (random()::text)
    FROM generate_series(1, 1000000) as i;


CREATE TEMPORARY TABLE t_b(
    b_id INT REFERENCES t_a(a_id),
    other_title VARCHAR(255)
);

INSERT INTO t_b(b_id, other_title)
SELECT i, (random()::text)
    FROM generate_series(1000, 1000000) as i;


EXPLAIN (ANALYSE)
SELECT t_a.title, t_b.other_title
FROM t_a
    JOIN t_b tb on t_a.a_id = tb.b_id
WHERE t_a.a_id < 2000;

-- As result: run time optimized from 299.596 to 0.268


-- 1) BEFORE:
-- Merge Join  (cost=10000035550.49..10000072517.33 rows=29913 width=1040) (actual time=299.596..300.141 rows=1000 loops=1)
--   Merge Cond: (t_a.some_id = tb.other_id)
--   ->  Index Scan using t_a_some_id_idx on t_a  (cost=0.42..35161.75 rows=333333 width=520) (actual time=0.069..0.358 rows=1999 loops=1)
--         Index Cond: (some_id < 2000)
--   ->  Materialize  (cost=10000035550.07..10000035998.77 rows=89740 width=520) (actual time=243.602..243.785 rows=1001 loops=1)
--         ->  Sort  (cost=10000035550.07..10000035774.42 rows=89740 width=520) (actual time=243.598..243.688 rows=1001 loops=1)
--               Sort Key: tb.other_id
--               Sort Method: external merge  Disk: 32552kB
--               ->  Seq Scan on t_b tb  (cost=10000000000.00..10000007307.40 rows=89740 width=520) (actual time=0.038..83.158 rows=999001 loops=1)
-- Planning Time: 0.213 ms
-- JIT:
--   Functions: 9
-- "  Options: Inlining true, Optimization true, Expressions true, Deforming true"
-- "  Timing: Generation 0.892 ms, Inlining 3.020 ms, Optimization 34.108 ms, Emission 18.473 ms, Total 56.493 ms"
-- Execution Time: 306.831 ms


-- 2) AFTER:
CREATE INDEX ON t_b(b_id);
-- Merge Join  (cost=0.85..93416.03 rows=333000 width=1040) (actual time=0.268..0.814 rows=1000 loops=1)
--   Merge Cond: (t_a.some_id = tb.other_id)
--   ->  Index Scan using t_a_some_id_idx on t_a  (cost=0.42..35161.75 rows=333333 width=520) (actual time=0.039..0.328 rows=1999 loops=1)
--         Index Cond: (some_id < 2000)
--   ->  Index Scan using t_b_other_id_idx on t_b tb  (cost=0.42..51593.44 rows=999001 width=520) (actual time=0.029..0.166 rows=1001 loops=1)
-- Planning Time: 0.242 ms
-- Execution Time: 0.863 ms
