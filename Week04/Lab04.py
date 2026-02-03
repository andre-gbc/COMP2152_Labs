# Lab 04: Loops and Functions Practice
# Student Name: Andre Antoine
# Date: Feb 3

# ============================================
# Question 1: Robot Return to Origin
# ============================================

def robot_returns_to_origin(moves):
    # Initialize starting position
    x = 0
    y = 0

    for move in moves:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'L':
            x -= 1
        elif move == 'R':
            x += 1

    # TODO: Loop through each move and update x, y
    # TODO: Return True if back at origin, False otherwise

    return x == 0 and y == 0

# Test cases
test_moves = ["UD", "LL", "UDLR", "LDRRLRUULR"]

for moves in test_moves:
    result = robot_returns_to_origin(moves)
    print("Moves '" + moves + "': Returns to origin? " + str(result))

# ============================================
# Question 2: Two Sum
# ============================================

# Part A: Brute Force with Nested Loops
def two_sum_brute_force(numbers, target):
    # TODO: Use nested loops to find the pair
    # Outer loop: i from 0 to len(numbers)
    # Inner loop: j from i+1 to len(numbers)

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (i, j)

    return None

# Part B: Optimized with Dictionary
def two_sum_optimized(numbers, target):
    seen = {}  
    for i in range(len(numbers)):
        needed = target - numbers[i]
        if needed in seen:
            return (seen[needed],i)
        seen[numbers[i]] = i
    
    return None


# Test cases
test_cases = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6),
    ([1, 5, 3, 8, 2], 10)
]


# ============================================
# Question 3: Shuffle the Array
# ============================================

def shuffle_array(nums, n):
    # Step 1: Split into two halves using slicing
    first_half = nums[:n]    # TODO: slice from start to n
    second_half = nums[n:]   # TODO: slice from n to end

    # Step 2: Create empty result list
    result = []

    # Step 3:
    for i in range(n):
        result.append(first_half[i])
        result.append(second_half[i])

    return result

# Test cases
test_cases = [
    ([2, 5, 1, 3, 4, 7], 3),
    ([1, 2, 3, 4, 4, 3, 2, 1], 4),
    ([1, 1, 2, 2], 2)
]

# ============================================
# Question 4: First Unique Character
# ============================================

def count_characters(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts

# Main function: Find first unique character
def first_unique_character(s):
    # Step 1: Get character counts using helper function
    char_counts = count_characters(s)
    for i in range(len(s)):
        if char_counts[s[i]] == 1:
            return i
    return -1

# Test cases
test_strings = ["leetcode", "loveleetcode", "aabb", "python", "aabbcc"]