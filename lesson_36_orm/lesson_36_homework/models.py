from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Date,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    username = Column(
        String(100),
        unique=True,
        nullable=False
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    currency = Column(
        String(3),
        default="UAH"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    categories = relationship(
        "Category",
        back_populates="user"
    )

    transactions = relationship(
        "Transaction",
        back_populates="user"
    )

    budgets = relationship(
        "Budget",
        back_populates="user"
    )

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)

    name = Column(
        String(100),
        nullable=False
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    user = relationship(
        "User",
        back_populates="categories"
    )

    transactions = relationship(
        "Transaction",
        back_populates="category"
    )

    budgets = relationship(
        "Budget",
        back_populates="category"
    )

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)

    amount = Column(
        Float,
        nullable=False
    )

    transaction_type = Column(
        String(20),
        nullable=False
    )

    category_id = Column(
        Integer,
        ForeignKey("categories.id"),
        nullable=True
    )

    description = Column(String)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    transaction_date = Column(Date)

    user = relationship(
        "User",
        back_populates="transactions"
    )

    category = relationship(
        "Category",
        back_populates="transactions"
    )

    def __repr__(self):
        return f"<Transaction(id={self.id}, amount={self.amount})>"


class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True)

    category_id = Column(
        Integer,
        ForeignKey("categories.id")
    )

    monthly_limit = Column(Float)

    month = Column(Date)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    user = relationship(
        "User",
        back_populates="budgets"
    )

    category = relationship(
        "Category",
        back_populates="budgets"
    )

    def __repr__(self):
        return f"<Budget(id={self.id})>"
    