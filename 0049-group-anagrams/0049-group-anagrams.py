class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for word in strs:
            # Sort the characters of the word
            sorted_word = ''.join(sorted(word))
            
            # Add the word to the corresponding list in the dictionary
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        
        # Convert the values of the dictionary to a list of lists
        return list(anagrams.values())