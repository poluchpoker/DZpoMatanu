import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

x, y = sym.symbols('x y')

f = x + (2 * x) / (x ** 2 + 1)

f1 = f.diff(x)

print("f' = ", f1)

x = np.arange(-1, 1, 0.01)

plt.plot(x, (x + (2 * x) / (x ** 2 + 1)))

plt.show()

plt.plot(x, -4*x**2/(x**2 + 1)**2 + 1 + 2/(x**2 + 1))

plt.show()
