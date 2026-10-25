# how to check version of matplotib
import matplotlib
print(matplotlib.__version__)

import matplotlib.pyplot as plt
fig, ax =plt.subplots(figsize=(8,4))
ax.plot([1,2,3,4],[10,14,12,18],marker="o")
ax.set_title("weeky output")
ax.set_xlabel("week")
ax.set_ylabel("units")
ax.grid(True,alpha=0.3)
fig.tight_layout()
plt.show()

import matplotlib.pyplot as plt
marks=[10,20,30]
plt.plot(marks)
plt.show()


