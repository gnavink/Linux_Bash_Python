nums = [1, 2, 3, 4, 5]

n = 100
squares = [n * n for n in nums]
print(squares)
squares = [n * n for n in nums if n > 2]     # [9, 16, 25]
print(squares)
print(f'Original value of n remains unchanged:{n}')