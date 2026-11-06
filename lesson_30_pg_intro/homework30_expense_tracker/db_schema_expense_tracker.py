import psycopg

ADMIN_DSN = "postgresql://postgres:Postgres2026!@localhost:5432/postgres"
DSN = "postgresql://postgres:Postgres2026!@localhost:5432/expense_tracker"


def create_database():
    try:

        with psycopg.connect(ADMIN_DSN, autocommit=True) as conn:
            with conn.cursor() as cur:
                cur.execute("DROP DATABASE IF EXISTS expense_tracker;")
                cur.execute("CREATE DATABASE expense_tracker;")

        print("✅ База даних expense_tracker створена")

        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:

                cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(100) UNIQUE NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    currency VARCHAR(3) DEFAULT 'UAH',
                    created_at TIMESTAMP DEFAULT NOW()
                );
                """)

                cur.execute("""
                CREATE TABLE IF NOT EXISTS categories (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    user_id INTEGER NOT NULL,
                    FOREIGN KEY (user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE
                );
                """)

                cur.execute("""
                CREATE TABLE IF NOT EXISTS transactions (
                    id SERIAL PRIMARY KEY,
                    amount DECIMAL(10,2) NOT NULL,
                    transaction_type VARCHAR(20) NOT NULL,
                    category_id INTEGER,
                    description TEXT,
                    user_id INTEGER NOT NULL,
                    transaction_date DATE DEFAULT CURRENT_DATE,

                    FOREIGN KEY (category_id)
                    REFERENCES categories(id)
                    ON DELETE SET NULL,

                    FOREIGN KEY (user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE
                );
                """)

                cur.execute("""
                CREATE TABLE IF NOT EXISTS budgets (
                    id SERIAL PRIMARY KEY,
                    category_id INTEGER NOT NULL,
                    monthly_limit DECIMAL(10,2) NOT NULL,
                    month DATE NOT NULL,
                    user_id INTEGER NOT NULL,

                    FOREIGN KEY (category_id)
                    REFERENCES categories(id)
                    ON DELETE CASCADE,

                    FOREIGN KEY (user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE
                );
                """)

                conn.commit()

        print("✅ Таблиці створені")
        print("✅ users")
        print("✅ categories")
        print("✅ transactions")
        print("✅ budgets")

    except psycopg.Error as e:
        print(f"❌ Помилка: {e}")


if __name__ == "__main__":
    create_database()
