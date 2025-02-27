import random

# Global variables
success_count = 0
failure_count = 0
total_success_steps = 0
total_failure_steps = 0
total_random_restarts = 0
total_steps_required = 0


# Validate and parse user input
def input_queens():
    while True:
        n = int(input("Enter the number of queens (minimum 4): "))
        if n >= 4:
            return n
        print("Invalid input! The number of queens must be at least 4.")


# Generate a random state with queens in different columns.
def generate_random_state(n):
    return [random.randint(0, n - 1) for _ in range(n)]


# Calculate the number of attacking pairs.
def calculate_heuristic(state):
    n = len(state)
    h = 0

    row_counts = [0] * n
    for row in state:
        row_counts[row] += 1
    for count in row_counts:
        h += count * (count - 1) // 2

    for i in range(n):
        for j in range(i + 1, n):
            if abs(i - j) == abs(state[i] - state[j]):
                h += 1
    return h


# Print the puzzle state in a nice format
def print_board(state):
    n = len(state)
    board = []

    for row in reversed(range(n)):
        line = ""
        for col in range(n):
            line += " Q " if state[col] == row else " . "
        board.append(line)

    print("\n".join(board))
    print()


# Generate all possible successor states by moving each queen in its column.
def get_successors(state):
    n = len(state)
    successors = []
    for col in range(n):
        original_row = state[col]
        for new_row in range(n):
            if new_row != original_row:
                new_state = list(state)
                new_state[col] = new_row
                successors.append(new_state)
    return successors


# Hill Climbing Search with and without sideways moves.
def basic_hill_climbing(n, max_sideways=0):
    current_state = generate_random_state(n)
    current_h = calculate_heuristic(current_state)
    steps = 1
    sideways_moves = 0
    path = [(0, current_h, current_state.copy())]

    while True:
        if current_h == 0:
            return (True, steps - 1, current_state, path)

        successors = get_successors(current_state)
        if not successors:
            return (False, steps - 1, current_state, path)

        successor_h = [(s, calculate_heuristic(s)) for s in successors]
        best_h = min(h for (s, h) in successor_h)

        if best_h > current_h:
            return (False, steps - 1, current_state, path)

        best_successors = [s for s, h in successor_h if h == best_h]
        next_state = random.choice(best_successors)
        next_h = best_h

        if next_h < current_h:
            sideways_moves = 0
        else:
            sideways_moves += 1
            if sideways_moves > max_sideways:
                return (False, steps - 1, current_state, path)

        current_state = next_state.copy()
        current_h = next_h
        path.append((steps, current_h, current_state.copy()))
        steps += 1


# Random-restart Hill Climbing Search with and without sideways moves.
def random_restart_hill_climbing(n, use_sideways=False):
    global total_random_restarts, total_steps_required
    total_steps = 0
    random_restarts = 0
    path = []

    while True:
        success, steps, state, run_path = basic_hill_climbing(
            n, 100 if use_sideways else 0)
        adjusted_path = []
        for step, h, s in run_path:
            adjusted_step = total_steps + step
            adjusted_path.append((adjusted_step, h, s))

        path.extend(adjusted_path)
        total_steps += steps

        if success:
            total_random_restarts += random_restarts
            total_steps_required += total_steps
            return (True, total_steps, state, path)

        random_restarts += 1
        current_h = calculate_heuristic(
            generate_random_state(n))  # Heuristic after randomizing
        total_steps += 1
        path.append((total_steps, f"Restarting search (Current heuristic: {current_h})", generate_random_state(n)))
        total_steps += 1


# Main function
def main():
    global success_count, failure_count, total_success_steps, total_failure_steps

    n = input_queens()
    runs = int(input("Enter the number of runs: "))

    print("\nSelect algorithm:")
    print("1. Hill Climbing")
    print("2. Hill Climbing with Sideways Moves")
    print("3. Random-Restart Hill Climbing")
    print("4. Random-Restart Hill Climbing with Sideways Moves")
    choice = int(input("Enter choice (1-4): "))

    for run in range(runs):
        print(f"\n{'=' * 40}")
        print(f"Run {run + 1}:")
        success = False
        steps = 0
        state = []
        path = []

        if choice == 1:
            success, steps, state, path = basic_hill_climbing(n, 0)
        elif choice == 2:
            success, steps, state, path = basic_hill_climbing(n, 100)
        elif choice == 3:
            success, steps, state, path = random_restart_hill_climbing(n, False)
        elif choice == 4:
            success, steps, state, path = random_restart_hill_climbing(n, True)
        else:
            print("Invalid choice")
            return

        for step, h, s in path:
            if isinstance(h, str):  # Restarting Search Message
                print(f"\nStep {step}: {h}")
            elif step == 0:         # Initial State Message
                print(f"\nRandom Initial State: Current heuristic: {h}")
            else:
                print(f"\nStep {step}: Current heuristic: {h}")
            print_board(s)

        if success:
            print("Solution found!")
            success_count += 1
            total_success_steps += steps
        else:
            print("Failed to find solution.")
            failure_count += 1
            total_failure_steps += steps

    success_rate = success_count / runs if runs > 0 else 0
    failure_rate = failure_count / runs if runs > 0 else 0
    avg_success_steps = total_success_steps / success_count if success_count > 0 else 0
    avg_failure_steps = total_failure_steps / failure_count if failure_count > 0 else 0

    if choice in [3, 4]:
        print("\nFinal Statistics:")
        print(
            f"{'Avg Restarts:':<20} {total_random_restarts / runs if runs > 0 else 0:.2f}"
        )
        print(
            f"{'Avg Steps:':<20} {total_steps_required / runs if runs > 0 else 0:.2f}"
        )
    else:
        print("\nFinal Statistics:")
        print(f"{'Success Rate:':<20} {success_rate * 100:.2f}%")
        print(f"{'Failure Rate:':<20} {failure_rate * 100:.2f}%")
        print(f"{'Avg Success Steps:':<20} {avg_success_steps:.2f}")
        print(f"{'Avg Failure Steps:':<20} {avg_failure_steps:.2f}")


if __name__ == "__main__":
    main()
