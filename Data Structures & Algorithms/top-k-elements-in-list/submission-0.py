class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapper = defaultdict(int)

        for num in nums:
            mapper[num] += 1
        
        valid = sorted(mapper.values())[k-1]

        output = []

        for k,v in mapper.items():
            if v >= valid:
                output.append(k)
        
        return output