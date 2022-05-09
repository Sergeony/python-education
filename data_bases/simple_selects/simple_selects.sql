--task 1--
SELECT *
FROM users;

SELECT *
FROM products;

SELECT *
FROM order_status;



--task 2--
SELECT *
FROM _order
WHERE order_status_order_status_id = 4;



--task 3--
SELECT *
FROM products
WHERE price > 80.00
  AND price <= 150.00;


SELECT *
FROM _order
WHERE created_at > '2020.10.01';


SELECT *
FROM _order
WHERE created_at >= '2020.01.01'
  AND created_at <= '2020.06.30';


SELECT *
FROM products
WHERE category_id IN (7, 11, 18);


SELECT *
FROM _order
WHERE order_status_order_status_id NOT IN (4, 5)
  AND updated_at <= '2020.12.31';


SELECT *
FROM carts
LEFT JOIN _order o ON carts.cart_id = o.carts_cart_id
WHERE o.order_id IS NULL;



--task 4--
SELECT avg(total)
FROM _order
WHERE order_status_order_status_id = 4;


SELECT max(total)
FROM _order
WHERE created_at >= '2020.07.01'
  AND created_at <= '2020.09.30';
