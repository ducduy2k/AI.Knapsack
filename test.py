from OR import knapsack_or
from GA import solver_knapsack_ga
import time
import signal
import resource

def signal_handler(signum, frame):
    f = open('result.txt', 'a')
    f.write(',#NA,#NA')
    f.close()
    print('time out')
    raise Exception("Timed out!")


signal.signal(signal.SIGALRM, signal_handler)
### limit 


# Khoi tao file
import os

f=open('result/index.txt','r')
i=int(f.readline())
f.close()
f=open('result/index.txt','w')
f.write(str(i+1))
f.close()
os.rename('result.txt','result/result_'+str(i)+'.txt')

result = 'result.txt'
f = open(result, 'w')
f.write(',,,GA,,,OR,,,\n,,,weight,value,time,weight,value,time')
f.close()
f = open('kplib/type.txt')
type = f.read().split()
size = open('kplib/size.txt').read().split()

# Chạy 2 functions

timelimit = 300


for t in type:
    o = open(result, 'a')
    o.write('\n'+str(t))
    o.close()
    for s in size:
        o = open(result, 'a')
        o.write('\n,'+str(s))
        o.close()
        for x in ['R01000', 'R10000']:
            f = open('kplib/'+t+'/'+s+'/'+x+'/s000.kp')
            a = f.read()
            f.close()
            test = open('test.txt', 'w')
            test.write(a)
            o = open(result, 'a')
            o.write('\n,,'+str(x))
            o.close()   
            test.close()
            # Genetic algorithm
            timestart = time.time()
            signal.alarm(timelimit)   # seconds
            try:
                solver_knapsack_ga.main()
            except:
                Exception
            timeend = time.time()
            f = open('result.txt', 'a')
            f.write(','+str((timeend-timestart)*100//1/100))
            f.close()
            # OR tool]
            timestart = time.time()
            signal.alarm(timelimit)   # seconds
            try:
                knapsack_or.main()
            except:
                Exception
            timeend = time.time()
            f = open('result.txt', 'a')
            f.write(','+str((timeend-timestart)*100//1/100))
            f.close()
