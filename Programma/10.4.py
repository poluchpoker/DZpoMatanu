import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x = sp.Symbol('x')

f = sp.log(sp.tan(1/x))
f1 = f.diff(x)
print("f' =", f1)


fig = plt.subplots()
y = np.linspace(0, 5, 1000000)
y1 = np.linspace(0, 5, 10)
q = lambda x: np.log(np.tan(1/x))
g = lambda x: -(np.tan(1/x)**2 + 1)/(x**2*np.tan(1/x))
plt.plot(y, q(y))

plt.show()

plt.plot(y1, g(y1))

plt.show()