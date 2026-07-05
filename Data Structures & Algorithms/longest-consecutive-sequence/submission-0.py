class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_cnt = 0
        for i in nums:
            cnt = 1
            j = i+0
            while True:
                if j + 1 in nums:
                    cnt += 1
                    j += 1
                else:
                    break
            max_cnt = max(cnt, max_cnt)
        return max_cnt