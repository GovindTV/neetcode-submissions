class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        out, l = set(), 0
        res = 0
        for r, rval in enumerate(s):
            while rval in out:
                out.remove(s[l])
                l += 1
            out.add(rval)
            res = max(res, len(out))
        return res