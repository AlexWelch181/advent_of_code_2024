def is_safe(nums):
    diff = [nums[i-1] - nums[i] for i in range(1, len(nums))]
    return set(diff) <= {1,2,3} or set(diff) <= {-1,-2,-3}



with open('day_two_in.txt') as file:
    out1 = 0
    out2 = 0
    for line in file.readlines():
        nums = [int(num) for num in line.split()]
        N = len(nums)
        if is_safe(nums):
            out1 += 1
        if any([is_safe(nums[:i] + nums[i+1:]) for i in range(N)]):
            out2 += 1
    print(out1)
    print(out2)
       