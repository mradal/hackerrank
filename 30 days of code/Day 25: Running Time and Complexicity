# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def check(n):
    if n<=1:
        return False
    s=math.sqrt(n)
    if s.is_integer():
        return False
    for i in range(2,int(s)+1):
        if n%i==0:
            return False
    return True
    
t=int(input())
for i in range(t):
    n=int(input())
    if check(n):
        print("Prime")
    else:
        print("Not prime")

