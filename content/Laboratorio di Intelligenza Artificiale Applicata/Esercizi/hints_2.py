# Complete the following function by adding the correct type hints. The 
# function takes a list of numbers and returns a dictionary containing the sum 
# and average of the numbers
# def analyze_numbers(numbers):
#     total = sum(numbers)
#     average = total / len(numbers) if numbers else 0
#     return {"sum": total, "average": average}

from typing import List, Tuple

def analyze_numbers(numbers : List[int]) -> Tuple[int, int]:
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return {"sum": total, "average": average}
