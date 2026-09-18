def total_receipt(items: list[tuple[str, int, int]]) -> int:
    """
    Возвращает общую сумму чека.
    """
    return sum(quantity * price for name, quantity, price in items)

receipt = [
    ("Хлеб", 2, 45),
    ("Молоко", 1, 89),
    ("Яблоки", 3, 120),
    ("Сыр", 1, 350)]

result = total_receipt(receipt)
print(result)
# 2*45 + 1*89 + 3*120 + 1*350 = 90 + 89 + 360 + 350 = 889