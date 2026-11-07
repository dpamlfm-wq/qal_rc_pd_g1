from database import Base, engine
from models import User, Category, Transaction, Budget


def init_db():
    """
    Створення таблиць у базі даних
    """
    Base.metadata.create_all(bind=engine)

    print("✅ Таблиці успішно створені!")
    print("\n📋 Створені таблиці:")

    for table_name in Base.metadata.tables.keys():
        print(f"  - {table_name}")


if __name__ == "__main__":
    print("🔄 Ініціалізація бази даних...")

    init_db()

    print("\n✅ База даних готова до роботи!")