class Solution:
    def reverse(self, x: int) -> int:
        # Convert integer to string
        str_x = str(x)
        
        # Check if the number is negative
        if str_x[0] == '-':
            reversed_str = '-' + str_x[:0:-1]  # Reverse the string excluding the negative sign
        else:
            reversed_str = str_x[::-1]  # Reverse the string
        
        # Convert the reversed string back to an integer
        reversed_int = int(reversed_str)
        
        # Check for integer overflow
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
        
        return reversed_int
