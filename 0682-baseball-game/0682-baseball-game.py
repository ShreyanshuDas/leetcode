class Solution:
    def calPoints(self, ops):
        stack = []
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(2 * stack[-1])
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)

# Example usage:
# sol = Solution()
# ops = ["5","2","C","D","+"]
# print(sol.calPoints(ops))  # Output: 30