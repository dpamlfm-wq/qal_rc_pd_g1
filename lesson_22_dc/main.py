from functools import reduce

from models import User, Transaction, Budget, TransactionType


def main():
    user = User(
        username="Olena",
        email="olena@example.com"
    )

    print("Користувач:")
    print(user.display())

    transactions = [
        Transaction(25000, TransactionType.INCOME, "Salary"),
        Transaction(5000, TransactionType.INCOME, "Freelance"),
        Transaction(450, TransactionType.EXPENSE, "Food"),
        Transaction(1200, TransactionType.EXPENSE, "Utilities"),
        Transaction(300, TransactionType.EXPENSE, "Transport"),
        Transaction(800, TransactionType.EXPENSE, "Food"),
        Transaction(2000, TransactionType.EXPENSE, "Clothes"),
        Transaction(1500, TransactionType.EXPENSE, "Entertainment"),
        Transaction(10000, TransactionType.INCOME, "Bonus"),
        Transaction(650, TransactionType.EXPENSE, "Food"),
    ]

    budgets = [
        Budget("Food", 5000, 1900),
        Budget("Transport", 1000, 300),
        Budget("Entertainment", 1200, 1500),
    ]

    # 1. Лише витрати
    expenses = list(
        filter(
            lambda t: t.is_expense(),
            transactions
        )
    )

    # 2. Лише доходи
    incomes = list(
        filter(
            lambda t: t.transaction_type == TransactionType.INCOME,
            transactions
        )
    )

    # 3. Загальна сума витрат
    total_expenses = reduce(
        lambda acc, t: acc + t.amount,
        expenses,
        0.0
    )

    # 4. Загальна сума доходів
    total_incomes = reduce(
        lambda acc, t: acc + t.amount,
        incomes,
        0.0
    )

    # 5. Витрати категорії Food
    food_expenses = list(
        map(
            lambda t: t.formatted(),
            filter(
                lambda t: t.category.lower() == "food",
                expenses
            )
        )
    )

    # 6. Сортування за сумою
    sorted_by_amount = sorted(
        transactions,
        key=lambda t: t.amount,
        reverse=True
    )

    balance = total_incomes - total_expenses

    print("\n" + "=" * 50)
    print("ФІНАНСОВИЙ ЗВІТ")
    print("=" * 50)

    print(f"\nДоходи:  +{total_incomes:.2f} UAH")
    print(f"Витрати: -{total_expenses:.2f} UAH")
    print(f"Баланс:   {balance:.2f} UAH")

    print("\nВитрати категорії Food:")
    for expense in food_expenses:
        print(expense)

    print("\nТранзакції за спаданням суми:")
    for transaction in sorted_by_amount:
        print(transaction.formatted())

    print("\nБюджети:")
    for budget in budgets:
        print(
            f"{budget.category}: "
            f"витрачено {budget.spent:.2f} / "
            f"{budget.monthly_limit:.2f} UAH | "
            f"залишок {budget.remaining():.2f} UAH | "
            f"використано {budget.utilization_pct():.1f}% | "
            f"перевищено: {budget.is_exceeded()}"
        )


if __name__ == "__main__":
    main()