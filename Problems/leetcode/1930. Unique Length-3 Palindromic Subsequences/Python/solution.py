class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        Counts the number of unique palindromic subsequences of length 3 in the input string.

        A palindromic subsequence is a subsequence that reads the same forwards and backwards.
        This function specifically considers subsequences of the form "x_yx", where:
        - `x` is the same character at the start and end of the subsequence.
        - `y` is a character that appears between the two occurrences of `x`.

        Parameters:
        s (str): The input string containing lowercase English letters.

        Returns:
        int: The total number of unique palindromic subsequences of length 3 in the string.

        Example:
        --------
        Input: s = "aabca"
        Output: 3
        Explanation:
        The palindromic subsequences are "aba", "aaa", and "aca".
        """
        l = set(s)
        counter = 0
        for x in l:
            left = s.index(x)
            right = s.rindex(x)
            b = set()
            if left != right:
                b = set(s[left + 1:right])
            counter += len(b)
        return counter


if __name__ == "__main__":
    # Instantiate the solution class
    solution = Solution()

    # Test cases
    print("Test 1:", solution.countPalindromicSubsequence("a"))  # Expected: 0
    print("Test 2:", solution.countPalindromicSubsequence("abc"))  # Expected: 0
    print("Test 3:", solution.countPalindromicSubsequence("aabca"))  # Expected: 3
    print("Test 4:", solution.countPalindromicSubsequence("bbcbaba"))  # Expected: 4
    print("Test 5:", solution.countPalindromicSubsequence("aaaaa"))  # Expected: 1
    print("Test 6:", solution.countPalindromicSubsequence("ababab"))  # Expected: 4
    print("Test 7:", solution.countPalindromicSubsequence("abcd"))  # Expected: 0
    print("Test 8:", solution.countPalindromicSubsequence("aa" * 500))  # Expected: 1