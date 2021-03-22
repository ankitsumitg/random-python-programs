#You have x no. of letters of A and B. You have to ensure that
#B is not beside B, but A can be beside A or B.
#Find the number of ways A and B can be arranged.
#For eg. def no._of_ways_AB(x):
#x=int(x)>0
#no._of_ways_AB(1):Ans=2 (as it can be arranged as A,B)
#no._of_ways_AB(2):Ans=3 (as it can be arranged as AB,BA ,AA)
#no._of_ways_AB(3):Ans= 5 (as it can be arranged as AAA,ABA,AAB,BAA,BAB)
#no._of_ways_AB(4):Ans=8(AAAA,ABAA,ABAB,AABA,AAAB,BAAA,BABA,BAAB)
#no. of ways AB(5): Ans=13(AAAAA,ABAAA,ABABA,ABAAB,AABAA,AABAB,AAABA,
#AAAAB,BAAAA,BABAA,BABAB,BAABA,BAAAB)

letters = ['A','B']
ans = ['A','B']
def sol(x):
    global ans
    print(len(ans))
    if len(ans[0]) == x:
        return len(ans)
    temp = list()
    for i in letters:
        for j in ans:
            if not (i == 'B' and j[-1] =='B') :
                temp.append(j+i)
    ans = temp
    return sol(x)

def no_of_ways_AB(x):
    return sol(x)
#hint its just fibbonaci series
print(no_of_ways_AB(7))
