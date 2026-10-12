class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold = threshold * k
        curr = 0
        l = 0
        res = 0
        for r in range(len(arr)):

            curr += arr[r]
            if r - l  > k-1:
                curr -= arr[l]
                l += 1
            if (r-l) == k -1 and curr >= threshold:
                res += 1
        return res

