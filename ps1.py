x = 1
count = 0
while count < 1000:
    y = x/2
    z = 2
    while True:
        if z > y:
            count+=1
           # print x
            break
        if x%z == 0:
            break;
        z+=1
    if count < 1000 :
        x+=2
print "The 1000th prime is: ",x
