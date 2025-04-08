# Write a function that takes two numbers and finds the average between the two.


def average(num1, num2):
    sum = num1 + num2
    return sum / 2


def main():
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)

    final_average = average(avg_1, avg_2)
    print("avg_1: ", avg_1)
    print("avg_2: ", avg_2)
    print("Final Average: ", final_average)


if __name__ == "__main__":
    main()
