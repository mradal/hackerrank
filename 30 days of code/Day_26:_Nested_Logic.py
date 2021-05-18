d1,m1,y1 = [int(e) for e in input().strip().split(' ')]
d2,m2,y2= [int(e) for e in input().strip().split(' ')]

# Check the biggest category: year
if y1<y2:
    print(0)
elif y1==y2:
    # Check the next biggest category: month
    if m1<m2:
        print(0)
    elif m1 == m2:
        # Check the last category: day
        if d1 <= d2:
            print(0)
        else:
            print(str((d1-d2) * 15))
    else:
        print(str((m1-m2) * 500))
else:
    print('10000')
