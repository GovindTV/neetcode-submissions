class Solution:

    def encode(self, strs: List[str]) -> str:
        key = '#'
        res = ''
        for i in strs:
            res += str(len(i)) + key + i
        print(res)
        return res        

    def decode(self, s: str) -> List[str]:
        key, res, i = '#', [], 0
        while i < len(s):
            j = i
            while s[j] != key:
                j += 1
            size = int(s[i:j])
            res.append(s[j+1:j+1+size])
            i = j + 1 + size
        return res