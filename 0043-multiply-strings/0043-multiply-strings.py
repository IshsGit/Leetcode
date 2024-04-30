class Solution:
    def multiply(self, num1: str, num2: str) -> str:
       
        def multiply_single_digit(digit1, digit2, carry=0):
            product = int(digit1) * int(digit2) + carry
            return str(product % 10), product // 10
        

        def add_strings(num1, num2):
            result = []
            carry = 0
            i, j = len(num1) - 1, len(num2) - 1
            while i >= 0 or j >= 0 or carry:
                digit_sum = (int(num1[i]) if i >= 0 else 0) + (int(num2[j]) if j >= 0 else 0) + carry
                result.append(str(digit_sum % 10))
                carry = digit_sum // 10
                i -= 1
                j -= 1
            return ''.join(result[::-1])
        
        if num1 == "0" or num2 == "0":
            return "0"
        
        result = "0"
        n = len(num1)
        m = len(num2)
        
        for i in range(n - 1, -1, -1):
            carry = 0
            current_result = ['0'] * (n - 1 - i)
            
            for j in range(m - 1, -1, -1):
                product, carry = multiply_single_digit(num1[i], num2[j], carry)
                current_result.append(product)
                
            if carry > 0:
                current_result.append(str(carry))
                
            result = add_strings(result, ''.join(current_result[::-1]))
            
        return result
