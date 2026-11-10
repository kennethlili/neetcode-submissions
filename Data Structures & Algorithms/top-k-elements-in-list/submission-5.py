"""
facts:
    arr of num as nums, integer k
        arr of nums is not sorted
        1 <= nums.length <= 10^4
            nums is not empty
        -1000 <= nums[i] <= 1000
            can be negative
        always having the ans
    return k most frequent elements in arr nums
        in any order
    the test case is always unique, so we must have k most frequent elements

maxheap = [(frequency, nums)]
how do we count the frequency of the nums?
    cnt = {}
how do we get the k most frequent nums in cnt?
    loop again the cnt
[1,2,2,3,3]
O(nlogn)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        maxHeap = []
        for n in nums:
            frequency[n] += 1
        # nlogn, given a frequency map, how to sort it by freq/how do we find the most freq with order
        # []
        # most freq to left/ right -> right /left
        # freq as index
        # arr = [0]
        res = [[] ] * len(nums)
        
        for num, freq in frequency.items():
            # heapq.heappush(maxHeap,(-1 * freq, num))
            copy = res[freq -1].copy()
            copy.append(num)
            res[freq - 1] = copy

        ans = []
        for i in range(len(res) -1, -1, -1):
            if res[i]:
                ans = ans + res[i]
            if len(ans) == k:
                return ans
