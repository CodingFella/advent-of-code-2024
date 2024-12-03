def compute():
    left = []
    right = []
    with open("input_day1.txt", "r") as f:
        for line in f:
            left.append(int(line.split("   ")[0]))
            right.append(int(line.split("   ")[1]))

    left.sort()
    right.sort()
    
    diff = 0

    for i in range(len(left)):
        diff += abs(left[i]-right[i])

    return diff

def compute_2():
    left = []
    right = []
    with open("input_day1.txt", "r") as f:
        for line in f:
            left.append(int(line.split("   ")[0]))
            right.append(int(line.split("   ")[1]))

    score = 0

    for i in range(len(left)):
        score += left[i] * right.count(left[i])
    
    return score

print(compute())

print(compute_2())
