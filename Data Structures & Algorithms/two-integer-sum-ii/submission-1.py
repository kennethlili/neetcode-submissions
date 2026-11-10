"""
facts:
return the indices pairs of two number in the arr that they add up to the target
    - we cannot reuse the same elements
    - exactly one valid solution
    - 1th index
arr are sorted in ascending order
    - only contain integer
    - 2 <= numbers.length <= 30000
restriction:
    use O(1) additional space


Brute Force:
    for i,n in numbers:
        replace with binary search
        for j (i+1, len(numbers)):
            if target - number[i] == number[j]:
                return [i,j]
    
time: O(nlogn)
space: O(1)

"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while(l < r):
            currSum = numbers[l] + numbers[r]
            if currSum == target:
                return [l+ 1, r+1]
            elif currSum > target:
                r -= 1
            else:
                l+= 1