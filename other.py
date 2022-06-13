# Just small bulks of code, primarily from https://stepik.org/course/58852/info

# >>> https://stepik.org/lesson/298795/step/11?unit=280622
for n in range(1, 1000):
    for k in range(1, 1000):
        for m in range(1, 1000):
            if 28*n + 30*k + 31*m == 365:
                print('n=', n, ', k=', k, ', m=', m)
