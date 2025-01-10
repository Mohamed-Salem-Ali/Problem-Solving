from typing import List

class Solution:
    def isPrefixAndSuffix(str1: str, str2: str) -> bool:
        """
        Checks if `str1` is both a prefix and a suffix of `str2`.

        Args:
            str1 (str): The string to check as a prefix and suffix.
            str2 (str): The string to check against.

        Returns:
            bool: True if `str1` is both a prefix and suffix of `str2`, False otherwise.
        """
        l = len(str1)
        if l > len(str2):
            return False
        else:
            return str1 == str2[:l] and str1 == str2[-l:]

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        """
        Counts the number of pairs (i, j) where `words[i]` is both a prefix and suffix of `words[j]`.

        Args:
            words (List[str]): A list of strings to check for prefix-suffix relationships.

        Returns:
            int: The number of prefix-suffix pairs in the list.
        """
        counter = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if Solution.isPrefixAndSuffix(words[i], words[j]):
                    counter += 1
        return counter

# Test cases in the main function
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Basic functionality
    print(solution.countPrefixSuffixPairs(["abc", "abcabc", "cab", "abc"]))  
    # Expected: 2 (abc is a prefix and suffix of abcabc, and abc is a prefix and suffix of itself in later comparisons)

    # Test case 2: No prefix-suffix pairs
    print(solution.countPrefixSuffixPairs(["hello", "world", "python"]))  
    # Expected: 0

    # Test case 3: Single-word list
    print(solution.countPrefixSuffixPairs(["prefix"]))  
    # Expected: 0

    # Test case 4: Multiple prefix-suffix pairs
    print(solution.countPrefixSuffixPairs(["a", "aa", "aaa", "aaaa"]))  
    # Expected: 6 (a is prefix-suffix of aa, aaa, aaaa; aa is prefix-suffix of aaa, aaaa; aaa is prefix-suffix of aaaa)

    # Test case 5: Empty list
    print(solution.countPrefixSuffixPairs([]))  
    # Expected: 0

    # Test case 6: Mixed string lengths
    print(solution.countPrefixSuffixPairs(["ab", "abab", "abc", "bab", "ab"]))  
    # Expected: 2 (ab is prefix-suffix of abab, ab;)
