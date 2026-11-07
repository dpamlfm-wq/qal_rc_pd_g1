from database import SessionLocal

from crud_operations import (
    UserCRUD,
    CategoryCRUD,
    TransactionCRUD
)


def test_user_crud():
    print("=== USER CRUD TEST ===\n")

    session = SessionLocal()

    try:
        print("1. CREATE USER")

        user = UserCRUD.create(
            session=session,
            username="olena_test",
            email="olena_test@example.com"
        )

        print(f"✅ User created: {user.id}")

        print("\n2. READ USER")

        found_user = UserCRUD.get_by_id(
            session,
            user.id
        )

        print(f"✅ Found: {found_user.username}")

        print("\n3. UPDATE USER")

        updated_user = UserCRUD.update(
            session,
            user.id,
            currency="USD"
        )

        print(f"✅ Currency updated: {updated_user.currency}")

        print("\n4. DELETE USER")

        deleted = UserCRUD.delete(
            session,
            user.id
        )

        print(f"✅ Deleted: {deleted}")

    finally:
        session.close()


def test_transaction_crud():
    print("\n=== TRANSACTION CRUD TEST ===\n")

    session = SessionLocal()

    try:
        user = UserCRUD.create(
            session=session,
            username="expense_user_0261107",
            email="expense_user_0261107@example.com"
        )

        category = CategoryCRUD.create(
            session=session,
            name="Food",
            user_id=user.id
        )

        transaction = TransactionCRUD.create(
            session=session,
            amount=250.50,
            transaction_type="expense",
            category_id=category.id,
            user_id=user.id,
            description="Supermarket"
        )

        print(
            f"✅ Transaction created: "
            f"{transaction.id}"
        )

        found = TransactionCRUD.get_by_id(
            session,
            transaction.id
        )

        print(
            f"✅ Transaction amount: "
            f"{found.amount}"
        )

        deleted = TransactionCRUD.delete(
            session,
            transaction.id
        )

        print(
            f"✅ Transaction deleted: "
            f"{deleted}"
        )

        #UserCRUD.delete(
         #   session,
          #  user.id
        #)

    finally:
        session.close()


if __name__ == "__main__":
    print("🚀 START TESTS\n")

    test_user_crud()
    test_transaction_crud()

    print("\n✅ ALL TESTS PASSED")