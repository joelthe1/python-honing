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
    matches = subStringMatchExact(target,key)
    print "match(es) =",matches

def subStringMatchExact(target,key,length):
        """subStringMatchExact(TargetString,KeyString) -> (Tuple of indexes of first letter of the key match)"""
        index = find(target,key)
        if index < 0:
            return ()
        else:
            matches = subStringMatchExact(target[index+len(key):len(target)],key,length)
            index += (length - len(target))
            matches += (index,)
            print matches
            return matches

"""def subStringMatchExact(target,key):
        subStringMatchExact(TargetString,KeyString) -> (List of indexes of first letter of the key match)
        index = find(target,key)
        #print 'here',target,key,index
        if index < 0:
            return []
        matches = subStringMatchExact(target[index+len(key):len(target)],key)
        offset = index + len(key)
        print matches
        if matches:
            for x in range(0, len(matches)) :
                matches[x] += offset
        matches.insert(0,index)
        return matches
"""
def subStringMatchExact(target,key):
        """subStringMatchExact(TargetString,KeyString) -> (List of indexes of first letter of the key match)"""
        index = find(target,key)
        #print 'here',target,key,index
        if index < 0:
            return ()
        matches = subStringMatchExact(target[index+len(key):len(target)],key)
        offset = index + len(key)
        temp_matches = ()
        print matches
        if matches:
            for x in range(0, len(matches)) :
               temp_matches += ((matches[x] + offset),)
        #matches.insert(0,index)
        temp_matches = (index,) + temp_matches
        return temp_matches
