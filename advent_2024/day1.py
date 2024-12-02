import pandas as pd


filepath = "advent_2024/inputs/day1.txt"
# filepath = "advent_2024/test_inputs/day1.txt" # for testing

def read_input_as_two_series() -> tuple[pd.Series, pd.Series]:
    """Read the weird space-separated format into pandas"""
    input_df = pd.read_csv(filepath, sep="   ", engine="python", header=None)
    return input_df[0], input_df[1]

# PART 1: sort values, then calcuate difference
def get_difference():
    series1, series2 = read_input_as_two_series()

    # pull out and sort the two lists
    sorted_1 = series1.sort_values().reset_index(drop=True)
    sorted_2 = series2.sort_values().reset_index(drop=True)

    # Get the differences between the two
    differences = (sorted_1 - sorted_2).abs()
    return differences.sum()

# PART 2: Find common numbers, multiply by # of occurances
def get_similarity_score():
    series1, series2 = read_input_as_two_series()
    list2_value_counts = series2.value_counts()

    total_score = 0
    for value in series1:
        num_occurances = list2_value_counts.get(value, 0)
        total_score += value * num_occurances

    return total_score

print("Part 1 Total difference:", get_difference())
print("Part 2 Similarity score:", get_similarity_score())