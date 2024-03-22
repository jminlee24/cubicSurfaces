# %%
import pyvista as pv
import numpy as np

#%%
mesh = pv.examples.download_bunny()
mesh.plot(cpos='xy')


#%%
points = np.random.random((1000, 3))

pc = pv.PolyData(points)

print(points[:, 2])

pc.plot(scalars=points[:, 2], point_size=5.0, cmap="jet")
