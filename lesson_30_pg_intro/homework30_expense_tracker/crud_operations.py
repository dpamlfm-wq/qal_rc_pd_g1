import psycopg

DSN = "postgresql://postgres:Postgres2026!@localhost:5432/expense_tracker"

with psycopg.connect(DSN) as conn:
    with conn.cursor() as cur:

        print("=== CREATE ===")

        cur.execute(
            """
            INSERT INTO users(username, email)
            VALUES(%s, %s)
            RETURNING id;
            """,
            ("olena", "olena@gmail.com")
        )

        user_id = cur.fetchone()[0]
        conn.commit()

        print("Створено користувача ID =", user_id)

        print("\n=== READ ===")

        cur.execute(
            "SELECT * FROM users WHERE id = %s;",
            (user_id,)
        )

        print(cur.fetchone())

        print("\n=== UPDATE ===")

        cur.execute(
            """
            UPDATE users
            SET email=%s
            WHERE id=%s;
            """,
            ("olena_new@gmail.com", user_id)
        )

        conn.commit()

        cur.execute(
            "SELECT * FROM users WHERE id=%s;",
            (user_id,)
        )

        print(cur.fetchone())

        print("\n=== DELETE ===")

        cur.execute(
            "DELETE FROM users WHERE id=%s;",
            (user_id,)
        )

        conn.commit()

        print("✅ Користувач видалений")