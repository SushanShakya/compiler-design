import time

n = 100

def code_motion_unoptimized():
    b = 10
    d = 20
    e = 30
    g = 40
    h = 50
    for i in range(n):
        a = b + i
        c = d + e
        f = g + h 

def code_motion_optimized():
    b = 10
    d = 20
    e = 30
    g = 40
    h = 50
    c = d + e
    f = g + h 
    for i in range(n):
        a = b + i


st1 = time.time()
code_motion_unoptimized();
et1 = time.time()
elt1 = et1 - st1


st2 = time.time()
code_motion_optimized();
et2 = time.time()
elt2 = et2 - st2

if elt1 > elt2:
    print("Optimized code is faster");
else:
    print("Unoptimized code is faster");
