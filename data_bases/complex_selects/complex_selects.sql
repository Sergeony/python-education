---Task 1---
CREATE TABLE potential_customer(
    id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    name VARCHAR(255),
    surname VARCHAR(255),
    second_name VARCHAR(255),
    city VARCHAR(255)
);


INSERT INTO potential_customer(email, name, surname, second_name, city) VALUES
('smth1@email.com', 'sm_name1', 'sm_surname1', 'sm_second_name1', 'city 17'),
('smth2@email.com', 'sm_name2', 'sm_surname2', 'sm_second_name2', 'city 12'),
('smth3@email.com', 'sm_name3', 'sm_surname3', 'sm_second_name3', 'city 13'),
('smth4@email.com', 'sm_name4', 'sm_surname4', 'sm_second_name4', 'city 14'),
('smth5@email.com', 'sm_name5', 'sm_surname5', 'sm_second_name5', 'city 15');


SELECT name, email
FROM potential_customer
WHERE city = 'city 17'
UNION
SELECT first_name, email
FROM users
WHERE city = 'city 17';



---Task 2---
SELECT first_name, email
FROM users
ORDER BY city, first_name;



---Task 3--
SELECT c.category_title, count(c.category_id)
FROM products
    JOIN categories c
        ON products.category_id = c.category_id
GROUP BY c.category_id
ORDER BY count(c.category_id) DESC;



---Task 4---
---1)---
SELECT products.product_id
FROM products
    LEFT JOIN cart_product cp
        ON products.product_id = cp.products_product_id
WHERE cp.carts_cart_id IS NULL;


---2)---
SELECT products.product_id, count(cp.carts_cart_id) as count_in_cart
FROM products
    LEFT JOIN cart_product cp
        ON products.product_id = cp.products_product_id
    LEFT JOIN _order o
        ON cp.carts_cart_id = o.carts_cart_id
GROUP BY product_id
HAVING count(o.order_id) = 0;


---3)---
SELECT products.product_id, count(product_id)
FROM products
    JOIN cart_product cp
        ON products.product_id = cp.products_product_id
GROUP BY product_id
ORDER BY count(product_id) DESC
LIMIT 10;


---4)---
SELECT products.product_id, count(product_id)
FROM products
    JOIN cart_product cp
        ON products.product_id = cp.products_product_id
    JOIN _order o
        ON cp.carts_cart_id = o.carts_cart_id
GROUP BY product_id
ORDER BY count(product_id) DESC
LIMIT 10;


---5)---
SELECT users.user_id, sum(o.total)
FROM users
    JOIN carts c
        ON users.user_id = c.users_user_id
    JOIN _order o
        ON c.cart_id = o.carts_cart_id
GROUP BY user_id
ORDER BY sum(o.total) DESC
LIMIT 5;


---6)---
SELECT users.user_id, count(o.order_id)
FROM users
    JOIN carts c
        ON users.user_id = c.users_user_id
    JOIN _order o
        ON c.cart_id = o.carts_cart_id
GROUP BY user_id
ORDER BY count(o.order_id) DESC
LIMIT 5;


---7)---
SELECT users.user_id, count(o.order_id)
FROM users
    JOIN carts c
        ON users.user_id = c.users_user_id
    LEFT JOIN _order o
        ON c.cart_id = o.carts_cart_id
GROUP BY user_id
HAVING count(o.order_id) = 0
--ORDER BY count(o.order_id) -- the same way --
LIMIT 5;
