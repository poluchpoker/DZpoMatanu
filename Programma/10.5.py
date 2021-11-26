import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x = sp.Symbol('x')

f = (sp.tan(x))**(4*x)
f1 = f.diff(x)
print("f' =", f1)


fig = plt.subplots()
y = np.linspace(0, 3, 100)
q = lambda x: (np.tan(x))**(4*x)
g = lambda x: (4*x*(np.tan(x)**2 + 1)/np.tan(x) + 4*np.log(np.tan(x)))*np.tan(x)**(4*x)
plt.plot(y, q(y))

plt.show()

plt.plot(y, g(y))

plt.show()