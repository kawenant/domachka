def farthest_point(points: list[tuple[int, int]]) -> tuple[int, int]:
    """
    Возвращает кортеж (x, y) — точку, наиболее удалённую от (0, 0).
    """
    return max(points, key=lambda p: p[0]**2 + p[1]**2)


points = [
    (1, 2),
    (3, 4),
    (-5, 1),
    (0, 6),
    (2, -3)]

result = farthest_point(points)
print(result)
# (-5, 1)   ← потому что 25 + 1 = 26 (максимум)