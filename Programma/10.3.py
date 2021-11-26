import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x = sp.Symbol('x')

f = sp.acos(sp.sqrt(1-3*x))
f1 = f.diff(x)
print("f' =", f1)

fig = plt.subplots()
y = np.linspace(0, 1, 1000)
y1 = np.linspace(0, 1, 1000)
q = lambda x: np.arccos(np.sqrt(1-3*x))
g = lambda x: np.sqrt(3)/(2*np.sqrt(x)*np.sqrt(1 - 3*x))

plt.plot(y, q(y))

plt.show()

plt.plot(y1, g(y1))

plt.show()
