# Just small bulks of code, primarily from https://stepik.org/course/58852/info

# >>> https://stepik.org/lesson/298795/step/11?unit=280622
for n in range(1, 10):
    for k in range(1, 10):
        for m in range(1, 10):
            if 28*n + 30*k + 31*m == 365:
                print('n=', n, ', k=', k, ', m=', m)    # (1): n= 1 , k= 4 , m= 7; (2): n= 2 , k= 1 , m= 9


# >>> https://stepik.org/lesson/298795/step/12?unit=280622
# 10*b + 5*k + 0.5*t = 100
for b in range(1, 10):
    for k in range(1, 20):
        for t in range(1, 200):
            if 10*b + 5*k + 0.5*t == 100 and b + k + t == 100:
                print('b=', b, ', k=', k, ', t=', t)    # b= 1 , k= 9 , t= 90
