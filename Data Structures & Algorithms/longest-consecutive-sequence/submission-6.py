'''

nums large
n large, contains negative -> no index for arr

actions:

[2,20,4,10,3,4,5]
[2,3,4,4,5,10,20]

sort the arr

i, j pter
i - look for curr index
j - look for the next val

scenatrio
1. j = i + 1
    - move the i to j
    - move the j +1
    - add to the res

2. i == j
    move j until not eq
    redo 1 again

3. else:
    move i to j
    move the j +1
    reset the res


'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 0:
            return 0
        # def helper(i,j,curr):
        #     # print(curr, i)
        #     # if j >= len(nums):
        #     #     return
        #     if nums[i] == nums[j]:
        #         helper(i, j +1, curr)
        #     elif nums[j] == nums[i] + 1:
        #         temp = curr+1
        #         res[0] = max(res[0], temp)
        #         helper(j, j +1, temp)
        #     else:
        #         helper(j, j +1, 1)
        
        # helper(0, 1, 1)
        i = 0
        j = 1
        res, steak = 1, 1
        while( j < len(nums)):
            if nums[i] == nums[j]:
                j+=1
                continue
            if nums[j] == nums[i] + 1:
                steak += 1
                res = max(res, steak)
                i = j
            else:
                i = j
                steak = 1
            j += 1

        return res
