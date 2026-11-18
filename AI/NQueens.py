def solve_n_queens(n):

    solutions = []

    # Store the column position of each queen
    board = [-1] * n

    # Helper arrays for Branch and Bound
    columns = [False] * n

    diag1 = [False] * (2 * n - 1)

    diag2 = [False] * (2 * n - 1)

    # Backtracking Function
    def backtrack(row):

        # All queens are placed successfully
        if row == n:
            solutions.append(board.copy())
            return

        # Try placing queen in every column
        for col in range(n):

            # Check column and diagonal conditions
            if (not columns[col]
                and not diag1[row + col]
                and not diag2[row - col + n - 1]):

                # Place the queen
                board[row] = col

                columns[col] = True
                diag1[row + col] = True
                diag2[row - col + n - 1] = True

                # Move to the next row
                backtrack(row + 1)

                # Backtracking: Remove the queen
                columns[col] = False
                diag1[row + col] = False
                diag2[row - col + n - 1] = False

    backtrack(0)

    return solutions


# Main Program
if __name__ == "__main__":

    n = 8

    solutions = solve_n_queens(n)

    print(f"Total solutions for {n}-Queens: {len(solutions)}")

    # Display the first solution
    if solutions:

        first_solution = solutions[0]

        print("\nFirst Solution:")

        for row in range(n):

            line = ['.'] * n

            line[first_solution[row]] = 'Q'

            print(" ".join(line))
