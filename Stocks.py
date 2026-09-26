import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 31)
prices = 100 + np.cumsum(np.random.randn(30)) 

plt.plot(days, prices, marker='o', linestyle='-', color='green')
plt.title("Simulated Stock Price")
plt.xlabel("Day")
plt.ylabel("Price ($)")
plt.grid(True)
plt.show()