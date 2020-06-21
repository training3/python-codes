strngs = []
for i in range(1,5):
    strngs.append(str(i))

print(','.join(strngs))

> 1,2,3,4
# OR
#for i in range(5):
#    print(i,end=",")
# but it will print , at the end of element as well.
