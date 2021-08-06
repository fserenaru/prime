import time
start=time.time()
#time1=time.strftime("%H:%M:%S")
#print(time1)
x=0;
for a in range(3,10000):
    x=0;

    for b in range(2,a):
        if(a%b==0):
            x +=1
    if x==0:
        print(a)
for i in range(17,1000000):
    x=0;
    if(i%2==1 and i%3!=0 and i%5!=0 and i%7!=0 and i%11!=0 and i%13!=0 and i%17!=0 and i%19!=0):
        for j in range(23,10000):
            if(i%j==0):
                x +=1
        if x==0:
            print(i)
#time2=time.strftime("%H:%M:%S")
#print(time2)
elapsed=time.time()-start
print(elapsed)