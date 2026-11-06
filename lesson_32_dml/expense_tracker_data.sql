INSERT INTO users
(first_name, last_name, email)
VALUES
('Olena', 'Nikitenko', 'olena@email.com'),
('Anna', 'Koval', 'anna@email.com'),
('Ivan', 'Petrenko', 'ivan@email.com');

INSERT INTO categories
(user_id, name)
VALUES
(1, 'Food'),
(1, 'Transport'),
(2, 'Health');

INSERT INTO expenses
(user_id, category_id, amount, expense_date, description)
VALUES
(1, 1, 350.50, '2026-11-01', 'Supermarket'),
(1, 2, 120.00, '2026-11-02', 'Bus ticket'),
(2, 3, 500.00, '2026-11-03', 'Pharmacy');