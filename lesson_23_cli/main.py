import logging

from config import get_settings
from cli import build_parser


def main():
    settings = get_settings()

    logging.basicConfig(
        level=settings["log_level"],
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(
                "expense_tracker.log",
                encoding="utf-8"
            ),
            logging.StreamHandler(),
        ],
    )

    parser = build_parser()
    args = parser.parse_args()

    if args.command == "add":
        sign = "+" if args.transaction_type == "income" else "-"

        print(
            f"✅ {sign}{args.amount} "
            f"{settings['base_currency']} "
            f"[{args.category}] додано"
        )

    elif args.command == "list":
        print(
            "📋 Транзакції "
            "(фільтри ще не підключені до storage)"
        )

    elif args.command == "balance":
        print(
            "💰 Баланс: "
            "(підключіть storage)"
        )

    elif args.command == "report":
        month = getattr(args, "month", None)

        if not month:
            month = "поточний місяць"

        print(
            f"📊 Звіт за {month}: "
            f"(підключіть storage)"
        )

    elif args.command == "delete":
        print(
            f"🗑️ Транзакцію #{args.id} видалено"
        )

    elif args.command == "budget":

        if args.budget_command == "set":
            print(
                f"📌 Ліміт для "
                f"'{args.category}': "
                f"{args.limit} "
                f"{settings['base_currency']}"
            )

        elif args.budget_command == "show":
            print(
                "📊 Бюджети: "
                "(підключіть storage)"
            )

    elif args.command == "export":
        print(
            f"📤 Експорт у форматі "
            f"{args.format.upper()}"
        )


if __name__ == "__main__":
    main()