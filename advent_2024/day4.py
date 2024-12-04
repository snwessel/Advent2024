
# filepath = "advent_2024/inputs/day4.txt"
filepath = "advent_2024/test_inputs/day4.txt" # for testing

def get_input_as_list() -> list[str]:
    lines = []
    with open(filepath, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def count_horizontal_words(list_of_lines: list[str]) -> int:
    """This function can be reused as the matrix of letters is transposed"""
    total = 0
    for line in list_of_lines:
        total += line.count('XMAS')
        total += line.count('SAMX')
    return total

def part1():
    list_of_lines = get_input_as_list()
    # Count horizontal words
    return count_horizontal_words(list_of_lines)
    
    pass

def part2():
    pass

print("Part 1:", part1())
print("Part 2:", part2())
