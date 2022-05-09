CREATE TABLE IF NOT EXISTS Users(
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    middle_name VARCHAR(255),
    is_staff SMALLINT,
    country VARCHAR(255),
    city VARCHAR(255),
    address TEXT
);


CREATE TABLE IF NOT EXISTS Carts(
    cart_id SERIAL PRIMARY KEY ,
    Users_user_id INT,
    FOREIGN KEY (Users_user_id)
        REFERENCES Users (user_id),
    subtotal DECIMAL,
    total DECIMAL,
    timestamp TIMESTAMP(2)
);


CREATE TABLE IF NOT EXISTS Categories(
    category_id SERIAL PRIMARY KEY,
    category_title VARCHAR(255),
    category_description TEXT
);


CREATE TABLE IF NOT EXISTS Products(
    product_id SERIAL PRIMARY KEY,
    product_title VARCHAR(255),
    product_description TEXT,
    in_stock INT,
    price FLOAT,
    slug VARCHAR(45),
    category_id INT,
    FOREIGN KEY (category_id)
        REFERENCES Categories (category_id)
);


CREATE TABLE IF NOT EXISTS Cart_product(
    carts_cart_id INT,
    products_product_id INT,
    FOREIGN KEY (carts_cart_id)
        REFERENCES Carts (cart_id),
    FOREIGN KEY (products_product_id)
         REFERENCES Products (product_id)
);


CREATE TABLE IF NOT EXISTS Order_status(
    order_status_id SERIAL PRIMARY KEY,
    status_name VARCHAR(255)
);


CREATE TABLE IF NOT EXISTS _Order(
    order_id SERIAL PRIMARY KEY,
    Carts_cart_id INT,
    FOREIGN KEY (Carts_cart_id)
        REFERENCES Carts(cart_id),
    Order_status_order_status_id INT,
    FOREIGN KEY (Order_status_order_status_id)
        REFERENCES Order_status(order_status_id),
    shipping_total DECIMAL,
    total DECIMAL,
    created_at TIMESTAMP(2),
    updated_at TIMESTAMP(2)
);


COPY Users FROM '/usr/src/users.csv' WITH (FORMAT csv);
COPY Carts FROM '/usr/src/carts.csv' WITH (FORMAT csv);
COPY Categories FROM '/usr/src/categories.csv' WITH (FORMAT csv);
COPY Products FROM '/usr/src/products.csv' WITH (FORMAT csv);
COPY Cart_product FROM '/usr/src/cart_products.csv' WITH (FORMAT csv);
COPY Order_status FROM '/usr/src/order_statuses.csv' WITH (FORMAT csv);
COPY _Order FROM '/usr/src/orders.csv' WITH (FORMAT csv);


ALTER TABLE Users ADD phone_number INT;
ALTER TABLE Users ALTER COLUMN phone_number TYPE VARCHAR;


UPDATE Products SET price = price * 2;
