-- homework35_expense_tracker.sql
-- Author: Olena Nikitenko

/* =====================================================
   GROUP BY / HAVING
   ===================================================== */

-- 1. Скільки витрат у кожній категорії
SELECT
    c.name AS category_name,
    COUNT(e.id) AS expense_count
FROM categories c
LEFT JOIN expenses e
    ON e.category_id = c.id
GROUP BY c.id, c.name
ORDER BY expense_count DESC;

-- 2. Загальна сума витрат по кожному користувачу
SELECT
    u.first_name,
    u.last_name,
    SUM(e.amount) AS total_expenses
FROM users u
JOIN expenses e
    ON e.user_id = u.id
GROUP BY u.id, u.first_name, u.last_name
ORDER BY total_expenses DESC;

-- 3. Категорії, де більше однієї витрати
SELECT
    c.name,
    COUNT(e.id) AS expense_count
FROM categories c
JOIN expenses e
    ON e.category_id = c.id
GROUP BY c.id, c.name
HAVING COUNT(e.id) > 1;

/* =====================================================
   SUBQUERIES
   ===================================================== */

-- 4. Витрати більші за середню суму всіх витрат
SELECT
    id,
    amount,
    expense_date
FROM expenses
WHERE amount >
(
    SELECT AVG(amount)
    FROM expenses
);

-- 5. Корельований підзапит:
-- витрати більші за середню суму у своїй категорії
SELECT
    e1.id,
    e1.amount,
    e1.category_id
FROM expenses e1
WHERE e1.amount >
(
    SELECT AVG(e2.amount)
    FROM expenses e2
    WHERE e2.category_id = e1.category_id
);

/* =====================================================
   DISTINCT ON
   ===================================================== */

-- 6. Остання витрата в кожній категорії
SELECT DISTINCT ON (category_id)
    category_id,
    id,
    amount,
    expense_date
FROM expenses
ORDER BY category_id, expense_date DESC;

/* =====================================================
   WINDOW FUNCTIONS
   ===================================================== */

-- 7. Рейтинг витрат за сумою
SELECT
    id,
    amount,
    RANK() OVER (
        ORDER BY amount DESC
    ) AS expense_rank
FROM expenses;

-- 8. Накопичувальна сума витрат
SELECT
    id,
    expense_date,
    amount,
    SUM(amount) OVER (
        ORDER BY expense_date
    ) AS running_total
FROM expenses;

/* =====================================================
   VIEWS
   ===================================================== */

-- 9. Представлення з повною інформацією про витрати

CREATE OR REPLACE VIEW v_expense_details AS
SELECT
    e.id,
    u.first_name,
    u.last_name,
    c.name AS category_name,
    e.amount,
    e.expense_date,
    e.description
FROM expenses e
JOIN users u
    ON u.id = e.user_id
JOIN categories c
    ON c.id = e.category_id;

-- Перевірка
SELECT * FROM v_expense_details;

-- 10. Представлення статистики категорій

CREATE OR REPLACE VIEW v_category_summary AS
SELECT
    c.id,
    c.name,
    COUNT(e.id) AS expense_count,
    COALESCE(SUM(e.amount), 0) AS total_amount,
    COALESCE(AVG(e.amount), 0) AS avg_amount
FROM categories c
LEFT JOIN expenses e
    ON e.category_id = c.id
GROUP BY c.id, c.name;

-- Перевірка
SELECT * FROM v_category_summary;