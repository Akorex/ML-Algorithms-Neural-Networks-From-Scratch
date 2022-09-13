"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""

def two_sum(nums, target):
    seen = {} 

    for i, num in enumerate(nums):
        if target - num in seen:
            return ([seen[target - num], i])
        elif num not in seen:
            seen[num] = i
