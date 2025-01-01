# Solution
def maxScore(s):
        
        maximum_score = 0
        for i in range(1,len(s)):
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
