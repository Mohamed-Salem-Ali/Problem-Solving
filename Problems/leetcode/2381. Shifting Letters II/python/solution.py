from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        """
        Shifts the letters of a string based on the given operations.

        Each operation in `shifts` specifies a range of indices to shift and a direction.
        - If `direction` is 1, shift letters forward in the alphabet.
        - If `direction` is 0, shift letters backward in the alphabet.

        Args:
            s (str): The input string consisting of lowercase English letters.
            shifts (List[List[int]]): A list of shifts, where each shift is represented as
                                       [start, end, direction].
                                       - `start` and `end` are the inclusive indices of the range.
                                       - `direction` is 1 (forward) or 0 (backward).

        Returns:
            str: The string after applying all shifts.
        """
        n = len(s)
        prefix_sum = [0] * (n + 1)

        # Build the prefix sum array based on shifts
        for start, end, direction in shifts:
            prefix_sum[start] += (1 if direction == 1 else -1)
            if end + 1 < n:
                prefix_sum[end + 1] -= (1 if direction == 1 else -1)

        # Apply the shifts to the string
        curr_shift = 0
        s = list(s)
        for i in range(n):
            curr_shift += prefix_sum[i]
            s[i] = chr((ord(s[i]) - ord('a') + curr_shift) % 26 + ord('a'))

        return "".join(s)

if __name__ == "__main__":
    # Test cases
    solution = Solution()

    # Test case 1
    s = "abc"
    shifts = [[0, 1, 1], [1, 2, 0]]
    print(solution.shiftingLetters(s, shifts))  # Expected output: "bbb"

    # Test case 2
    s = "xyz"
    shifts = [[0, 2, 1]]
    print(solution.shiftingLetters(s, shifts))  # Expected output: "yza"

    # Test case 3
    s = "aaa"
    shifts = [[0, 0, 1], [1, 1, 0], [2, 2, 1]]
    print(solution.shiftingLetters(s, shifts))  # Expected output: "bzb"

    # Test case 4
    s = "z"
    shifts = [[0, 0, 1], [0, 0, 0]]
    print(solution.shiftingLetters(s, shifts))  # Expected output: "z"

    # Test case 5
    s = "abcdef"
    shifts = [[0, 5, 1], [0, 2, 0]]
    print(solution.shiftingLetters(s, shifts))  # Expected output: "abcefg"
