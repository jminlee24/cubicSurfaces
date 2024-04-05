# %%
import pyvista as pv
import numpy as np
import sympy as sym

# %%
mesh = pv.examples.download_bunny()
mesh.plot(cpos='xy')


# %%
k = 18
x, y, z = np.mgrid[-10:10:50j, -10:10:50j, -10:10:50j]


def cubic(x, y, z, k):
  return x**2 + y**2 + z**2 - x * y * z - k - 2


x, y, z = sym.symbols('x y z')
eq = sym.Eq(0, cubic(x, y, z, 18))

eqs = eqs = [v.replace('sqrt', 'np.sqrt') for v in map(str, sym.solve(eq, z))]

print(eqs)
# %%
points = np.random.random((1000, 3))

pc = pv.PolyData(points)

print(points[:, 2])

pc.plot(scalars=points[:, 2], point_size=5.0, cmap="jet")

# %%
