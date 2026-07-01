class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            sort_i = "".join(sorted(i))
            if sort_i in d:
                d[sort_i].append(i)
            else:
                d[sort_i] = [i]
        
        output = []
        for k,v in d.items():
            output.append(v)
        
        return output