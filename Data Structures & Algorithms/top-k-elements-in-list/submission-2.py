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

"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        maxHeap = []
        for n in nums:
            frequency[n] += 1
        for num, freq in frequency.items():
            heapq.heappush(maxHeap,(-1 * freq, num))
        res = []
        for _ in range(k):
            _,num = heapq.heappop(maxHeap)
            res.append(num)

        return res