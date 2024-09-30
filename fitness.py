'''
A user is using the Amazon fitness tracker, and they are engaged in a jumping exercise routine. The user is positioned on the ground, and there are n stones, each placed at different heights. The height of the ith stone is represented by height[i] meters.
The goal is to maximize the calorie burn during this exercise, and the calories burned when jumping from the ith stone to the jth stone is calculated as (height[i] - height[j])^2.

The user intends to practice jumping on each stone exactly once but can choose the order in which they jump. Since the user is looking to optimize their calorie burn for this single session, the task is to determine the maximum amount of calories that can be burned during the exercise.
Formally, given an array height of size n, representing the height of each stone, find the maximum amount of calories the user can burn.

'''

def solution(arr):
    arr = sorted(arr, reverse=True)
    left = 0
    right = len(arr)-1
    optimal_sequence = []
    res = 0
    while left <= right:
        if left == right:
            optimal_sequence.append(arr[left])
        else:
            optimal_sequence.append(arr[left])
            optimal_sequence.append(arr[right])
        left +=1
        right -=1
    print(optimal_sequence)
    for i in range(1,len(optimal_sequence)):
        res += (optimal_sequence[i]-optimal_sequence[i-1])**2
    res += optimal_sequence[0]**2
    return res 

res =solution([2,2,4,3])
print(res)