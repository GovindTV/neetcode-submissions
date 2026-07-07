class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for f in range(len(nums)):
            if f!=0 and nums[f] == nums[f-1]:
                continue
            l,r = f+1,len(nums)-1
            tar = 0 - nums[f]
            while l < r:
                cursum = nums[l] + nums[r]
                if cursum > tar:
                    r -= 1                    
                elif cursum < tar:
                    l += 1
                else:
                    res.append([nums[f],nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res