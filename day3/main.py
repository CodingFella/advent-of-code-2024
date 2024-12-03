import re

def compute():
    contents = "";
    with open("input.txt", "r") as f:
        contents = f.read()
    
    total = 0
    x = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", contents)
    
    enabled = True

    for match in x:
        if "do()" in match:
            enabled = True 
        elif "don't()" in match:
            enabled = False
        elif enabled:
            print(match)
            m = re.findall(r"mul\((\d+),(\d+)\)", match)
            a, b = m[0]
            print(m[0])
            total += int(a) * int(b)
    return total

print(compute())
