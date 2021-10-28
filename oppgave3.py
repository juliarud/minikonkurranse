"""
Given an array of integers nums, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,10,8], target = 8
Output: [3,5]

Example 2:
Input: nums = [5,7,3,7,8,0,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

def searchRange(number_list, target):
    #Return list with length 2, with first and last position of the target in the list
    return 

 

test_list = [3, 4, 7, 9, 0, 8, 4, 7, 9]
test_list1 = [0,0,0,1,0]
test_list2 = []


#tester
assert searchRange(test_list, 7) == [2,7]
assert searchRange(test_list,2) == [-1,-1]
assert searchRange(test_list1, 0) == [0,4]
assert searchRange(test_list2,6) == [-1,-1]



