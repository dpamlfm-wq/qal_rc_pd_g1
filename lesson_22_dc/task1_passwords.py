# Завдання 1. Охоронці воріт

passwords = [
    "Cossack1",
    "sich",
    "ZAPORIZHZHIA2024",
    "Sich Gate 5",
    "Mazepa99",
    "короткий1",
    "BohunTheBrave",
    "D0br0nich!",
    "аааааааА1",
    "Valid1Pass",
]


def is_strong(password):
    return (
        8 <= len(password) <= 20
        and any(char.isdigit() for char in password)
        and any(char.isupper() for char in password)
        and " " not in password
    )


strong_passwords = list(
    filter(lambda p: is_strong(p), passwords)
)

weak_passwords = list(
    filter(lambda p: not is_strong(p), passwords)
)

print("Надійні паролі:")
for password in strong_passwords:
    print(f"✅ {password} — надійний")

print("\nНенадійні паролі:")
for password in weak_passwords:
    print(f"❌ {password} — відхилено")