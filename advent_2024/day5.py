
filepath = "advent_2024/inputs/day5.txt"
# filepath = "advent_2024/test_inputs/day5.txt" # for testing

def get_input_rules_and_updates() -> tuple[list[tuple[str, str]], list[list[str]]]:
    """
    Get the set of rules as a list of tuples.
    Get the set of updates as a list of lists of numbers.
    """
    rules = []
    updates = []
    reached_end_of_rules = False

    with open(filepath, 'r') as f:
        for line in f:
            stripped_line = line.strip()
            if stripped_line == "":
                reached_end_of_rules = True
            elif reached_end_of_rules:
                values = stripped_line.split(",")
                updates.append(values)
            else:
                values = stripped_line.split("|")
                rules.append(tuple(values))
    return rules, updates

def is_update_valid(update: list[str], rules: list[tuple[str, str]]) -> bool:
    for rule_val1, rule_val2 in rules:
        rule_is_applicable = (rule_val1 in update and rule_val2 in update)
        if rule_is_applicable:
            index1 = update.index(rule_val1)
            index2 = update.index(rule_val2)
            # if the rule is broken, then the update is not valid
            if index1 > index2:
                return False
    # If all rules have passed, the udpate is valid
    return True


def part1():
    rules, updates = get_input_rules_and_updates()

    total_sum = 0
    for update in updates:
        update_is_valid = is_update_valid(update, rules)
        if update_is_valid:
            print("VALID UPDATE", update)
            middle_index = len(update) // 2 # integer division rounds down
            total_sum += int(update[middle_index])
    return total_sum

def part2():
    pass # TODO:

print("Part 1:", part1())
print("Part 2:", part2())
