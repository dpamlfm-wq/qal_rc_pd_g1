Expense Tracker Database
Опис
База даних призначена для обліку особистих витрат користувачів.

Користувач може створювати категорії витрат та додавати витрати до цих категорій.

Кожна витрата містить суму, дату та опис.

Сутності
Users
id
first_name
last_name
email
Categories
id
user_id
name
Expenses
id
user_id
category_id
amount
expense_date
description
Зв'язки
User -> Categories (1:N)
User -> Expenses (1:N)
Category -> Expenses (1:N)
Використані обмеження
PRIMARY KEY
FOREIGN KEY
UNIQUE
NOT NULL
CHECK
DEFAULT