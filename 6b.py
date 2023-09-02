import time

n = 100

def loop_jamming_unoptimized():
    a = 0
    c = 0
    b = 10
    for i in range(n):
        a = b + i

    for i in range(n):
        c = b + i

def loop_jamming_optimized():
    a = 0
    c = 0
    b = 10
    for i in range(n):
        a = b + i
        c = b + i


st1 = time.time()
loop_jamming_unoptimized();
et1 = time.time()
elt1 = et1 - st1


st2 = time.time()
loop_jamming_optimized();
et2 = time.time()
elt2 = et2 - st2

if elt1 > elt2:
    print("Optimized code is faster");
else:
    print("Unoptimized code is faster");
