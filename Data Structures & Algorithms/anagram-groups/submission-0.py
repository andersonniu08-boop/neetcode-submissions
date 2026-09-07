class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        amap = {}
        for i in strs:
            key = "".join(sorted(i))
            if key not in amap:
                amap[key] = []
            amap[key].append(i)
        
        return list(amap.values())