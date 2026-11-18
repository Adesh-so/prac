
import heapq


# Node Class
class Node:

    def __init__(self, position, g, h):
        self.position = position
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = None

    # Compare nodes based on f value
    def __lt__(self, other):
        return self.f < other.f


# Heuristic Function (Manhattan Distance)
def heuristic(a, b):

    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Get Valid Neighbors
def get_neighbors(position, grid):

    x, y = position

    neighbors = []

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dx, dy in directions:

        nx = x + dx
        ny = y + dy

        if (0 <= nx < len(grid)
            and 0 <= ny < len(grid[0])
            and grid[nx][ny] == 0):

            neighbors.append((nx, ny))

    return neighbors


# A* Search Algorithm
def astar(start, goal, grid):

    open_list = []

    closed_list = set()

    # Create starting node
    start_node = Node(start, 0, heuristic(start, goal))

    heapq.heappush(open_list, start_node)

    while open_list:

        current_node = heapq.heappop(open_list)

        # Check whether goal is reached
        if current_node.position == goal:

            path = []

            while current_node:

                path.append(current_node.position)

                current_node = current_node.parent

            return path[::-1]

        closed_list.add(current_node.position)

        # Explore neighboring positions
        for neighbor in get_neighbors(current_node.position, grid):

            if neighbor in closed_list:
                continue

            g_cost = current_node.g + 1

            h_cost = heuristic(neighbor, goal)

            neighbor_node = Node(neighbor, g_cost, h_cost)

            neighbor_node.parent = current_node

            # Check whether a better path already exists
            existing_node = next(
                (node for node in open_list
                 if node.position == neighbor),
                None
            )

            if existing_node is not None:

                if existing_node.g <= g_cost:
                    continue

                open_list.remove(existing_node)
                heapq.heapify(open_list)

            heapq.heappush(open_list, neighbor_node)

    return None


# Main Function
def main():

    rows = int(input("Enter number of rows: "))

    cols = int(input("Enter number of columns: "))

    print("Enter the grid (0 for empty, 1 for obstacle):")

    grid = []

    for i in range(rows):

        row = list(map(int, input().split()))

        grid.append(row)

    # Get starting position
    start_x, start_y = map(
        int,
        input("Enter start position (x y): ").split()
    )

    # Get goal position
    goal_x, goal_y = map(
        int,
        input("Enter goal position (x y): ").split()
    )

    start = (start_x, start_y)

    goal = (goal_x, goal_y)

    # Execute A* Algorithm
    path = astar(start, goal, grid)

    if path:

        print("Path found:", path)

    else:

        print("No path found.")


# Program Execution
if __name__ == "__main__":
    main()
