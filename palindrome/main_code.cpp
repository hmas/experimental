# Function to count palindromic substrings

def count_palindromic_substrings(s):
    # Initialize a counter to keep track of palindromic substrings
    count = 0
    n = len(s)

    # Function to expand around center and count palindromes
    def expand_around_center(left, right):
        nonlocal count
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    # Iterate over each character and consider it as the center of a palindrome
    for i in range(n):
        # Odd length palindromes (single character center)
        expand_around_center(i, i)
        # Even length palindromes (two character center)
        expand_around_center(i, i + 1)

    return count

# Example usage
print(count_palindromic_substrings("abba"))  # Output: 6 (a, b, b, a, bb, abba)