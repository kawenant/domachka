def calculate_position():
    # Получаем данные
    name = input("Название товара: ")
    price = float(input("Цена за единицу: "))
    quantity = int(input("Количество: "))
    promo = input("Участвует в акции? (да/нет): ").strip().lower()

    # Базовая сумма без скидок
    total = price * quantity

    # Определяем размер скидки
    discount = 0
    if quantity >= 5:
        discount += 10
    if promo in ("да", "yes", "y", "д"):
        discount += 15

    # Применяем скидку
    final_sum = total * (1 - discount / 100)

    # Вывод результата
    print("\n--- Результат ---")
    print(f"Товар: {name}")
    print(f"Количество: {quantity}")
    print(f"Цена за единицу: {price:.2f}")
    print(f"Сумма без скидки: {total:.2f}")
    print(f"Скидка: {discount}%")
    print(f"Итоговая сумма: {final_sum:.2f}")


# Запуск программы
if __name__ == "__main__":
    calculate_position()