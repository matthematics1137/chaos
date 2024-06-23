import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the differential equation
def dx_dt(x, t):
    return x * (1 - x)

# Runge-Kutta 4th Order Method
def runge_kutta(f, x0, t):
    n = len(t)
    x = np.zeros(n)
    x[0] = x0
    for i in range(1, n):
        h = t[i] - t[i-1]
        k1 = h * f(x[i-1], t[i-1])
        k2 = h * f(x[i-1] + 0.5 * k1, t[i-1] + 0.5 * h)
        k3 = h * f(x[i-1] + 0.5 * k2, t[i-1] + 0.5 * h)
        k4 = h * f(x[i-1] + k3, t[i-1] + h)
        x[i] = x[i-1] + (k1 + 2*k2 + 2*k3 + k4) / 6
    return x

# Time steps
t = np.linspace(0, 10, 100)

# Initial conditions
initial_conditions = [0.1, 0.5, 0.9]

# Prepare the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Create a grid of points for the streamlines
X, Y = np.meshgrid(np.linspace(0, 10, 100), np.linspace(0, 2, 20))
U = np.ones_like(X)
V = dx_dt(Y, X)

# Plot the streamlines
strm = ax.streamplot(X, Y, U, V, color='k', linewidth=0.5, density=1)

# Plot the trajectories for different initial conditions
lines = []
for x0 in initial_conditions:
    line, = ax.plot([], [], label=f'Starting point: {x0}')
    lines.append(line)

# Adding labels and title
ax.set_xlabel('Time t')
ax.set_ylabel('x(t)')
ax.set_title('Advanced Phase Portrait for dx/dt = x(1-x)')
ax.legend()
ax.grid(True)

# Animation function
def animate(i):
    for line, x0 in zip(lines, initial_conditions):
        x = runge_kutta(dx_dt, x0, t)
        line.set_data(t[:i], x[:i])
    return lines

# Create the animation
ani = FuncAnimation(fig, animate, frames=len(t), interval=100, blit=True)

# Save the animation as a GIF or display it
ani.save('runge_kutta_solution_with_streamlines.gif', writer='imagemagick')
plt.show()  # Display the animation in an interactive window
