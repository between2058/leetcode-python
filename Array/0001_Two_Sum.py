'''
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):    #O(n)
            complement = target - num   
            
            if complement not in map:     #O(1)
                map[num] = i              #O(1)
            else:
                return [map[complement], i] #O(1)
        return []
    
        '''
        Time complexity: O(n)
        O(n) = O(n) * O(1)  --> outer loop * inner loop
        Note that dictionary in python is a hash table, so "in" operator is O(1), and getting value by key is also O(1)

        Space complexity: O(n)
        Hash table is used to store the value and index of the element in the list, so space complexity is O(n)
        '''
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            complement = target - i
            if complement in nums:
                return [nums.index(i), nums.index(complement)]
            
        '''
        time complexity: O(n^2)
        Outer loop -> O(n)
        Inner loop -> O(n) = O(n) + O(n)
        Note that "in" operator is O(n) in list, ".index()" is O(n)
        Total time complexity: O(n^2) = O(n) * O(n) (inner loop * outer loop)

        space complexity: O(1)
        No extra data structure is used so space complexity is O(1)
        '''    
        
