class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        char_map = {}
        maxf = 0
        res = 0

        for j in range(len(s)):
            char_map[s[j]] = char_map.get(s[j], 0) + 1
            maxf = max(maxf, char_map[s[j]])

            if (j - i + 1) - maxf > k:
                char_map[s[i]] -= 1
                i += 1 
                
            
            res = max(res, j - i + 1)
        
        return res
        
        

        