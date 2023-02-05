def linear_search(values, target):
    for i in range(len(values)+1):
        if values[i] == target:
            return i
    return -1

# Example usage
values = [1, 2, 3, 4, 5]
target = 3
index = linear_search(values, target)
if index != -1:
    print("Target found at index:", index)
else:
    print("Target not found in list.")

def binary_search(values, target):
    low = 0
    high = len(values) - 1
    while low <= high:
        mid = (low + high) // 2
        if values[mid] == target:
            return mid
        elif values[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5

# Perform the search
index = binary_search(values, target)

# Check if the target was found
if index != -1:
    print("Target found at index:", index)
else:
    print("Target not found in list.")

# Additional test values
target2 = 8
index2 = binary_search(values, target2)

# Check if the target was found
if index2 != -1:
    print("Target found at index:", index2)
else:
    print("Target not found in list.")

def BFS(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

# Test graph represented as a dictionary
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

# Perform BFS starting from vertex 'A'
visited = BFS(graph, 'A')

# Print the visited vertices
print(visited)




