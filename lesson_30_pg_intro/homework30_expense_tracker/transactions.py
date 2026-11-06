import psycopg

DSN = "postgresql://postgres:Postgres2026!@localhost:5432/expense_tracker"

print("=== TRANSACTIONS ===")

try:
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:

            cur.execute(
                """
                INSERT INTO users(username, email)
                VALUES(%s, %s)
                """,
                ("transaction_user", "transaction@gmail.com")
            )

            conn.commit()

            print("✅ COMMIT успішний")

except psycopg.Error as e:
    print(f"❌ Помилка: {e}")