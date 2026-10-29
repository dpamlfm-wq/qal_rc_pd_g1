import logging
import random

from decorators import (
    chronicle,
    guard,
    retry,
    log_transaction,
    validate_amount,
    currency_aware,
)


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(
            "expense_tracker.log",
            encoding="utf-8"
        ),
        logging.StreamHandler()
    ]
)


@chronicle("Самійло Величко")
def make_decision(action, target):
    return f"Рішення: {action} → {target}"


@chronicle()
def count_warriors(regiment):
    return 500


@guard(secret="Мамай")
def open_treasury():
    print("Скарбниця відчинена!")
    return "золото, срібло, зброя"


@retry(times=4, delay=0.5)
def unreliable_scout():
    if random.random() < 0.7:
        raise ConnectionError(
            "Розвідник не повернувся"
        )

    return "Ворог за річкою!"


class ExpenseTracker:

    @log_transaction
    @validate_amount
    @currency_aware()
    def add_income(
            self,
            amount,
            category,
            description=""
    ):
        print(
            f"Дохід: {amount} грн "
            f"| {category}"
        )

        return True

    @log_transaction
    @validate_amount
    @currency_aware()
    def add_expense(
            self,
            amount,
            category,
            description=""
    ):
        print(
            f"Витрата: {amount} грн "
            f"| {category}"
        )

        return True

    @log_transaction
    def delete_transaction(
            self,
            transaction_id
    ):
        print(
            f"Транзакцію "
            f"{transaction_id} видалено"
        )

        return True


def main():

    print("=== Завдання 1 ===")

    make_decision(
        "Атакувати",
        "Перекоп"
    )

    count_warriors(
        "Полтавський"
    )

    print("\n=== Завдання 2 ===")

    open_treasury()

    print("\n=== Завдання 3 ===")

    try:
        result = unreliable_scout()
        print(result)

    except Exception as error:
        print(error)

    print("\n=== Expense Tracker ===")

    tracker = ExpenseTracker()

    tracker.add_income(
        15000,
        "Salary"
    )

    tracker.add_expense(
        350,
        "Food"
    )

    tracker.add_expense(
        -100,
        "Transport"
    )

    tracker.delete_transaction(
        5
    )

    print(
        "\nПеревірте файл:"
    )
    print(
        "expense_tracker.log"
    )


if __name__ == "__main__":
    main()