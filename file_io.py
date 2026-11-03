import argparse
from pathlib import Path
from tempfile import TemporaryDirectory

from points import farthest_pair, read_points

SAMPLE = "point:\np1: 1.0, 1.0\np2: 2.0, 2.0\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, nargs="?")
    parser.add_argument("output", type=Path, nargs="?", default=Path("result.txt"))
    args = parser.parse_args()

    try:
        with TemporaryDirectory(dir=args.output.parent) as folder:
            source = args.input
            if source is None:
                source = Path(folder) / "points.txt"
                source.write_text(SAMPLE, encoding="utf-8")
                print(source.read_text(encoding="utf-8"), end="")
            if source.resolve() == args.output.resolve():
                raise ValueError("Input and output must be different files")
            points = read_points(source)
            for point in points:
                print(f"{point.name}: x={point.x:g}, y={point.y:g}")
            a, b, length = farthest_pair(points)
            result = f"{a.name} - {b.name}: {length:.6f}"
            args.output.write_text(result + "\n", encoding="utf-8")
            print(result)
    except (OSError, ValueError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()

