-- ====================
-- POSITIVE TEST
-- ====================

INSERT INTO users
(first_name, last_name, email)
VALUES
('Olena', 'Nikitenko', 'olena@email.com');

INSERT INTO categories
(user_id, name)
VALUES
(1, 'Food');

INSERT INTO expenses
(user_id, category_id, amount, expense_date, description)
VALUES
(1, 1, 350.50, '2026-11-06', 'Supermarket');

-- ====================
-- NEGATIVE TEST 1
-- UNIQUE
-- ====================

INSERT INTO users
(first_name, last_name, email)
VALUES
('Olena', 'Nikitenko', 'olena@email.com');

-- ====================
-- NEGATIVE TEST 2
-- CHECK
-- ====================

INSERT INTO expenses
(user_id, category_id, amount, expense_date)
VALUES
(1, 1, -50, '2026-11-06');

-- ====================
-- NEGATIVE TEST 3
-- FOREIGN KEY
-- ====================

INSERT INTO expenses
(user_id, category_id, amount, expense_date)
VALUES
(999, 999, 100, '2026-11-06');