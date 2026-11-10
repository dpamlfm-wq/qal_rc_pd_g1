from functools import reduce

raw_registry = [
    "  іван сірко  | полковник | 150",
    "БОГДАН ХМЕЛЬНИЦЬКИЙ | гетьман | 10000",
    "петро дорошенко|сотник|75",
    "  Іван Мазепа | гетьман | 30000 ",
    "семен палій  |  полковник  | 500",
    "  Григорій Сковорода | філософ | 0",
]


def parse_record(record):
    name, rank, warriors = map(str.strip, record.split("|"))

    return {
        "name": name.title(),
        "rank": rank.title(),
        "warriors": int(warriors)
    }


# 1. map -> словники
registry = list(map(parse_record, raw_registry))

# 2. filter -> тільки ті, у кого воїнів більше 0
active_registry = list(
    filter(
        lambda person: person["warriors"] > 0,
        registry
    )
)

# 3. reduce -> загальна кількість воїнів
total_warriors = reduce(
    lambda total, person: total + person["warriors"],
    active_registry,
    0
)

# 4. sorted -> за кількістю воїнів (спадання)
sorted_registry = sorted(
    active_registry,
    key=lambda person: person["warriors"],
    reverse=True
)

print(
    f"Козацький реєстр ({len(sorted_registry)} записів)"
)
print("─" * 55)
print(
    f"{'№':<3} {'Імʼя':<22} {'Посада':<12} {'Воїни':>8}"
)
print("─" * 55)

for index, person in enumerate(sorted_registry, start=1):
    print(
        f"{index:<3} "
        f"{person['name']:<22} "
        f"{person['rank']:<12} "
        f"{person['warriors']:>8}"
    )

print("─" * 55)
print(f"Разом воїнів: {total_warriors}")