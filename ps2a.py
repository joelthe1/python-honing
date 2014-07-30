#a = b = c = 0
ansf = 0
iterv = 1
count = 0
temp = 0
breakFlag = False
testc = [0,0]
while testc[0] != 6:
    for c in range(0,11):
        if breakFlag == True:
            break
        for b in range(0,11):
            if breakFlag == True:
                break
            for a in range(0,11):
                temp = (6*a) + (9*b) + (20*c)
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
    iterv += 1
print "Largest number of McNuggets that cannot be bought in exact quantity: ",ansf
