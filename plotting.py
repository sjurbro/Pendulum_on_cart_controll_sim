import matplotlib.pyplot as plt

def plot_easy(t, x):
    plt.plot(t,x, label = ["x", "x_dot", "theta", "theta_dot"], linestyle = "--")

    plt.legend()
    plt.grid()
    plt.show()


