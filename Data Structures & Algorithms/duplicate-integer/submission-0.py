class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my = set()
        for i in nums:
            if i in my:
                return True
            else:
                my.add(i)
        return False
    