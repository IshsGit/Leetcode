class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s='', left=0, right=0):
            # Base case: if the length is 2 * n, add the result
            if len(s) == 2 * n:
                result.append(s)
                return
            # Recursive cases: add a left parenthesis or a right parenthesis
            if left < n:
                backtrack(s+'(', left+1, right)
            if right < left:
                backtrack(s+')', left, right+1)

        result = []
        backtrack()
        return result


