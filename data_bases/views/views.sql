--Task 1: products
CREATE OR REPLACE VIEW product_view_for_users AS
    SELECT
        product_title,
        product_description,
        price
    FROM products
    ORDER BY price;

DROP VIEW product_view_for_users;

--USAGES:
SELECT *
FROM product_view_for_users
LIMIT 10;

SELECT product_title, price
FROM product_view_for_users;



--Task 2: order_status & order
CREATE OR REPLACE VIEW recent_orders_with_statuses AS
    SELECT
        order_id,
        os.status_name,
        created_at,
        total
    FROM _order
        JOIN order_status os
            ON _order.order_status_order_status_id = os.order_status_id
    ORDER BY (created_at, total) DESC;

DROP VIEW recent_orders_with_statuses;

-- USAGES:
SELECT * FROM recent_orders_with_statuses
LIMIT 10;

SELECT order_id, status_name
FROM recent_orders_with_statuses
LIMIT 10;



--Task 3: categories & products
CREATE OR REPLACE VIEW biggest_categories_in_stock AS
    SELECT
        categories.category_id, sum(p.in_stock)
    FROM categories
        JOIN products p USING (category_id)
    GROUP BY categories.category_id
    ORDER BY sum(p.in_stock) DESC;

DROP VIEW biggest_categories_in_stock;

--USAGES:
SELECT * FROM biggest_categories_in_stock
LIMIT 10;



--Task 4: materialized view
CREATE MATERIALIZED VIEW most_added_categories AS
    SELECT ct.category_title, count(p.product_id)
    FROM carts c
        JOIN cart_product cp
            ON c.cart_id = cp.carts_cart_id
        JOIN products p
            ON cp.products_product_id = p.product_id
        JOIN categories ct
            ON p.category_id = ct.category_id
    GROUP BY ct.category_id
    ORDER BY count(p.product_id) DESC
WITH NO DATA;

DROP MATERIALIZED VIEW most_added_categories;

--USAGES:
REFRESH MATERIALIZED VIEW most_added_categories;
SELECT * FROM most_added_categories;
