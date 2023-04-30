import math
from tkinter import ttk
from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

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

vinit = 0
angleinit = 0

win_input = tk.Tk()

frm_v = tk.Frame(padx=30, pady=10)
frm_a = tk.Frame(padx=30, pady=10)
frm_btn = tk.Frame(padx=30, pady= 10)
lbl_v = tk.Label(master = frm_v, font=15, text="Enter the initial velocity (m/s): ")
lbl_a = tk.Label(master = frm_a, font=15, text="Enter the angle of projection (deg): ")
ent_v = tk.Entry(master = frm_v, font=15, borderwidth=2)
ent_a = tk.Entry(master = frm_a, font=15, borderwidth=2)
btn_calc = tk.Button(font = 15, master = frm_btn, text="Calculate Trajectory", pady=5, padx=10)

frm_v.pack()
lbl_v.pack()
ent_v.pack()
frm_a.pack()
lbl_a.pack()
ent_a.pack()
frm_btn.pack()
btn_calc.pack()

def traj_calc(event):
    global vinit, angleinit
    vinit = float(ent_v.get())
    angleinit = float(ent_a.get())
    lbl_ft = tk.Label(text="Flight time (s): " + str(tflight(angleinit, vinit, g)))
    lbl_mh = tk.Label(text="Maximum height (m): " + str(hmax(angleinit, vinit, g)))
    lbl_hr = tk.Label(text="Horizontal range (m): " + str(hrange(angleinit, vinit, g)))
    lbl_mpr = tk.Label(text="Maximum possible range (m): " + str(rangemax(vinit, g)))
    ttk.Separator(orient=HORIZONTAL, style='TSeparator', class_= ttk.Separator, takefocus= 1, cursor='plus').pack(fill=X, padx=10, expand=True)
    lbl_ft.pack()
    lbl_mh.pack()
    lbl_hr.pack()
    lbl_mpr.pack()
    
    plot_trajectory(angleinit, vinit, g)

btn_calc.bind("<Button-1>", traj_calc)

win_input.mainloop()