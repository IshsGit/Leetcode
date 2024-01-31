class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Define a mapping of digits to letters
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        # Base case: if the input digits are empty, return an empty list
        if not digits:
            return []
        
        # Initialize a list to store the combinations
        combinations = []
        
        # Define a recursive helper function to generate combinations
        def generate_combinations(current, remaining_digits):
            # Base case: if there are no remaining digits, add the current combination
            if not remaining_digits:
                combinations.append(current)
                return
            
            # Get the letters corresponding to the first digit
            letters = digit_map[remaining_digits[0]]
            
            # Iterate through each letter and make a recursive call
            for letter in letters:
                generate_combinations(current + letter, remaining_digits[1:])
        
        # Start the recursive process with an empty current string and all digits
        generate_combinations('', digits)
        
        return combinations

# Example usage:
solution = Solution()
result = solution.letterCombinations('23')
print(result)