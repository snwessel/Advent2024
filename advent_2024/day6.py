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
    
class GuardState:

    def __init__(self):
        self.matrix = get_input_char_matrix()
        self.guard_pos = get_guard_position(self.matrix)
        self.movement = (-1, 0) # start with moving up one
        self.matrix[self.guard_pos[0], self.guard_pos[1]] = "X"
        # TODO: keep track of walls that have been hit?

    def step(self):
        """
        Returns True if the guard successfully moves. 
        Returns False if the guard is off the map.
        """
        next_pos = (self.guard_pos[0] + self.movement[0], self.guard_pos[1] + self.movement[1])
        # Check if we've exited the map
        if not guard_is_on_map(self.matrix.shape, next_pos):
            return False

        # if the next value is a wall, change direction
        next_matrix_val = self.matrix[next_pos[0], next_pos[1]]
        if next_matrix_val == "#":
            self.movement = get_next_movement(self.movement)
        # Otherwise, move in the planned direction + update the matrix
        else:
            self.guard_pos = next_pos
            self.matrix[self.guard_pos[0], self.guard_pos[1]] = "X"

        return True


def part1():
    guard_state = GuardState()

    # Run the process until the guard exits the map
    while guard_state.step():
        pass

    # Count total tiles visited
    visited_pos_count = np.count_nonzero(guard_state.matrix == "X")
    return visited_pos_count

def part2():
    # BRUTE FORCE!! - This isn't a great solution, and does take a few minutes to run.
    total = 0
    # Get all positions which are valid locations for new walls
    guard_state = GuardState()
    valid_positions = np.argwhere(guard_state.matrix == ".") 

    for new_wall_pos in valid_positions:
        # Set up the guard state with the new wall
        temp_guard_state = GuardState()
        temp_guard_state.matrix[new_wall_pos[0]][new_wall_pos[1]] = "#"
        # Rule of thumb: if it takes more than 10,000 steps, then it's stuck in a circle
        step_count = 0
        while temp_guard_state.step() and step_count < 10000:
            step_count += 1
        print(f"Finished in {step_count} steps")
        if step_count >= 10000:
            total += 1

    return total

print("Part 1:", part1())
print("Part 2:", part2())
