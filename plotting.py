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

def plot_measurements(t, x_true, y):
    """Compare noisy sensor measurements with true states."""

    fig, axes = plt.subplots(2, 1, figsize=(11, 7), sharex=True)

    # Cart position
    axes[0].plot(t, x_true[:, 0], label="True position")
    axes[0].plot(t, y[:, 0], ".", markersize=2,
                 alpha=0.4, label="Measured position")

    axes[0].set_ylabel("Position [m]")
    axes[0].legend()
    axes[0].grid(True)

    # Pendulum angle
    axes[1].plot(t, np.rad2deg(x_true[:, 2]),
                 label="True angle")

    axes[1].plot(t, np.rad2deg(y[:, 1]), ".",
                 markersize=2, alpha=0.4,
                 label="Measured angle")

    axes[1].set_ylabel("Angle [deg]")
    axes[1].set_xlabel("Time [s]")
    axes[1].legend()
    axes[1].grid(True)

    plt.tight_layout()
    plt.show()

import matplotlib.pyplot as plt

def plot_estimation_comparison(t, x, x_hat):
    fig, axes = plt.subplots(4, 1, figsize=(10, 10), sharex=True)
    
    labels = ["Posisjon (p)", "Vognhastighet (v)", "Vinkel (theta)", "Vinkelhastighet (omega)"]
    
    for i in range(4):
        axes[i].plot(t, x[:, i], label='Sann verdi (x)', color='black', alpha=0.7)
        axes[i].plot(t, x_hat[:, i], label='Kalman-estimat (x_hat)', color='red', linestyle='--', alpha=0.9)
        axes[i].set_ylabel(labels[i])
        axes[i].legend(loc='upper right')
        axes[i].grid(True)
        
    axes[-1].set_xlabel('Tid [s]')
    plt.suptitle('Sammenligning av sann tilstand vs. Kalman-filter estimat')
    plt.tight_layout()
    plt.show()