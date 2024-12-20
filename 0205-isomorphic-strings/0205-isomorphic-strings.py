class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_map = {}
        mapped_chars = set()
        
        for i in range(len(s)):
            if s[i] not in char_map:
                if t[i] in mapped_chars:
                    return False
                char_map[s[i]] = t[i]
                mapped_chars.add(t[i])
            else:
                if char_map[s[i]] != t[i]:
                    return False
                
        return True
