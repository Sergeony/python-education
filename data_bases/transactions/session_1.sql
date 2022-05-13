---Task 1: add random numbers to the user table.---
BEGIN ISOLATION LEVEL READ COMMITTED;

SAVEPOINT blank_number;

UPDATE users
SET phone_number = floor(random()*899999999 + 100000000);

SELECT * FROM users
LIMIT 10;

ROLLBACK TO blank_number;

COMMIT;



---Task 2: insert some new potential customers.---
BEGIN ISOLATION LEVEL READ COMMITTED;

INSERT INTO potential_customer(email, name, surname, second_name, city) VALUES
    ('unknown1@gmail.com', 'unknown1', 'unknowenko1', 'unknownovich1', 'smth1'),
    ('unknown2@gmail.com', 'unknown2', 'unknowenko2', 'unknownovich2', 'smth2'),
    ('unknown3@gmail.com', 'unknown3', 'unknowenko3', 'unknownovich3', 'smth3'),
    ('unknown4@gmail.com', 'unknown4', 'unknowenko4', 'unknownovich4', 'smth4');

SELECT * FROM potential_customer;

ROLLBACK;

COMMIT;



---Task 3: delete newly inserted customers.---
BEGIN ISOLATION LEVEL READ COMMITTED;

SAVEPOINT undo_deleting;

DELETE FROM potential_customer
WHERE email LIKE 'unknown%';

SELECT * FROM potential_customer;

ROLLBACK TO undo_deleting;

COMMIT;
