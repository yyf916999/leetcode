def min_movement_cost(containers):
    n = len(containers)
    total_products = sum(containers)
    target = total_products // n
    
    # Compute the differences (excess or deficit) from the target for each container
    diff = [container - target for container in containers]
    
    # We will accumulate the imbalance and calculate the total movement cost
    total_cost = 0
    index = 0
    cur_bal = 0
    temp_len = n
    for i in range(len(diff)):
        if diff[i] > 0:
            index = i

    temp_index = index
    while temp_len>0:
        if diff[temp_index] > 0:
            cur_bal += diff[temp_index]
        


    temp_index = index
    temp_len = n
    while temp_len> 0 :

    return total_cost

# Example usage:
containers = [3, 4, 6, 6, 6]
print(min_movement_cost(containers))  # Output should be 7
