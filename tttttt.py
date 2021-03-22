f, b, n = 5,7,15
t = ''
for i in range(1,n+1):
    if i%b == 0 and i%f ==0:
        if t =='':
            t+=str(i-1)
            print(t)
        else:
            t+='-'+str(i-1)
            print(t)
        print('FizzBuzz')
        t =''
    elif i%f ==0 :
        if t =='':
            t+=str(i-1)
            print(t)
        else:
            t+='-'+str(i-1)
            print(t)
        print('Fizz')
        t =''
    elif i%b ==0:
        if t =='':
            t+=str(i-1)
            print(t)
        else:
            t+='-'+str(i-1)
            print(t)
        print('Buzz')
        t =''
    else:
        if t =='':
            t+=str(i)