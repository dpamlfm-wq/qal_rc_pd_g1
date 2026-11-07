-- homework34_expense_tracker.sql
-- Author: Olena Nikitenko

-- =====================================================
-- 1. Усі витрати від найбільшої до найменшої суми
-- Очікується: усі записи з таблиці expenses
-- =====================================================

SELECT e.id, e.amount, e.expense_date, e.description
FROM expenses e
ORDER BY e.amount DESC;

-- =====================================================
-- 2. Витрати від 100 до 500 грн
-- Очікується: записи в заданому діапазоні
-- =====================================================

SELECT e.id, e.amount, e.expense_date
FROM expenses e
WHERE e.amount BETWEEN 100 AND 500
ORDER BY e.amount;

-- =====================================================
-- 3. Категорії із назвою Food
-- Очікується: 1 або кілька рядків
-- =====================================================

SELECT c.id, c.name
FROM categories c
WHERE c.name ILIKE '%food%';

-- =====================================================
-- 4. Топ-3 найбільші витрати
-- Очікується: 3 рядки
-- =====================================================

SELECT e.id, e.amount, e.expense_date
FROM expenses e
ORDER BY e.amount DESC
LIMIT 3;

-- =====================================================
-- 5. Витрати з даними користувача
-- Бізнес-питання: хто здійснив витрату?
-- =====================================================

SELECT
    e.id,
    u.first_name,
    u.last_name,
    e.amount,
    e.expense_date
FROM expenses e
INNER JOIN users u
    ON u.id = e.user_id;

-- =====================================================
-- 6. Витрати та їх категорії
-- Бізнес-питання: до якої категорії належить витрата?
-- =====================================================

SELECT
    e.id,
    c.name AS category_name,
    e.amount,
    e.expense_date
FROM expenses e
INNER JOIN categories c
    ON c.id = e.category_id;

-- =====================================================
-- 7. Повна інформація про витрати
-- Бізнес-питання: користувач + категорія + сума
-- =====================================================

SELECT
    u.first_name,
    u.last_name,
    c.name AS category_name,
    e.amount,
    e.expense_date
FROM expenses e
INNER JOIN users u
    ON u.id = e.user_id
INNER JOIN categories c
    ON c.id = e.category_id
ORDER BY e.amount DESC;

-- =====================================================
-- 8. Усі категорії та прив'язані витрати
-- Бізнес-питання: чи є витрати в категорії?
-- =====================================================

SELECT
    c.name,
    e.amount,
    e.expense_date
FROM categories c
LEFT JOIN expenses e
    ON e.category_id = c.id;

-- =====================================================
-- 9. Категорії без жодної витрати
-- Бізнес-питання: які категорії не використовуються?
-- =====================================================

SELECT
    c.id,
    c.name
FROM categories c
LEFT JOIN expenses e
    ON e.category_id = c.id
WHERE e.id IS NULL;

-- =====================================================
-- 10. Користувачі без жодної витрати
-- Бізнес-питання: хто ще не додав витрати?
-- =====================================================

SELECT
    u.id,
    u.first_name,
    u.last_name
FROM users u
LEFT JOIN expenses e
    ON e.user_id = u.id
WHERE e.id IS NULL;