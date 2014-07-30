from string import *
def countSubStringMatch(target,key):
    """countSubStringMatch(TargetString, KeyString)"""
    index = -1
    count = 0
    index = find(target,key)
    if index == -1 :
        print "Key string not found in target string."
    else :
        while index != -1 :
            count += 1
            index = find(target,key,index+len(key))
        print "The key string is",count,"times in the target string"
            

def countSubStringMatchRecursive(target,key,count):
    """Recursively finds the number of times key string is present in the target string."""
    print target
    index = find(target,key)
    if index < 0 :
        return 0
    else :
        count += countSubStringMatchRecursive(target[index+len(key):len(target)+1],key,count)
        count += 1
        print count
        return count


def recCountString():
    """"Input strings for testing."""
    target = raw_input("Enter target string: ")
    key = raw_input("Enter key string: ")
    count = countSubStringMatchRecursive(target,key,0)
    print "count is",count
