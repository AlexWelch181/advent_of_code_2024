from functools import cache

with open('day_eleven_in.txt') as file:
    nums = [int(num) for num in file.readline().split()]

@cache
def stone_sum(val, blinks):
    str_val = str(val)
    length = len(str_val)
    if blinks == 0:
        return 1
    elif val == 0:
        return stone_sum(1, blinks-1)
    elif length % 2 == 0:
        return stone_sum(int(str_val[:length//2]), blinks-1) + stone_sum(int(str_val[length//2:]), blinks-1)
    else:
        return stone_sum(2024*val, blinks-1)

print(sum([stone_sum(num, 75) for num in nums]))
