class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return not stack


class TestValidParentheses:
    @staticmethod
    def run_tests():
        test_cases = [
            ("()", True),
            ("()[]{}", True),
            ("(]", False),
        ]

        solution = Solution()

        for s, expected in test_cases:
            result = solution.isValid(s)
            assert result == expected, f"Expected: {expected}, Got: {result}"
            print(f"Input: s='{s}'")
            print("Result:", result)
            print("Expected output:", expected)
            print("Test passed:", result == expected)
            print()

        print("All test cases passed!")


if __name__ == "__main__":
    TestValidParentheses.run_tests()