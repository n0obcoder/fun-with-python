import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

start_time = time.time()

def animate(i):
  xar = list(np.random.randint(0, 10, 7))
  yar = list(np.random.randint(0, 10, 7))

  ax1.clear()
  ax1.plot(xar, yar)
  
curren_time = time.time() - start_time
_, s = divmod(current_time, 60)

print(f'current_time: {round(s, 3)} secs')

ani = animation.FuncAnimation(fig, animate, fargs = None, interval = 1000)
plt.show()
