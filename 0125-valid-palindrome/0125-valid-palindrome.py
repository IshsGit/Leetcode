class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert the string to lowercase and remove non-alphanumeric characters
        cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
        
        # Check if the cleaned string is equal to its reverse
        return cleaned_s == cleaned_s[::-1]