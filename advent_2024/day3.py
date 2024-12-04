import re 

filepath = "advent_2024/inputs/day3.txt"
# filepath = "advent_2024/test_inputs/day3.txt" # for testing

# pulls out the two numbers in mul operations (as separate groups)
mul_regex = r"mul\((\d{1,3}),(\d{1,3})\)" 

# identifies both mul operations and do/dont operations
valid_section_regex = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
# full_regex = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

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
    input_text = read_input_file()
    total = 0
    do_operations = True

    operations = re.findall(valid_section_regex, input_text)
    for operation in operations:
        if operation == "do()":
            do_operations = True
        elif operation == "don't()":
            do_operations = False
        mul_operation_match = re.search(mul_regex, operation)
        if mul_operation_match and do_operations:
            product = int(mul_operation_match.group(1)) * int(mul_operation_match.group(2))
            total += product
    return total

print("Part 1:", part1())
print("Part 2:", part2())
