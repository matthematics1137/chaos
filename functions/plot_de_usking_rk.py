import numpy as np
import matplotlib.pyplot as plt

# Runge-Kutta method implementation
def runge_kutta(f, x0, t):
    n = len(t)
    x = np.zeros(n)
    x[0] = x0
    for i in range(1, n):
        h = t[i] - t[i - 1]
        k1 = h * f(x[i - 1], t[i - 1])
        k2 = h * f(x[i - 1] + 0.5 * k1, t[i - 1] + 0.5 * h)
        k3 = h * f(x[i - 1] + 0.5 * k2, t[i - 1] + 0.5 * h)
        k4 = h * f(x[i - 1] + k3, t[i - 1] + h)
        x[i] = x[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return x

# Differential equations
def f1(x, t):
    return 4 * x**2 - 16

def f2(x, t):
    return 1 - x**14

def f3(x, t):
    return x - x**3

def f4(x, t):
    return np.exp(-x) * np.sin(x)

def f5(x, t):
    return 1 + 0.5 * np.cos(x)

def f6(x, t):
    return 1 - 2 * np.cos(x)

# Time vector
t = np.linspace(0, 10, 1000)

# Initial conditions
initial_conditions = [-3, -1, 0, 1, 3]

# Plotting
fig, axes = plt.subplots(3, 2, figsize=(15, 15))

functions = [f1, f2, f3, f4, f5, f6]
titles = [
    r"$\dot{x} = 4x^2 - 16$",
    r"$\dot{x} = 1 - x^{14}$",
    r"$\dot{x} = x - x^3$",
    r"$\dot{x} = e^{-x} \sin x$",
    r"$\dot{x} = 1 + \frac{1}{2} \cos x$",
    r"$\dot{x} = 1 - 2 \cos x$"
]

for ax, f, title in zip(axes.flatten(), functions, titles):
    for x0 in initial_conditions:
        x = runge_kutta(f, x0, t)
        ax.plot(t, x, label=f"$x_0={x0}$")
    ax.set_title(title)
    ax.set_xlabel("t")
    ax.set_ylabel("x(t)")
    ax.legend()

plt.tight_layout()
plt.show()
