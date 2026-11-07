from sqlalchemy.orm import Session

from models import (
    User,
    Category,
    Transaction,
    Budget
)


class UserCRUD:

    @staticmethod
    def create(
        session: Session,
        username: str,
        email: str
    ):
        user = User(
            username=username,
            email=email
        )

        session.add(user)
        session.commit()
        session.refresh(user)

        return user

    @staticmethod
    def get_by_id(
        session: Session,
        user_id: int
    ):
        return (
            session.query(User)
            .filter(User.id == user_id)
            .first()
        )

    @staticmethod
    def get_all(session: Session):
        return session.query(User).all()

    @staticmethod
    def update(
        session: Session,
        user_id: int,
        **kwargs
    ):
        user = UserCRUD.get_by_id(
            session,
            user_id
        )

        if not user:
            return None

        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)

        session.commit()
        session.refresh(user)

        return user

    @staticmethod
    def delete(
        session: Session,
        user_id: int
    ):
        user = UserCRUD.get_by_id(
            session,
            user_id
        )

        if not user:
            return False

        session.delete(user)
        session.commit()

        return True


class CategoryCRUD:

    @staticmethod
    def create(
        session: Session,
        name: str,
        user_id: int
    ):
        category = Category(
            name=name,
            user_id=user_id
        )

        session.add(category)
        session.commit()
        session.refresh(category)

        return category

    @staticmethod
    def get_by_id(
        session: Session,
        category_id: int
    ):
        return (
            session.query(Category)
            .filter(Category.id == category_id)
            .first()
        )


class TransactionCRUD:

    @staticmethod
    def create(
        session: Session,
        amount: float,
        transaction_type: str,
        category_id: int,
        user_id: int,
        description: str = ""
    ):
        transaction = Transaction(
            amount=amount,
            transaction_type=transaction_type,
            category_id=category_id,
            user_id=user_id,
            description=description
        )

        session.add(transaction)
        session.commit()
        session.refresh(transaction)

        return transaction

    @staticmethod
    def get_by_id(
        session: Session,
        transaction_id: int
    ):
        return (
            session.query(Transaction)
            .filter(Transaction.id == transaction_id)
            .first()
        )

    @staticmethod
    def get_all(
        session: Session
    ):
        return session.query(Transaction).all()

    @staticmethod
    def delete(
        session: Session,
        transaction_id: int
    ):
        transaction = (
            session.query(Transaction)
            .filter(Transaction.id == transaction_id)
            .first()
        )

        if not transaction:
            return False

        session.delete(transaction)
        session.commit()

        return True


class BudgetCRUD:

    @staticmethod
    def create(
        session: Session,
        category_id: int,
        monthly_limit: float,
        month,
        user_id: int
    ):
        budget = Budget(
            category_id=category_id,
            monthly_limit=monthly_limit,
            month=month,
            user_id=user_id
        )

        session.add(budget)
        session.commit()
        session.refresh(budget)

        return budget

    @staticmethod
    def get_by_id(
        session: Session,
        budget_id: int
    ):
        return (
            session.query(Budget)
            .filter(Budget.id == budget_id)
            .first()
        )