def mailing_intersection(buyers: list[str], subscribers: list[str]) -> set[str]:
    """
    Возвращает множество email, которым нужно отправить письмо
    (пересечение покупателей и подписчиков).
    """
    return set(buyers) & set(subscribers)


# Пример использования
buyers = [
    "alice@example.com",
    "bob@example.com",
    "carol@example.com",
    "dave@example.com"
]

subscribers = [
    "bob@example.com",
    "carol@example.com",
    "eve@example.com",
    "frank@example.com"
]

result = mailing_intersection(buyers, subscribers)
print(result)
# {'bob@example.com', 'carol@example.com'}