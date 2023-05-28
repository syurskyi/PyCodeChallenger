from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = ""
        for i, char in enumerate(strs[0]):
            if any(word[i] != char for word in strs[1:]):
                break
            prefix += char

        return prefix


class TestLongestCommonPrefix:
    @staticmethod
    def run_tests():
        test_cases = [
            (["flower", "flow", "flight"], "fl"),
            (["dog", "racecar", "car"], ""),
        ]

        solution = Solution()

        for strs, expected in test_cases:
            result = solution.longestCommonPrefix(strs)
            assert result == expected, f"Expected: {expected}, Got: {result}"
            print(f"Input: strs={strs}")
            print("Result:", result)
            print("Expected output:", expected)
            print("Test passed:", result == expected)
            print()

        print("All test cases passed!")


if __name__ == "__main__":
    TestLongestCommonPrefix.run_tests()
