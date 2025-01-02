# Solution
def maxScore(s):
    """
    Calculate the maximum score of a string by splitting it into two non-empty parts.

    The score is calculated as:
    - The number of '0's in the left part (s[:i]).
    - The number of '1's in the right part (s[i:]).

    Args:
    s (str): A binary string containing only '0' and '1'.

    Returns:
    int: The maximum possible score achieved by splitting the string.
    """
    maximum_score = 0 # Initialize the maximum score to 0

    # Iterate through all possible split points (excluding the first and last characters)
    for i in range(1,len(s)):
        # Calculate the score for the current split
        score = s[i:].count('1') + s[:i].count('0')
        
        if score > maximum_score:
            maximum_score = score
    return maximum_score

# Test Cases
if __name__ == "__main__":
    # Sample test cases
    s = "0011" 
    target = 4
    print(f"Input: s={s}, target={target} -> Output: {maxScore(s), target}")
    # Test cases
    print(maxScore("011101"))  # Expected output: 5
    print(maxScore("00111"))   # Expected output: 4
    print(maxScore("1111"))    # Expected output: 3
    print(maxScore("0000"))    # Expected output: 3
