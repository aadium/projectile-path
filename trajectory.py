import math
import matplotlib.pyplot as plt
import numpy as np

def pequation(angleinit, vinit, g):
    angle_rad = math.radians(angleinit)
    print(f"Path Equation: {math.tan(angle_rad)}x - {(g / 2 * (vinit * math.cos(angle_rad)) ** 2)}x^2")

def tflight(angleinit, vinit, g):
    angle_rad = math.radians(angleinit)
    return 2 * ((vinit * math.sin(angle_rad))/g)

def hmax(angleinit, vinit, g):
    angle_rad = math.radians(angleinit)
    return (vinit * math.sin(angle_rad)) ** 2 / (2 * g)

def hrange(angleinit, vinit, g):
    angle_rad = math.radians(angleinit)
    return (vinit ** 2) * math.sin(2 * angle_rad) / g

def rangemax(vinit, g):
    return vinit ** 2 / g

def plot_trajectory(angleinit, vinit, g):
    angle_rad = np.deg2rad(angleinit)
    t = np.linspace(0, tflight(angleinit, vinit, g), 100)
    x = vinit * np.cos(angle_rad) * t
    y = vinit * np.sin(angle_rad) * t - 0.5 * g * t ** 2

    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.set_xlim(0, max(x) + 5)
    ax.set_ylim(0, max(y) + 5)

    ax.set_xlabel("Horizontal distance (m)")
    ax.set_ylabel("Vertical distance (m)")
    ax.set_title("Trajectory")

    ax.grid(True, linestyle='-')

    plt.show()


g = 9.81
again = 'y'

while again == 'y' or again == 'Y':
    vinit = float(input("Enter the initial velocity (m/s): "))
    angleinit = float(input("Enter the angle of projection (degrees): "))

    print("=======================================================")
    pequation(angleinit, vinit, g)
    print("Flight time (s): ", tflight(angleinit, vinit, g))
    print("Maximum height (m): ", hmax(angleinit, vinit, g))
    print("Horizontal range (m): ", hrange(angleinit, vinit, g))
    print("Maximum possible range (m): ", rangemax(vinit, g))
    print("=======================================================")
    plot_trajectory(angleinit, vinit, g)
    again = input("Calculate another trajectory? (y/n): ")

print("Exiting program...")
