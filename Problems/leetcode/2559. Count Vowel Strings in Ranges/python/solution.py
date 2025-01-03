from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        """
        Calculates the number of words that start and end with vowels within the given ranges.

        Args:
        words (List[str]): A list of strings to evaluate.
        queries (List[List[int]]): A list of query ranges [start, end] to count vowel strings.

        Returns:
        List[int]: A list of integers representing the counts of vowel strings for each query.
        """
        # Number of words in the input list
        n = len(words)
        
        # Prefix sum array to store the cumulative count of vowel strings
        Prefix = [0] * (n + 1)
        
        # Set of vowel characters
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # Populate the prefix sum array
        for i in range(n):
            # Carry forward the cumulative count
            Prefix[i + 1] = Prefix[i]
            # Check if the word starts and ends with vowels
            if words[i][0].lower() in vowels and words[i][-1].lower() in vowels:
                Prefix[i + 1] += 1

        # Initialize the result list to store counts for each query
        ANS = []
        for query in queries:
            # Calculate the count of vowel strings in the given range
            start, end = query
            ANS.append(Prefix[end + 1] - Prefix[start])

        return ANS

# Test Cases
if __name__ == "__main__":
    # Sample test cases
    solution = Solution()

    # Test case 1
    words = ["apple", "banana", "orange", "umbrella"]
    queries = [[0, 1], [0, 3], [2, 3]]
    print(f"Input: words={words}, queries={queries} -> Output: {solution.vowelStrings(words, queries)}")

    # Test case 2
    words = ["a", "b", "c", "u"]
    queries = [[0, 3], [1, 2]]
    print(f"Input: words={words}, queries={queries} -> Output: {solution.vowelStrings(words, queries)}")

    # Test case 3
    words = ["eat", "idle", "egg", "ice"]
    queries = [[0, 3], [1, 2], [2, 3]]
    print(f"Input: words={words}, queries={queries} -> Output: {solution.vowelStrings(words, queries)}")

    # Test case 4
    words = ["rock", "roll", "hill", "bill"]
    queries = [[0, 3], [0, 1], [2, 3]]
    print(f"Input: words={words}, queries={queries} -> Output: {solution.vowelStrings(words, queries)}")

    # Test case 5
    words = ["up", "out", "end", "echo"]
    queries = [[0, 2], [1, 3], [0, 3]]
    print(f"Input: words={words}, queries={queries} -> Output: {solution.vowelStrings(words, queries)}")

    # Test Case 1
    #[1, 3, 2]

    # Test Case 2
    #[2, 0]

    # Test Case 3
    #[2, 1, 1]

    # Test Case 4
    #[0, 0, 0]

    # Test Case 5
    #[0, 1, 1]
