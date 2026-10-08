# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys

import statistics
numbers = read_numbers()
if len(numbers) == 0:
    sys.exit("Error: no numbers provided")

print("Minimum =", str(min(numbers)))
print("Maximum =", str(max(numbers)))
print("Mean =", statistics.mean(numbers))
print("Median =", statistics.median(numbers))
