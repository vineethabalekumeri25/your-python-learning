# 02_functions/lambda_and_map.py
# Using lambda and map functions

nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, nums))
print("Squares:", squares)