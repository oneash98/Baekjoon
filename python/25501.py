def recursion(s, l, r):
    global n
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: 
        n += 1
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(input())
for i in range(T):
    S = input()
    n = 1
    print(isPalindrome(S), n)