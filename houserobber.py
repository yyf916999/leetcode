def rob(nums: list[int]) -> int:
    dp = [0] * len(nums)
    dp[0] = nums[0]
    n = len(nums)
    if n == 1:
        return nums[0]
    if n >= 2:
        dp[1] = max(nums[0] + nums[1], nums[1])
    for i in range(2, n):
        dp[i] = max(nums[i] + dp[i-2], nums[i] + dp[i-1])
    print(dp)
    return max(dp[-1], dp[-2])


res = rob([9, -1, -3, 4, 5, -3, 4, 2, 1, -2])

print(res)
