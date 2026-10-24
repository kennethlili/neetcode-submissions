"""
You are given an array of positive integers nums.
nums arr length is small
num are smalls
nums are postive

Return true if you can partition the array into two subsets, subset1 and subset2 where sum(subset1) == sum(subset2). Otherwise, return false.
-counting
-conbination
combination?
-no duplciate
1,4 2,3
- I need to pick a subset that sum up to sum/2 -> target
- stop: when the cumulateive sum is >= target

summary: find the same subset of arr that is the same of sum amt

Input: nums = nums
Decision: find the sum of taken subset to equal to sum(nums)/2 -> target

Starting with first element what can i do?
take i
- curr sum is gonna be nums[i], need to look for target-nums[i] = 4
skip i
-curr sum is gonna be 0, need to look for target
- i need to be move the next element -> i+1

take i,  need to look for target-nums[i] = 4, take i+1 or skip i+1
skip i, need to look for target, take i+1 or skip i+1

recurative
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        if sm % 2 != 0:
            return False
        target = sm / 2
        memo = {}

        def numWays_startwith_toMatch_target(i, currSum):
            if i >= len(nums):
                return False
            if currSum == target:
                return True
            if currSum > target:
                return False
            if (i, currSum) in memo:
                return memo[(i, currSum)]
            take = numWays_startwith_toMatch_target(i + 1, currSum + nums[i])
            skip = numWays_startwith_toMatch_target(i + 1, currSum)
            memo[(i, currSum)] = take or skip
            return memo[(i, currSum)]

        return numWays_startwith_toMatch_target(0, 0)
