import time
import numpy as np
import matplotlib.pyplot as plt


sizes = np.linspace(100, 1000000, 100)
times = []
for size in sizes:
    vals = set(np.random.randint(1, 10000000, size))
    ts = []
    for j in range(50):
        start = time.time()
        for i in range(1, 10000):
            x = np.random.randint(1,1000000)
            blah = (x in vals)            
        ts.append(time.time() - start)
    times.append(np.amin(ts) * 1000)

p = np.polyfit(sizes, times, 1)
print p

plt.plot(sizes, times, 'o')

xs = np.array([sizes[0], sizes[-1]])
plt.plot(xs, p[0]*xs + p[1], 'r--', lw=2)
plt.gca().set_ylim(ymin=0, ymax=np.amax(times)*1.5)

plt.show()
