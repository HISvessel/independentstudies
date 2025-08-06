#!/usr/bin/python3

def target_number(nums, target):
    for index, value in enumerate(nums):
        result = target - value
        if result in nums:
            next_index = nums.index(result)
            return (index, next_index)


nums = [2, 7, 11, 15]
target = 9
print(target_number(nums, target))