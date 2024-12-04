def compute():
    chars = []
    with open("input.txt", "r") as f:
        for line in f:
            chars.append(list(line.strip()))

    count = 0
    # see horizontal forward
    for i in range(len(chars)):
        for j in range(len(chars[0])-3):
            if(chars[i][j] == "X" and chars[i][j+1] == "M" and chars[i][j+2] == "A" and chars[i][j+3] == "S"):
                count += 1
            if(chars[i][j] == "S" and chars[i][j+1] == "A" and chars[i][j+2] == "M" and chars[i][j+3] == "X"):
                count += 1
   
    for i in range(len(chars)-3):
        for j in range(len(chars[0])):
            if(chars[i][j] == "X" and chars[i+1][j] == "M" and chars[i+2][j] == "A" and chars[i+3][j] == "S"):
                count += 1
            if(chars[i][j] == "S" and chars[i+1][j] == "A" and chars[i+2][j] == "M" and chars[i+3][j] == "X"):
                count += 1
   
    for i in range(len(chars)-3):
        for j in range(len(chars[0])-3):
            if(chars[i][j] == "X" and chars[i+1][j+1] == "M" and chars[i+2][j+2] == "A" and chars[i+3][j+3] == "S"):
                count += 1
            if(chars[i][j] == "S" and chars[i+1][j+1] == "A" and chars[i+2][j+2] == "M" and chars[i+3][j+3] == "X"):
                count += 1
  
    for i in range(3, len(chars)):
        for j in range(len(chars[0]) - 3):
            # Bottom-left to top-right diagonal
            if (chars[i][j] == "X" and chars[i-1][j+1] == "M" and chars[i-2][j+2] == "A" and chars[i-3][j+3] == "S"):
                count += 1
            if (chars[i][j] == "S" and chars[i-1][j+1] == "A" and chars[i-2][j+2] == "M" and chars[i-3][j+3] == "X"):
                count += 1


    return count

def compute2():
    chars = []
    with open("input.txt", "r") as f:
        for line in f:
            chars.append(list(line.strip()))

    count = 0
    for i in range(1, len(chars)-1): 
        for j in range(1, len(chars[0])-1):
            if(chars[i][j] == "A"):
                if((chars[i-1][j-1] == "M" and chars[i+1][j+1] == "S" or chars[i-1][j-1] == "S" and chars[i+1][j+1] == "M") and (chars[i+1][j-1] == "M" and chars[i-1][j+1] == "S" or chars[i+1][j-1] == "S" and chars[i-1][j+1] == "M")):
                    count += 1

    return count

print(compute())
print(compute2())
