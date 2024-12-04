import re 

filepath = "advent_2024/inputs/day3.txt"
# filepath = "advent_2024/test_inputs/day3.txt" # for testing

mul_regex = r"mul\((\d{1,3}),(\d{1,3})\)" # pulls out the two numberes (as separate grouops)

def read_input_file() -> str:
    file = open(filepath, "r")
    content = file.read()
    file.close()
    return content

def part1():
    input_text = read_input_file()
    total = 0

    mul_operations = re.findall(mul_regex, input_text)
    for number1, number2 in mul_operations:
        product = int(number1) * int(number2)
        total += product

    return total


def part2():
    pass

print("Part 1:", part1())
print("Part 2:", part2())
