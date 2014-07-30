def isPalindrome(x):
    if len(x) <= 1:
        return True
    else x[0] == x[-1] and isPalindrome(x[1:-1])
