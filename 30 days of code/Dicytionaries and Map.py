n=int(input())
d={}
for i in range(n):
    a=input()
    name,number=a.split()
    d[name]=number

for i in range(0, n):
    name = input()
    if name in d:
        print(f"{name}={d[name]}")
    else:
        print("Not found")
    
