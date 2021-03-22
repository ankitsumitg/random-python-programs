import math
test_case = int(input().strip().split()[0])
i = 0
for i in range( test_case):
    n = int(input().strip().split()[0])
    temp =input().strip().split()
    p,q = int(temp[0]),int(temp[1])
    whole= math.floor(p/q)
    dec = p/q -whole
    sumofdecimal = 0
    while(n):
        sumofdecimal =sumofdecimal+ (100*dec)//10
        dec =dec*10
        whole= math.floor(dec)
        dec = dec - whole
        n=n-1
    print(sumofdecimal)