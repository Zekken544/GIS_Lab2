from dataclasses import dataclass
from math import dist, isfinite


@dataclass(frozen=True)
class Point:
    name: str
    x: float
    y: float

    def distance_to(self, other):
        return dist((self.x, self.y), (other.x, other.y))


def farthest_three(points):
    if len(points) != 3:
        raise ValueError("Exactly three points are required")
    longest = -1
    for index in range(3):
        a, b = points[index], points[(index + 1) % 3]
        distance = a.distance_to(b)
        if distance > longest:
            best, longest = (a, b), distance
    return *best, longest


def farthest_pair(points):
    if len(points) < 2:
        raise ValueError("At least two points are required")
    longest = -1
    for i, a in enumerate(points):
        for j in range(i + 1, len(points)):
            b = points[j]
            distance = a.distance_to(b)
            if distance > longest:
                best, longest = (a, b), distance
    return *best, longest


def read_points(path):
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    if not lines or lines[0].strip() not in ("point:", "point;"):
        raise ValueError("Expected a point: or point; header")
    separator = lines[0].strip()[-1]
    points = []
    for number, line in enumerate(lines[1:], 2):
        if not line.strip():
            continue
        try:
            if separator == ":" and ":" not in line:
                records = [(None, item) for item in line.split(";")]
            else:
                name, coordinates = line.split(separator, 1)
                records = [(name.strip(), coordinates)]
            for name, coordinates in records:
                x, y = map(float, coordinates.split(","))
                if not all(map(isfinite, (x, y))) or name == "":
                    raise ValueError
                points.append(Point(name or f"p{len(points) + 1}", x, y))
        except ValueError as error:
            raise ValueError(f"Invalid point on line {number}: {line}") from error
    return points


if __name__ == "__main__":
    sample = [Point("p1", 0, 0), Point("p2", 3, 4), Point("p3", 1, 1), Point("p4", 6, 8)]
    for result in (farthest_three(sample[:3]), farthest_pair(sample)):
        a, b, length = result
        print(f"{a.name} - {b.name}: {length:g}")
