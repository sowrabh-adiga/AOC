
#----------------------problem 1 --------------------------#
'''
result = 0
with open("AOC_day2_input.txt") as obj:
    for line in obj:
        temp1,temp2 = line.split(":")  #get two halfs after splitting at ':'
        temp3,temp4 = temp1.split()  #split first value at space
        low,high = map(int,temp3. split("-"))
        count1 = temp2.count(temp4)
        if (count1<=high) and (count1>=low):
            result +=1

print(result)
'''        
#----------------------problem 1 --------------------------#



#----------------------problem 2 --------------------------#
result = 0
with open("AOC_day2_input.txt") as obj:
    for line in obj:
        temp1,temp2 = line.split(":")  #get two halfs after splitting at ':'
        temp3,temp4 = temp1.split()  #split first value at space
        low,high = map(int,temp3. split("-"))
        if temp2[low] != temp2[high]:
            if (temp2[low] == temp4) or (temp2[high] == temp4):
                result +=1            

print(result)



#----------------------problem 2 --------------------------#