from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class TransactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"


@dataclass
class User:
    username: str
    email: str
    currency: str = "UAH"

    def display(self) -> str:
        return f"{self.username} <{self.email}>"


@dataclass
class Transaction:
    amount: float
    transaction_type: TransactionType
    category: str
    date: date = field(default_factory=date.today)
    description: str = ""

    def is_expense(self) -> bool:
        return self.transaction_type == TransactionType.EXPENSE

    def formatted(self) -> str:
        sign = "+" if self.transaction_type == TransactionType.INCOME else "-"
        return (
            f"{sign} {self.amount:.2f} UAH "
            f"[{self.category}] {self.date}"
        )


@dataclass
class Budget:
    category: str
    monthly_limit: float
    spent: float = 0.0

    def remaining(self) -> float:
        return self.monthly_limit - self.spent

    def is_exceeded(self) -> bool:
        return self.spent > self.monthly_limit

    def utilization_pct(self) -> float:
        if self.monthly_limit == 0:
            return 0.0

        return (self.spent / self.monthly_limit) * 100