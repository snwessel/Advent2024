import numpy as np

filepath = "advent_2024/inputs/day4.txt"
# filepath = "advent_2024/test_inputs/day4.txt" # for testing

def get_input_char_matrix() -> list[list[str]]:
    """Raed the input as a matrix of characters"""
    char_matrix = []
    with open(filepath, 'r') as f:
        for line in f:
            char_matrix.append(list(line.strip()))
    return char_matrix

def count_horizontal_words(char_matrix: np.ndarray[str]) -> int:
    """This function can be reused as the matrix of letters is transposed"""
    total = 0
    for line in char_matrix:
        line_as_string = ''.join(line)
        total += line_as_string.count('XMAS')
        total += line_as_string.count('SAMX')
    return total

def part1():
    total_count = 0
    char_matrix = np.array(get_input_char_matrix())

    # Count horizontal words
    total_count += count_horizontal_words(char_matrix)

    # Transpose the matrix to count the vertical words
    transposed_matrix = char_matrix.transpose()
    total_count += count_horizontal_words(transposed_matrix)

    # Now get all of the diagonals
    col_len, row_len = char_matrix.shape
    forward_diags = [[] for _ in range(row_len + col_len - 1)]
    back_diags = [[] for _ in range(len(forward_diags))]
    min_back_diag = -row_len + 1

    for x in range(col_len):
        for y in range(row_len):
            forward_diags[x+y].append(char_matrix[y][x])
            back_diags[x-y-min_back_diag].append(char_matrix[y][x])
    total_count += count_horizontal_words(forward_diags)
    total_count += count_horizontal_words(back_diags)

    return total_count
    

def part2():
    matrix = get_input_char_matrix()

    row_len = len(matrix)
    col_len = len(matrix[0])
    count = 0

    # Check for X-MAS patterns
    # Iterate through each possible center-point of the X (all but the outer-most points)
    for x in range(1, row_len - 1):
        for y in range(1, col_len - 1):
            center_point = matrix[x][y]
            # if the center point isn't "A", it's not worth considering
            if center_point == "A": 
                top_left_point = matrix[x-1][y-1]
                top_right_point = matrix[x+1][y-1]
                bottom_left_point = matrix[x-1][y+1]
                bottom_right_point = matrix[x+1][y+1]
                
                right_diag = {top_left_point, bottom_right_point}
                left_diag = {bottom_left_point, top_right_point}
                if right_diag == {"M", "S"} and left_diag == {"M", "S"}:
                    count += 1
    return count

print("Part 1:", part1())
print("Part 2:", part2())
