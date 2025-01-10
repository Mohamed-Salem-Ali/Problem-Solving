from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        """
        Finds all strings in the list `words` that are substrings of other strings in the list.

        Args:
            words (List[str]): A list of strings to check for substrings.

        Returns:
            List[str]: A list of strings from `words` that are substrings of other strings in the list.
        """
        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] in words[j] and i != j:
                    if words[i] not in ans:
                        ans.append(words[i])
        return ans

# Test cases in the main function
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Basic functionality
    print(solution.stringMatching(["mass", "as", "hero", "superhero"]))  # Expected: ["as", "hero"]
    
    # Test case 2: Words as complete substrings of others
    print(solution.stringMatching(["leetcode", "et", "code"]))  # Expected: ["et", "code"]
    
    # Test case 3: No substrings
    print(solution.stringMatching(["apple", "banana", "cherry"]))  # Expected: []
    
    # Test case 4: All words are substrings
    print(solution.stringMatching(["a", "ab", "abc", "abcd"]))  # Expected: ["a", "ab", "abc"]
    
    # Test case 5: Duplicates in input
    print(solution.stringMatching(["a", "a", "abc", "abc"]))  # Expected: ["a","abc"]
    
    # Test case 6: Single word in list
    print(solution.stringMatching(["word"]))  # Expected: []
    
    # Test case 7: Empty list
    print(solution.stringMatching([]))  # Expected: []
