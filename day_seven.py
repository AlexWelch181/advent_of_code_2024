import time

part_two = True

# Average time approx 4s for part 2
start = time.time()
with open('day_seven_in.txt') as file:
    out = 0
    for line in file.readlines():
        target, nums = line.strip('\n').split(':')
        target = int(target)
        nums = [int(n) for n in nums.split()]
        results = [nums[0]]
        for idx in range(1, len(nums)):
            tmp_results = []
            for res in results:
                if res <= target:    
                    tmp_results.append(res + nums[idx])
                    tmp_results.append(res * nums[idx])
                    if part_two:
                        tmp_results.append(int(f'{res}{nums[idx]}'))
            results = tmp_results
        if target in results:
            out += target
    print(out)
print(time.time() - start)


# Average time approx 0.05s for part 2
start = time.time()
with open('day_seven_in.txt') as file:
    out = 0
    for line in file.readlines():
        target, nums = line.strip('\n').split(':')
        nums = [int(n) for n in nums.split()]
        results = [int(target)]
        for idx in range(len(nums)-1, -1, -1):
            tmp_results = []
            for res in results:
                if res - nums[idx] > 0:
                    tmp_results.append(res - nums[idx])
                if res % nums[idx] == 0:
                    tmp_results.append(res // nums[idx])
                if part_two:
                    str_num, str_target = str(nums[idx]), str(res)
                    if str_target.endswith(str_num):
                        val = str_target[:len(str_target) - len(str_num)]
                        tmp_results.append(int(val) if val else 0)
            results = tmp_results
        if 1 in results:
            out += int(target)
    print(out)
print(time.time() - start)