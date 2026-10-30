import functools
import inspect
import logging
import time


def chronicle(chronicler="Анонімний"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logging.info(
                f"[Літописець: {chronicler}] "
                f"Викликано: {func.__name__}{args}"
            )

            result = func(*args, **kwargs)

            logging.info(f"[Результат]: {result}")

            return result

        return wrapper

    return decorator


def guard(secret):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            password = input("Назви пароль: ")

            if password == secret:
                logging.info(
                    f"Доступ надано: {func.__name__}"
                )
                return func(*args, **kwargs)

            logging.warning(
                f"Невдала спроба доступу до: "
                f"{func.__name__}"
            )

            print("Стій! Доступ заборонено.")
            return None

        return wrapper

    return decorator


def retry(times=3, delay=1.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            for attempt in range(1, times + 1):

                try:
                    result = func(*args, **kwargs)

                    logging.info(
                        f"Успіх на спробі "
                        f"{attempt}/{times}"
                    )

                    return result

                except Exception as error:

                    logging.warning(
                        f"Спроба {attempt}/{times} "
                        f"не вдалася: {error}"
                    )

                    if attempt == times:
                        logging.error(
                            "Усі спроби вичерпано"
                        )
                        raise

                    time.sleep(delay)

        return wrapper

    return decorator


def log_transaction(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        if result is not None:
            logging.info(
                f"{func.__name__}: "
                f"args={args[1:]}, "
                f"kwargs={kwargs}"
            )

        return result

    return wrapper


def validate_amount(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        amount = None

        if "amount" in kwargs:
            amount = kwargs["amount"]

        elif len(args) > 1:
            amount = args[1]

        if not isinstance(
                amount,
                (int, float)
        ):
            logging.warning(
                f"Некоректний тип суми: "
                f"{amount}"
            )
            return None

        if amount <= 0:
            logging.warning(
                f"Сума має бути > 0. "
                f"Отримано: {amount}"
            )
            return None

        return func(*args, **kwargs)

    return wrapper


def currency_aware(
        base_currency="UAH"
):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            logging.debug(
                f"[currency_aware] "
                f"Конвертація ще не реалізована. "
                f"Базова валюта: "
                f"{base_currency}"
            )

            return func(
                *args,
                **kwargs
            )

        return wrapper

    return decorator
