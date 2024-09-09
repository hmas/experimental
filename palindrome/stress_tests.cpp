# Stress test for the count_palindromic_substrings function
import time

# Generate a long string of repeated characters
long_string = "a" * 1000

start_time = time.time()
print(count_palindromic_substrings(long_string))  # Expected output: 500500
end_time = time.time()

print(f"Stress test took {end_time - start_time} seconds")