class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        j = 0
        char_map = {}
        freq_map = {}
        for j in range(len(s1)):
            # Instead of appending indices:
            freq_map[s1[j]] = freq_map.get(s1[j], 0) + 1
            char_map[s2[j]] = char_map.get(s2[j], 0) + 1
        if char_map == freq_map:
            return True


 
        for j in range(len(s1), len(s2)):
            if char_map == freq_map:
                return True
                       
            char_map[s2[j]] = char_map.get(s2[j], 0) + 1

            i = s2[j - len(s1)]

            char_map[i] -= 1

            if char_map[i] == 0:
                del char_map[i]
            
            if char_map == freq_map:
                return True
                
    
        return False
        
        