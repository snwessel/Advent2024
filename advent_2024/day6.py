import numpy as np

filepath = "advent_2024/inputs/day6.txt"
# filepath = "advent_2024/test_inputs/day6.txt" # for testing

def get_input_char_matrix() -> np.ndarray:
    """Raed the input as a matrix of characters"""
    char_matrix = []
    with open(filepath, 'r') as f:
        for line in f:
            char_matrix.append(list(line.strip()))
    return np.array(char_matrix)

def get_guard_position(matrix: np.ndarray) -> tuple[int, int]:
    for i in range(matrix.shape[0]): # iterate through rows
        for j in range(matrix.shape[1]): # iterate through row values
            value = matrix[i][j]
            if value == "^":
                return (i, j)
            
def guard_is_on_map(matrix_shape: tuple[int, int], guard_pos: tuple[int, int]) -> bool:
    if (guard_pos[0] >= matrix_shape[0]) or (guard_pos[0] < 0):
        return False
    elif (guard_pos[1] >= matrix_shape[1]) or (guard_pos[1] < 0):
        return False
    else:
        return True
    
def get_next_movement(current_movement):
    """Turn right. Could probably be implemented better... oh well"""
    movement_sequence = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    ]
    current_index = movement_sequence.index(current_movement)
    if current_index < 3:
        return movement_sequence[current_index+1]
    else:
        return movement_sequence[0]
    


def part1():
    # Find the initial location of the guard
    matrix = get_input_char_matrix()
    current_guard_pos = get_guard_position(matrix)
    movement = (-1, 0) # start with moving up one
    next_pos = (current_guard_pos[0] + movement[0], current_guard_pos[1] + movement[1])

    while True:
        # print("Position:", current_guard_pos)
        # print("Moving:", movement)
        next_pos = (current_guard_pos[0] + movement[0], current_guard_pos[1] + movement[1])
        # Check if we've exited the map
        if not guard_is_on_map(matrix.shape, next_pos):
            visited_pos_count = np.count_nonzero(matrix == "X")
            return visited_pos_count
        
        # if the next value is a wall, change direction
        next_matrix_val = matrix[next_pos[0], next_pos[1]]
        if next_matrix_val == "#":
            movement = get_next_movement(movement)

        # Otherwise, move in the planned direction + update the matrix
        else:
            matrix[current_guard_pos[0], current_guard_pos[1]] = "X"
            current_guard_pos = next_pos
            matrix[current_guard_pos[0], current_guard_pos[1]] = "X"

    print(matrix)

def part2():
    pass

print("Part 1:", part1())
print("Part 2:", part2())
