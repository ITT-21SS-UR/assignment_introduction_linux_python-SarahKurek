import math
import sys

# stats.py:
# Reads in a list of floating point numbers either from a textfile
# passed as an argument to the script or via stdin.
# Numbers are separated by space characters and may contain
# either , or . as decimal separator.
# Prints out the mean, median, and standard deviation for these on stdout.
# The script should only use built-in commands, the math module
# (for math.sqrt() ), and the sys module (for sys.argv and sys.stdin ).


def read_file(filename):
    with open(filename) as f:
        return read_stream(f)


def read_stream(stream):
    content = stream.readlines()
    return parse_data(content)


def read_stdin():
    return parse_data(sys.stdin)


def parse_data(data):
    tmp = []

    for i in data:
        tmp.extend(i.replace(',', '.').replace('\n', ' ').split(' '))

    data = list(filter(None, tmp))

    return list(map(float, data))


def calculate_mean(numbers):
    sum = 0.0

    for i in numbers:
        sum += i

    return sum / len(numbers)


def calculate_median(numbers):
    numbers = sorted(numbers)
    mid_pos = int(len(numbers) / 2)

    if len(numbers) % 2 == 0:
        return (numbers[mid_pos] + numbers[mid_pos - 1]) / 2

    return float(numbers[mid_pos])


def calculate_sd(numbers):
    mean = calculate_mean(numbers)

    if len(numbers) < 2:
        return "nan"

    sum = 0
    for i in numbers:
        sum += math.pow((i - mean), 2)

    variance = sum / (len(numbers) - 1)

    return math.sqrt(variance)


def print_statistics(numbers):
    sys.stdout.write("The mean is: " + str(calculate_mean(numbers)) + ", \n"
                     + "the median is: " +
                     str(calculate_median(numbers)) + " and \n"
                     + "the standard deviation is: "
                     + str(calculate_sd(numbers)) + "\n")


if __name__ == "__main__":
    arguments_len = len(sys.argv)

    if arguments_len == 1:
        numbers = read_stdin()

    elif arguments_len == 2:
        numbers = read_file(sys.argv[1])

    print_statistics(numbers)
