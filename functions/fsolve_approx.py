import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Define the function
def func(x):
    return np.exp(x) - np.cos(x)

# Define a range of x values
x = np.linspace(-2, 2, 400)

# Plot the functions
plt.plot(x, np.exp(x), label=r'$e^x$')
plt.plot(x, np.cos(x), label=r'$\cos(x)$')
plt.plot(x, func(x), label=r'$e^x - \cos(x)$')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $e^x$ and $\cos(x)$')

# Use fsolve to find the root
initial_guesses = [-1, 0, 1]
roots = [fsolve(func, guess) for guess in initial_guesses]

# Plot the roots
for root in roots:
    plt.plot(root, np.exp(root), 'ro')  # plotting roots on e^x

plt.show()

# Print the roots
print("Roots of e^x - cos(x) = 0:")
for root in roots:
    print(f"x ≈ {root[0]}")
