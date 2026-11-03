def sum_integers(start, stop, step=1):
    total = 0
    for number in range(start, stop, step):
        total += number
    return total


if __name__ == "__main__":
    print("All:", sum_integers(1, 101))
    print("Odd:", sum_integers(1, 101, 2))
    print("Even:", sum_integers(2, 101, 2))
