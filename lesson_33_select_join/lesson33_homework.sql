-- lesson33_homework.sql
-- Author: Olena Nikitenko

-- 1. Опубліковані курси дорожчі за 1000, від дорожчих до дешевших
SELECT c.id, c.title, c.price
FROM lms_courses c
WHERE c.published = TRUE
  AND c.price > 1000
ORDER BY c.price DESC;

-- 2. Студенти з email на @example.com, відсортовані за прізвищем
SELECT u.last_name, u.first_name, u.email
FROM lms_users u
WHERE u.role = 'student'
  AND u.email LIKE '%@example.com'
ORDER BY u.last_name, u.first_name;

-- 3. Три найгірші оцінки (лише виставлені)
SELECT s.id, s.user_id, s.score
FROM lms_submissions s
WHERE s.score IS NOT NULL
ORDER BY s.score ASC
LIMIT 3;

-- 4. Завдання з max_score не менше 80 і датою не пізніше 15.10.2026
SELECT a.id, a.title, a.max_score, a.due_date
FROM lms_assignments a
WHERE a.max_score >= 80
  AND a.due_date <= '2026-10-15'
ORDER BY a.due_date;

-- 5. Знизити ціну курсу SQL Basics на 100 і повернути змінений рядок
BEGIN;

UPDATE lms_courses
SET price = price - 100
WHERE title = 'SQL Basics'
RETURNING id, title, price;

ROLLBACK;

-- 6. Позначити запис користувача 5 на курс 1 як completed
BEGIN;

UPDATE lms_enrollments
SET status = 'completed'
WHERE user_id = 5
  AND course_id = 1
RETURNING user_id, course_id, status;

ROLLBACK;

-- 7. Видалити відповіді без оцінки до завдання 4
BEGIN;

DELETE FROM lms_submissions
WHERE assignment_id = 4
  AND score IS NULL
RETURNING id, user_id, assignment_id;

ROLLBACK;

-- 8. JOIN: назва курсу і прізвище викладача для всіх курсів
SELECT c.title, u.last_name
FROM lms_courses c
JOIN lms_users u
    ON u.id = c.teacher_id
ORDER BY c.title;

-- 9. JOIN: студент, курс і статус лише для активних записів
SELECT u.last_name, c.title, e.status
FROM lms_enrollments e
JOIN lms_users u
    ON u.id = e.user_id
JOIN lms_courses c
    ON c.id = e.course_id
WHERE e.status = 'active'
ORDER BY c.title, u.last_name;

-- 10. LEFT JOIN: курси, на які ніхто не записаний
SELECT c.title
FROM lms_courses c
LEFT JOIN lms_enrollments e
    ON e.course_id = c.id
WHERE e.user_id IS NULL
ORDER BY c.title;