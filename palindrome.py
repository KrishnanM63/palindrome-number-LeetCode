class Solution:
    def isPalindrome(self, x: int) -> bool:
        v=str(x)
        return v==v[::-1]
     
