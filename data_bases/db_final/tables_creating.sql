CREATE TABLE IF NOT EXISTS city(
    city_id SERIAL PRIMARY KEY,
    title VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS street(
    street_id SERIAL PRIMARY KEY,
    title VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS address(
    address_id SERIAL PRIMARY KEY,
    city_id INT,
    street_id INT,
    house_number INT,
    FOREIGN KEY (city_id)
        REFERENCES city(city_id),
    FOREIGN KEY (street_id)
        REFERENCES street(street_id)
);

CREATE TABLE IF NOT EXISTS customer(
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    address_id INT,
    phone_number VARCHAR(255) UNIQUE NOT NULL,
    FOREIGN KEY (address_id)
        REFERENCES address(address_id)
);

CREATE TABLE IF NOT EXISTS branch(
    branch_id SERIAL PRIMARY KEY,
    address_id INT UNIQUE NOT NULL,
    phone_number varchar(20) UNIQUE NOT NULL,
    FOREIGN KEY (address_id)
        REFERENCES address(address_id)
);

CREATE TABLE IF NOT EXISTS brand(
    brand_id SERIAL PRIMARY KEY,
    title VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS model(
    model_id SERIAL PRIMARY KEY,
    brand_id INT,
    title VARCHAR(50) UNIQUE NOT NULL,
    FOREIGN KEY (brand_id)
        REFERENCES brand(brand_id)
);

CREATE TABLE IF NOT EXISTS car(
    car_id SERIAL PRIMARY KEY,
    branch_id INT,
    model_id INT,
    plate_number VARCHAR(50) UNIQUE NOT NULL,
    rental_price MONEY,
    FOREIGN KEY (model_id)
        REFERENCES model(model_id),
    FOREIGN KEY (branch_id)
        REFERENCES branch(branch_id)
);

CREATE TABLE IF NOT EXISTS rent(
    rent_id SERIAL PRIMARY KEY,
    customer_id INT,
    car_id INT,
    rental_date DATE,
    period INTERVAL,
    FOREIGN KEY (customer_id)
        REFERENCES customer(customer_id),
    FOREIGN KEY (car_id)
        REFERENCES car(car_id) ON DELETE CASCADE
);


DROP TABLE city CASCADE;
DROP TABLE street CASCADE;
DROP TABLE address CASCADE;
DROP TABLE customer CASCADE;
DROP TABLE branch CASCADE;
DROP TABLE brand CASCADE;
DROP TABLE model CASCADE;
DROP TABLE car CASCADE;
DROP TABLE rent CASCADE;
