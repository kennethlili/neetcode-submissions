"""
facts:
    nums, arr of integer and a k -> slidig window size
    return a list that contains the max element within the k window
    at each step we slide one position to rhe right
    until the len(nums) - k
    7, until index4 = len - k
    time: o(n)
    space: O(n)
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        left = 0
        q = deque()
        for r, num in enumerate(nums):
            if not q:
                q.append((num, r))
            else:
                while q and q[-1][0] < num:
                    q.pop()
                q.append((num, r))

            if r - left + 1 > k:
                if q[0][1] == left:
                    q.popleft()
                left += 1
            if r - left + 1 == k:
                res.append(q[0][0])
        return res
