from itertools import combinations


def multiple_choice(num_items, num_dims, weights, values, capacity):
    # initialize the best value and best combination
    best_value = 0
    best_combination = []

    # loop through all possible combinations of items
    for i in range(1, num_items + 1):
        for combination in combinations(range(num_items), i):
            # check if the combination is valid (fits within the capacity)
            valid = True
            for dim in range(num_dims):
                dim_weight = sum([weights[item][dim] for item in combination])
                if dim_weight > capacity[dim]:
                    valid = False
                    break
            if valid:
                # calculate the value of the combination
                combination_value = sum([values[item] for item in combination])
                # update the best value and combination if necessary
                if combination_value > best_value:
                    best_value = combination_value
                    best_combination = combination

    # return the best combination and its value
    return best_combination, best_value


# example usage
num_items = 5
num_dims = 3
weights = [[3, 2, 1], [2, 5, 2], [4, 1, 3], [1, 2, 2], [2, 3, 4]]
values = [5, 8, 6, 3, 7]
capacity = [8, 10, 6]
best_combination, best_value = multiple_choice(num_items, num_dims, weights, values, capacity)
print("Best combination:", best_combination)
print("Best value:", best_value)

def multidimensional_knapsack(n, m, weights, values, capacity):
    # Initialize the knapsack array
    knapsack = [[0 for j in range(capacity[i] + 1)] for i in range(n)]

    # Fill the knapsack array
    for i in range(n):
        for j in range(1, m[i] + 1):
            for k in range(capacity[i] + 1):
                if weights[i][j - 1] > k:
                    knapsack[i][k] = knapsack[i][k]
                else:
                    knapsack[i][k] = max(knapsack[i][k], knapsack[i][k - weights[i][j - 1]] + values[i][j - 1])

    # Return the maximum value of the knapsack
    return knapsack[n - 1][capacity[n - 1]]

# Number of classes
n = 3

# Number of items in each class
m = [4, 3, 2]

# Weights of items
weights = [[2, 4, 6, 8], [1, 2, 3], [5, 8]]

# Values of items
values = [[10, 20, 30, 40], [5, 10, 15], [20, 30]]

# Capacity of each knapsack
capacity = [10, 5, 15]

# Call the function and print the result
print("The maximum cost of the items placed in knapsacks: ", end='')
print(multidimensional_knapsack(n, m, weights, values, capacity))

def demand_constraints(items, knapsacks, costs, sizes, capacities, demands):
    n = len(items)
    m = len(knapsacks)
    # Create the 2D array dp with all elements initialized to -1
    dp = [[-1 for _ in range(m)] for _ in range(n+1)]
    # Initialize the base case for the first row
    for j in range(m):
        if sizes[0][j] >= demands[j]:
            dp[0][j] = costs[0][j]

    # Iterate through the remaining rows of the dp array
    for i in range(1, n):
        for j in range(m):
            # If the size of the item is greater than the capacity of the knapsack, skip
            if sizes[i][j] > capacities[j]:
                continue
            # Initialize the max cost to be the cost of the item in the current knapsack
            max_cost = costs[i][j]
            # Iterate through the remaining knapsacks
            for k in range(m):
                # If the demand of the knapsack is less than the size of the item
                if demands[k] <= sizes[i][k]:
                    # Update the max cost by adding the cost of the item in the current knapsack
                    # and the cost of the items in the previous knapsack
                    max_cost = max(max_cost, costs[i][j] + dp[i-1][k])
            dp[i][j] = max_cost

    # Return the maximum cost from the last row
    return max([dp[n-1][j] for j in range(m)])


items = ["item1", "item2", "item3", "item4"]
knapsacks = ["knapsack1", "knapsack2", "knapsack3"]
costs = [[2, 3, 4], [4, 6, 5], [3, 5, 6], [2, 4, 2]]
sizes = [[3, 2, 1], [4, 3, 2], [2, 4, 3], [1, 2, 4]]
capacities = [6, 8, 10]
demands = [2, 3, 4]

result = demand_constraints(items, knapsacks, costs, sizes, capacities, demands)
print("The maximum cost of the items placed in knapsacks:", result)