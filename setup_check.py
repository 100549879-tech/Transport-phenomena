import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(f"NumPy version: {np.__version__}")
print(f"Matplotlib version: {matplotlib.__version__}")
print(f"OpenCV version: {cv2.__version__}")

x = np.arange(5)
y = x**2

plt.plot(x, y, marker="o")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("setup_check.png")
plt.show()
