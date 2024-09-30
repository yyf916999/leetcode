def min_movement_cost(containers):
    n = len(containers)
    total_products = sum(containers)
    target = total_products // n
    
    # Compute the differences (excess or deficit) from the target for each container
    diff = [container - target for container in containers]
    
    # We will accumulate the imbalance and calculate the total movement cost
    total_cost = 100000000000
    temp_1 = 0
    imbalance = 0
    
    for i from (n):
    
    imbalance = 0
    temp_2 = 0
    # Traverse the containers, accumulate the imbalance, and calculate the cost
    for i in range(n-1,-1,-1):
        imbalance += diff[i]
        temp_2
    
    return total_cost

# Example usage:
containers = [3, 4, 6, 6, 6]
print(min_movement_cost(containers))  # Output should be 7
