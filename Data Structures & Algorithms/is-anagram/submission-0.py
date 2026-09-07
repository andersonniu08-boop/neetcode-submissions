class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False;
        ana = {} 
        for char in s:
            ana[char] = ana.get(char, 0) + 1
        for char in t:
            if char not in ana or ana[char] == 0:
                return False
            ana[char] -= 1
        return True
        
        