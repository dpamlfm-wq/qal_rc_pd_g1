import psycopg

DSN = "postgresql://postgres:Postgres2026!@localhost:5432/lesson_30_test"

try:
    with psycopg.connect(DSN) as conn:

        print("✅ Успішно підключені до PostgreSQL!")

        with conn.cursor() as cur:

            cur.execute("SELECT version();")
            print(cur.fetchone()[0])

            cur.execute("SELECT current_user;")
            print(cur.fetchone()[0])

            cur.execute("SELECT current_database();")
            print(cur.fetchone()[0])

except psycopg.Error as e:
    print(f"❌ Помилка: {e}")