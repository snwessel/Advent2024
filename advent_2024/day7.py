import operator
from functools import reduce

# TODO: there is something wrong with my solution here. It's off by 

filepath = "advent_2024/inputs/day7.txt"
# filepath = "advent_2024/test_inputs/day7.txt" # for testing

def get_input_as_list_of_tuples() -> list[tuple[int, list[int]]]:
    """Raed the input as a matrix of characters"""
    output = []
    with open(filepath, 'r') as f:
        for line in f:
            key, value = line.split(":")
            val_list = value.strip().split(" ")
            output.append((int(key), [int(v) for v in val_list]))
    return output

def compute_options(left_options: list[int], right_val: int):
    """
    Function that should be passed into the "reduce" method.
    """
    # Base case
    if left_options == []:
        return [right_val]
    
    # Otherwise, return all combinations of (left+right) and (left*right)
    new_options = []
    for left_val in left_options:
        new_options.append(left_val+right_val)
        new_options.append(right_val*left_val)
        new_options.append(int(str(left_val) + str(right_val))) # line added for part 2
    return new_options

def get_all_possible_combos(values: list[int]):
    return reduce(compute_options, values, [])

def part1():
    input_list = get_input_as_list_of_tuples()
    
    total = 0
    for key, val_list in input_list:
        possible_combos = get_all_possible_combos(val_list)
        if key in possible_combos:
            total += key
            
            print(key)
    return total

def part2():
    # just added a line to part 1
    pass


# Example: 480991
# Input: 480991: 52 75 1 91 966
# Actual from running: (matches manually computed below)
# manually computed (does not include expected): [1185, 211554, 12614, 11251968, 1184, 210588, 12523, 11164062, 4958, 3856272, 355957, 342921306, 4957, 3855306, 355866, 342833400]


print("Part 1:", part1())
print("Part 2:", part2())
