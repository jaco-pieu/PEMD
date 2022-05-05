import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import traitement


data = traitement.importdata("data1103.txt")

harvest = np.array(data)

fig, ax = plt.subplots()
im = ax.imshow(harvest)

# Show all ticks and label them with the respective list entries
ax.set_xticks([])
ax.set_yticks([])

cbar = ax.figure.colorbar(im, ax=ax,)
cbar.ax.set_ylabel("taille (cm)", rotation=-90, va="bottom")

data = harvest
ax.spines[:].set_visible(False)

ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
ax.tick_params(which="minor", bottom=False, left=False)

# Loop over data dimensions and create text annotations.
for i in range(8):
    for j in range(8):
        text = ax.text(j, i, harvest[i, j],
                       ha="center", va="center", color="w")
ax.set_title("taille des plants en fonction de leur position")
fig.tight_layout()
plt.show()