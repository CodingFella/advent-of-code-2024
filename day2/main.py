def isSafe(nums):
    if(len(nums) <= 1):
        return True

    # decreasing
    if(nums[1] < nums[0]):
        for i in range(len(nums)-1):
            if(nums[i+1] >= nums[i] or abs(nums[i+1]-nums[i]) > 3):
                return False
    # increasing
    elif(nums[1] > nums[0]):
        for i in range(len(nums)-1):
            if(nums[i+1] <= nums[i] or abs(nums[i+1]-nums[i]) > 3):
                return False
    else:
        return False

    return True

def problemDampener(nums):
    temp = [x for x in nums]
    for i in range(len(nums)):
        del temp[i]
        if(isSafe(temp)):
            return True
        temp = [x for x in nums]
    return False

def compute():
    count = 0
    with open("input.txt", "r") as f:
        for line in f:
            str_list = line.split(" ")
            int_list = [int(x) for x in str_list]
            if(problemDampener(int_list)):
                count += 1
                print(int_list)
    return count

print(compute())
