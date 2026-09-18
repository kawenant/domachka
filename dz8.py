def count_underperformers(sales: list[float], plan: float) -> int:
    """
    Возвращает число сотрудников, не выполнивших план продаж.
    """
    return sum(1 for amount in sales if amount < plan)


# Пример использования
sales = [120000, 95000, 150000, 87000, 110000, 99000]
plan = 100000

result = count_underperformers(sales, plan)
print(result)
