import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x, y = sp.symbols('x y')

f = x ** 0.5 + y ** 0.5 - 9
f1 = f.diff(x)
f2 = f.diff(y)
f3 = - f1/f2

print("f' =", f3)

fig = plt.subplots()
y = np.linspace(0, 82, 100000)
q = lambda x: x - 18*np.sqrt(x) + 81                      # sqrt(y) = 9 - sqrt(x), значит y = x - 18 * sqrt(x) + 81
g = lambda x: -1.0*(x - 18*np.sqrt(x) + 81)**0.5/x**0.5

plt.plot(y, q(y))

plt.show()

plt.plot(y, g(y))

plt.show()
