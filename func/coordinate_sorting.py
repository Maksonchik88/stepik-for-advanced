points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]


def coordinate_sorting(coordinates: tuple) -> int:
    return (coordinates[0]**2 + coordinates[1]**2)**0.5


sort_points = sorted(points, key=coordinate_sorting)
print(sort_points)


