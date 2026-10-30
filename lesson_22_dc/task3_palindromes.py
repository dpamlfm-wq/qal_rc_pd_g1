# Завдання 3. Пошук козацьких шифрів

messages = [
    "А роза упала на лапу азора",
    "Козак",
    "Зараз",
    "level",
    "Python",
    "А баба",
    "racecar",
    "Запоріжжя",
    "noon",
    "Мазепа",
]


def is_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


# 1. Знаходимо всі паліндроми
cipher_messages = list(
    filter(
        lambda message: is_palindrome(message),
        messages
    )
)

# 2. Форматуємо результат через map
formatted_messages = list(
    map(
        lambda message:
        f"🔐 {message} → {message.replace(' ', '').lower()[::-1]}",
        cipher_messages
    )
)

# 3. Виводимо результат
print("Козацькі шифри:")

for message in formatted_messages:
    print(message)