import sys
 
result = ''
for i in range(1,len(sys.argv),2):
    arg1=sys.argv[i]
    arg2=sys.argv[i+1]
    n = int(arg1)
    m = int(arg2)
    j = 1
    while True:
        result +=str(j)
        j = 1 + (j + m - 2) % n
        if j == 1:
            break
print(result)
