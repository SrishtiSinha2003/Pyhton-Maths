from matplotlib import pyplot as plt
import numpy as np
def plot_equations() :
    x = np.linspace(-10, 10, 100)
    y1 = (6 - 3 * x) / 2
    y2 = x - 4

    plt.plot(x, y1, label = "3x + 2y = 6")
    plt.plot(x, y2, label = "x - y = 4")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()
plot_equations()