class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for i in s.lower():
            if ord('0') <= ord(i) <= ord('9'):
                res.append(i)

            elif ord('a') <= ord(i) <= ord('z'):
                res.append(i)
            
        for i in range(len(res)//2):
            if res[i] != res[len(res)-1-i]:
                return False
        return True