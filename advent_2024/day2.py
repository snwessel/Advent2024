import pandas as pd


filepath = "advent_2024/inputs/day2.txt"
# filepath = "advent_2024/test_inputs/day2.txt" # for testing

def read_input_as_dataframe() -> pd.DataFrame:
    """Read the weird space-separated format into pandas"""
    return pd.read_csv(filepath, sep=" ", header=None)

def is_record_safe(record: pd.Series):
    value_changes = record.diff().dropna()
    # "The levels are either all increasing or all decreasing."
    if not ((value_changes > 0).all() or (value_changes < 0).all()):
        return False
    # "Any two adjacent levels differ by at least one and at most three."
    if (value_changes == 0).any():
        return False
    if (value_changes.abs() > 3).any():
        return False
    return True

def part1():
    input_df = read_input_as_dataframe()
    safe_record_count = 0
    for index, record in input_df.iterrows():
        if is_record_safe(record):
            safe_record_count += 1
    return safe_record_count

# PART 2

def is_record_safe_with_dampener(record: pd.Series):
    """Would the record be safe if one bad entry were removed"""
    if is_record_safe(record):
        return True
    # For the dampener, let's try brute force first!
    for i in record.index:
        temp_record = record.drop(i) 
        if is_record_safe(temp_record):
            return True
        
    return False



def part2():
    input_df = read_input_as_dataframe()
    safe_record_count = 0
    for index, record in input_df.iterrows():
        if is_record_safe_with_dampener(record):
            safe_record_count += 1
    return safe_record_count


print("Part 1:", part1())
print("Part 2:", part2())
