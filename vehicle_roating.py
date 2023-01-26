from typing import List, Tuple


def vrp_solver(num_vehicles: int, vehicle_capacity: int, customer_list: List[Tuple[float, float, int]]) -> List[
    List[int]]:
    # Initialize the routes for each vehicle
    routes = [[] for _ in range(num_vehicles)]

    # Sort the customers by their demand
    customer_list = sorted(customer_list, key=lambda x: x[2])

    # Initialize the current vehicle and its load
    current_vehicle = 0
    current_load = 0

    # Iterate through the customers
    for i, customer in enumerate(customer_list):
        location, demand = customer[:2], customer[2]
        # If adding the customer to the current route would exceed the vehicle's capacity, move to the next vehicle
        if current_load + demand > vehicle_capacity:
            current_vehicle += 1
            current_load = 0
            if current_vehicle == num_vehicles:
                current_vehicle = 0
        # Add the customer to the current route
        routes[current_vehicle].append(i)
        current_load += demand
    return routes


# Example usage
num_vehicles = 2
vehicle_capacity = 10
customer_list = [(1, 2, 3), (3, 4, 5), (2, 3, 4), (1, 1, 2), (5, 6, 8)]
routes = vrp_solver(num_vehicles, vehicle_capacity, customer_list)
print(routes)
