"""
substring -> continuious
palindrome:
    a single char is a palindrome
    palindrome can be start from odd or even case

"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def helper(start, curr):
            if start == len(s):
                res.append(curr[:])
                return
            for end in range(start, len(s)):
                if self.isPal(start, end, s):
                    curr.append(s[start: end + 1])
                    helper(end + 1, curr)
                    curr.pop()
            

        helper( 0,[])
        return res

    def isPal(self, start, end , s):
        l = start
        r = end
        while( l<= r):
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        
