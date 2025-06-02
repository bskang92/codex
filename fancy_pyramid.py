import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import cm
import numpy as np

"""Generate a colorful 3D pyramid with gradient faces.
This script enhances the basic pyramid demo by applying a brighter
colormap, thicker edge lines and outputs the figure as ``fancy_pyramid.png``.
"""

# Pyramid height
height = 1.5

# Square base coordinates
base = np.array([
    [0.0, 0.0, 0.0],
    [1.0, 0.0, 0.0],
    [1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0]
])

# Apex position
apex = np.array([0.5, 0.5, height])

# Define faces (four sides and the base)
faces = [
    [base[0], base[1], apex],
    [base[1], base[2], apex],
    [base[2], base[3], apex],
    [base[3], base[0], apex],
    [base[0], base[1], base[2], base[3]]
]

# Apply vibrant colors to each face
colors = cm.magma(np.linspace(0.2, 0.8, len(faces)))

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection="3d")

poly = Poly3DCollection(
    faces,
    facecolors=colors,
    edgecolors="white",
    linewidths=1.5,
    alpha=0.95,
)
ax.add_collection3d(poly)

# Set limits and viewing angle
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, height)
ax.axis("off")
ax.view_init(elev=30, azim=35)

plt.tight_layout()
plt.savefig("fancy_pyramid.png", dpi=300)
print("Saved fancy_pyramid.png")
