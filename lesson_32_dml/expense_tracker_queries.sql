-- LIKE
SELECT * FROM categories
WHERE name ILIKE '%food%';

-- ORDER BY
SELECT * FROM expenses
ORDER BY amount DESC;

-- LIMIT
SELECT * FROM expenses
ORDER BY amount DESC
LIMIT 3;

-- BETWEEN
SELECT * FROM expenses
WHERE amount BETWEEN 100 AND 500;

-- IS NULL
SELECT * FROM expenses
WHERE description IS NULL;

-- UPDATE
UPDATE expenses
SET amount = 400.00
WHERE id = 1;

-- DELETE
DELETE FROM expenses
WHERE id = 3;