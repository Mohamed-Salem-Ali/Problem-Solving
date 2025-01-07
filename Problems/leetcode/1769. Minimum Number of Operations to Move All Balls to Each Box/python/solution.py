from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        Calculate the minimum number of operations to move all balls to each box.

        For each box, the number of operations is defined as the sum of the absolute distances
        between that box and every other box containing a ball.

        Args:
            boxes (str): A binary string where each character represents a box. '1' indicates
                         the box contains a ball, and '0' indicates it is empty.

        Returns:
            List[int]: A list of integers where the i-th element represents the minimum number of
                       operations required to move all balls to the i-th box.
        """
        indices = []
        output = []

        # Collect indices of boxes that contain balls
        for i in range(len(boxes)):
            if boxes[i] == '1':
                indices.append(i)

        # Calculate operations for each box
        for j in range(len(boxes)):
            s = 0
            for k in indices:
                s += abs(j - k)
            output.append(s)

        return output

if __name__ == "__main__":
    # Test cases
    solution = Solution()

    # Test case 1
    boxes = "110"
    print(solution.minOperations(boxes))  # Expected output: [1, 1, 3]

    # Test case 2
    boxes = "001"
    print(solution.minOperations(boxes))  # Expected output: [2, 1, 0]

    # Test case 3
    boxes = "101"
    print(solution.minOperations(boxes))  # Expected output: [2, 2, 2]

    # Test case 4
    boxes = "000"
    print(solution.minOperations(boxes))  # Expected output: [0, 0, 0]

    # Test case 5
    boxes = "111"
    print(solution.minOperations(boxes))  # Expected output: [3, 2, 3]
