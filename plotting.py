import matplotlib.pyplot as plt
import numpy as np


def plot_states(t, x):
    """Plot the four states of the cart-pendulum system."""

    labels = [
        "Cart position [m]",
        "Cart velocity [m/s]",
        "Pendulum angle [deg]",
        "Angular velocity [deg/s]"
    ]

    x_plot = x.copy()
    x_plot[:, 2:4] = np.rad2deg(x_plot[:, 2:4])

    fig, axes = plt.subplots(4, 1, figsize=(10, 9), sharex=True)

    for i, ax in enumerate(axes):
        ax.plot(t, x_plot[:, i])
        ax.set_ylabel(labels[i])
        ax.grid(True)

    axes[-1].set_xlabel("Time [s]")

    fig.suptitle("Cart-Pendulum States")
    plt.tight_layout()
    plt.show()

def plot_control(t, u_history, t_window=None):
    """Plot control force using a zero-order hold representation."""

    fig, ax = plt.subplots(figsize=(10, 4))

    ax.step(t, u_history, where="post")

    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Control force [N]")
    ax.set_title("Control Input (ZOH)")
    ax.grid(True)

    if t_window is not None:
        ax.set_xlim(t_window)

    plt.tight_layout()
    plt.show()

def plot_simulation(t, x, u_history):
    """Plot system states and control input."""

    labels = [
        "Position [m]",
        "Velocity [m/s]",
        "Angle [deg]",
        "Angular velocity [deg/s]"
    ]

    x_plot = x.copy()
    x_plot[:, 2:4] = np.rad2deg(x_plot[:, 2:4])

    fig, axes = plt.subplots(5, 1, figsize=(11, 11), sharex=True)

    for i in range(4):
        axes[i].plot(t, x_plot[:, i])
        axes[i].set_ylabel(labels[i])
        axes[i].grid(True)

    axes[4].step(t, u_history, where="post")
    axes[4].set_ylabel("Force [N]")
    axes[4].set_xlabel("Time [s]")
    axes[4].grid(True)

    fig.suptitle("Cart-Pendulum Simulation")

    plt.tight_layout()
    plt.show()