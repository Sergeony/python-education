---Task 1: see the numbers after the update transaction is completed.---
BEGIN ISOLATION LEVEL READ COMMITTED;

SELECT phone_number FROM users
LIMIT 10;

COMMIT;



--Task 2: see new customers after the next transaction.---
BEGIN ISOLATION LEVEL REPEATABLE READ;

SELECT * FROM potential_customer;

COMMIT;



---Task 3: unsuccessful attempt to delete customers already deleted in the other session.---
BEGIN ISOLATION LEVEL SERIALIZABLE;

DELETE FROM potential_customer
WHERE email SIMILAR TO 'unknown%';

SELECT * FROM potential_customer;

COMMIT;
