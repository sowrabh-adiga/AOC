def FindTrees(x,y):
    f = open("AOC_day3_input.txt")
    l1 = f.readline().rstrip()
    i = 0
    count =0
    while True:
        if y > 1:
            for _ in range(y-1):
                l3 = f.readline()
        l2 = f.readline().rstrip()
        if not l2: break  #EOF
        i =(i + x)% len(l2)
        if l2[i] == "#":
            count +=1
    f.close()
    return count

stepx = [1,3,5,7,1]
stepy = [1,1,1,1,2]
result =[]
mul = 1
for ele in range(len(stepx)):
    result += [FindTrees(stepx[ele],stepy[ele])]
    mul *= result[ele]

print(f"List of Tree counts is {result} \nThe Product is {mul}")