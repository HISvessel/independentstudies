#!/usr/bin/python3

def target_number(nums, target):
    for index, value in enumerate(nums):
        result = target - value
        if result in nums:
            result_index = [i for i, value in enumerate(nums) if value == result]
            #next_index = nums.index(result)
            return (index, result_index)


nums = [2, 7, 11, 15]
target = 26
print(target_number(nums, target))