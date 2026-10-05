# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import statistics

numbers = read_numbers()
print("Minimum =", str(min(numbers)))
print("Maximum =", str(max(numbers)))
print("Mean =", statistics.mean(numbers))
print("Median =", statistics.median(numbers))
