import psycopg

DSN = "postgresql://postgres:Postgres2026!@localhost:5432/expense_tracker"

with psycopg.connect(DSN) as conn:
    with conn.cursor() as cur:

        dangerous_username = "admin'; DROP TABLE users; --"

        cur.execute(
            """
            SELECT *
            FROM users
            WHERE username = %s;
            """,
            (dangerous_username,)
        )

        result = cur.fetchall()

        print("✅ Запит виконано безпечно")
        print("Кількість записів:", len(result))

        print("\nПриклад небезпечного рядка:")
        print(dangerous_username)