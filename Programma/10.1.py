import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

x, y = sym.symbols('x y')

f = x ** 4 * 3 + 30 * x ** 2 - 9 * x ** 3 - 27 * x + 63

f1 = f.diff(x)

print("f' =", f1)

x = np.arange(-1, 1, 0.01)

plt.plot(x, (3 * x ** 4 + 30 * x ** 2 - 9 * x ** 3 - 27 * x + 63))

plt.show()

plt.plot(x, 12*x**3 - 27*x**2 + 60*x - 27)

plt.show()
