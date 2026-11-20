"""
temperatures, temperatures[i] represents the daily temperatures on the ith day
Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.
    - warmer -> higher temp -> temp_a < temp_b
    - ith means the index after that day
    - no day warmer , return 0
time: O(n^2)
space: O(1)
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # for i, temp in enumerate(temperatures):
        #     numOfDay = 0
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j]>temp:
        #             numOfDay = j - i
        #             break
        #     # res.append(numOfDay)
        #     temperatures[i] = numOfDay
        # return temperatures
        stack = []
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp,i))
            else:
                while stack and stack[-1][0] < temp:
                    (_, idx) = stack.pop()
                    temperatures[idx] = i - idx
                stack.append((temp,i))
            
        for _,idx in stack:
            temperatures[idx] = 0
        return temperatures



