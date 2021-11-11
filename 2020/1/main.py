import time

with open('input') as f:
    report = [int(l) for l in f]

a = time.perf_counter()

for n,i in enumerate(report):
    for m in range(n, len(report)):
        for l in range(m, len(report)):
            j = report[m]
            k = report[l]
            if (i != j != k) and (i + j + k == 2020):
                print(i * j * k)

b = time.perf_counter()

print(f'took {round((b-a) * 1e3)}ms')