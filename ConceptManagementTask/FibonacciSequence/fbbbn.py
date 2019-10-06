import time
from datetime import datetime
# start1 = time.time()
start = datetime.now()
n = 3
y = 0
l1 = [0,1]
for x in range(n-1):
    # print(x)
    y = l1[x] +l1[x+1]
    l1.append(y)

# print(l1[n])
# print(len(l1))
# end1 = time.time()
# print(start1)
# print(end1)
end = datetime.now()
time_taken = end - start
print('Time: ',time_taken)