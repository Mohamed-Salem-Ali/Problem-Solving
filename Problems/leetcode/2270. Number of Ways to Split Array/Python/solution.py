from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        """
        Counts the number of ways to split the array into two non-empty parts 
        where the sum of the left part is greater than or equal to the sum 
        of the right part.

        Args:
            nums (List[int]): List of integers to split.

        Returns:
            int: The number of valid splits.
        """
        answer = 0  # Initialize the answer to 0
        L = 0       # Variable to store the sum of the left part
        R = sum(nums)  # Calculate the total sum of the array
        
        # Iterate through the array, excluding the last element
        for i in range(len(nums) - 1):
            L += nums[i]   # Add the current element to the left sum
            R -= nums[i]   # Subtract the current element from the right sum
            
            # Check if the left sum is greater than or equal to the right sum
            if L >= R:
                answer += 1  # Increment the count of valid splits
        
        return answer  # Return the total number of valid splits


# Sample test cases
solution = Solution()

# Test case 1
nums = [10, 4, -8, 7]
print(f"Input: nums={nums} -> Output: {solution.waysToSplitArray(nums)}")

# Test case 2
nums = [2, 3, 1, 0]
print(f"Input: nums={nums} -> Output: {solution.waysToSplitArray(nums)}")

# Test case 3
nums = [1, 2, 3, 4, 5]
print(f"Input: nums={nums} -> Output: {solution.waysToSplitArray(nums)}")

# Test case 4
nums = [-1, -2, -3, -4]
print(f"Input: nums={nums} -> Output: {solution.waysToSplitArray(nums)}")

# Test case 5
nums = [5, 5, 5, 5, 5]
print(f"Input: nums={nums} -> Output: {solution.waysToSplitArray(nums)}")

# expected output  

# Input: nums = [10, 4, -8, 7]
# Output: 2

# Input: nums = [2, 3, 1, 0]
# Output: 2

# Input: nums = [1, 2, 3, 4, 5]
# Output: 1

# Input: nums = [-1, -2, -3, -4]
# Output: 2

# Input: nums = [5, 5, 5, 5, 5]
# Output: 2