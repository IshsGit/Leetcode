class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        longest = 1
        start = 0
        substr = s[0]

        for idx, ch in enumerate(s[1::]):

            if ch in substr:
                print("in substr")
                print("longest: ", longest)
                print("substr: ", substr)
                longest = max(longest, len(substr))
                substr = substr[substr.index(ch)+1::] + ch
                print("new substr: ", substr)
            else:
                substr += ch
                longest = max(len(substr), longest)

        print("final: ", substr)
        return longest