CREATE INDEX idx_expenses_user_id
ON expenses(user_id);

CREATE INDEX idx_expenses_category_id
ON expenses(category_id);

EXPLAIN ANALYZE
SELECT *
FROM expenses
WHERE user_id = 1;