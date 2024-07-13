import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, axs = plt.subplots(2)

axs[0].plot(x, y1)
axs[0].set_title('Sine')

axs[1].plot(x, y2)
axs[1].set_title('Cosine')

plt.tight_layout()
plt.show()
