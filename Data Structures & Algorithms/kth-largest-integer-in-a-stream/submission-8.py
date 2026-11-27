'''


'''


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # nums.sort()
        # self.nums = nums
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.nums = nums

    def add(self, val: int) -> int:
        # self.nums.append(val)
        # self.nums.sort()
        # return self.nums[len(self.nums) - self.k ]
        # if self.nums and val <= self.nums[0]:
        #     return self.nums[0]
        # else:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]

