ansf = 0
iterv = 1
count = 0
temp = 0
breakFlag = False
testc = [0,0]
A = int(raw_input("Enter size of the package A: "))
B = int(raw_input("Enter size of the package B: "))
C = int(raw_input("Enter size of the package C: "))
limit = int(raw_input("Enter the upper bound of the search: "))
while testc[0] != 6:
    for c in range(0,(limit/C)+1):
        if breakFlag == True:
            break
        for b in range(0,(limit/B)+1):
            if breakFlag == True:
                break
            for a in range(0,(limit/A)+1):
                temp = (A*a) + (B*b) + (C*c)
                if temp == iterv:
                    if iterv - testc[1] == 1:
                        testc[0] += 1
                    else:
                        testc[0] = 0
                    testc[1] = iterv
                    breakFlag = True
                    break
    if breakFlag == False:
        ansf = iterv
    breakFlag = False
    if (iterv > limit):
        break
    iterv += 1
print "Given package sizes ", A ,", ", B ,", and" , C , "the largest number of McNuggets that cannot be bought in exact quantity is: ",ansf
