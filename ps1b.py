import math
limit = int(raw_input("Enter the limit of primes: "))
x = 3
count = 1
logsum = math.log(2)
print 2, logsum
while x <= limit:
    y = x/2
    z = 2
    while True:
        if z > y:
            count+=1
            #print x
            logsum += math.log(x)            
            break
        if x%z == 0:
            break;
        z+=1
    if x <= limit :
        x+=2
print "The limit n is: ",limit
print "The sum of the log primes is: ",logsum
print "The ratio of sum to n is: ",logsum/limit
