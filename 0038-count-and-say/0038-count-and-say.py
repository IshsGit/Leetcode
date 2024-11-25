class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        if n == 1:
            return "1"
        
        # Recursive call to get the previous sequence
        prev_sequence = self.countAndSay(n - 1)
        
        # Initialize variables
        count = 1
        result = ""
        
        # Iterate through the previous sequence
        for i in range(len(prev_sequence)):
            # If the current character is the same as the next one
            if i + 1 < len(prev_sequence) and prev_sequence[i] == prev_sequence[i + 1]:
                count += 1
            else:
                # Append the count and the character to the result
                result += str(count) + prev_sequence[i]
                # Reset count for the next character
                count = 1
        
        return result