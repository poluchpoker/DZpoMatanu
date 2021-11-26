import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
x, y, t = sp.symbols('x y t')

z = 1                    # константа при взяти производной не учитывается, можно избавиться приравняв к 1

f = z*(z - sp.sin(t))
f1 = z*sp.cos(t)
result1 = f.diff(t)
result2 = f1.diff(t)

result = result2/result1

print('Производная yx =', result)

fig = plt.subplots()
y = np.linspace(0, 3, 100)
q = lambda x: np.cos(np.arcsin(1 - x))
g = lambda x: np.sin(np.arcsin(1 - x))/np.cos(np.arcsin(1 - x))
plt.plot(y, q(y))

plt.show()

plt.plot(y, g(y))

plt.show()
