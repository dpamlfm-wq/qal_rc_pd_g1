import psycopg

DSN = "postgresql://postgres:Postgres2026!@localhost:5432/expense_tracker"

with psycopg.connect(DSN) as conn:
    with conn.cursor() as cur:

        # очищаємо тестові дані
        cur.execute("DELETE FROM budgets;")
        cur.execute("DELETE FROM transactions;")
        cur.execute("DELETE FROM categories;")
        cur.execute("DELETE FROM users;")

        # користувач
        cur.execute("""
            INSERT INTO users(username, email)
            VALUES(%s, %s)
            RETURNING id;
        """, ("anna", "anna@gmail.com"))

        user_id = cur.fetchone()[0]

        # категорія
        cur.execute("""
            INSERT INTO categories(name, user_id)
            VALUES(%s, %s)
            RETURNING id;
        """, ("Food", user_id))

        conn.commit()

        # JOIN
        cur.execute("""
            SELECT
                u.username,
                c.name
            FROM users u
            INNER JOIN categories c
                ON u.id = c.user_id;
        """)

        rows = cur.fetchall()

        print("=== JOIN RESULT ===")

        for row in rows:
            print(row)