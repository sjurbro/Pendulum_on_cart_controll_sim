import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
from numpy import sin, cos


def animate(x, params, frame_step=30):
    fig, ax = plt.subplots()
    ax.set_xlim(-15, 15)
    ax.set_ylim(-5, 5)
    ax.grid(True)
    ax.set_aspect('equal', adjustable='box')

    cart_width = 0.8
    cart_height = 0.4
    mass_radius = 0.2
    L = params["L"]

    cart = patches.Rectangle((0, 0), cart_width, cart_height, fc='blue')
    mass = patches.Circle((0, 0), mass_radius, fc='red')
    rod, = ax.plot([], [], lw=2, color='black')

    def init():
        ax.add_patch(cart)
        ax.add_patch(mass)
        ax.add_line(rod)
        return cart, mass, rod

    def animate_frame(i):
        x_cart = x[i, 0]
        theta = x[i, 2]

        # Cart lower-left corner
        cart.set_xy((x_cart, 0))

        # Pivot at top center of cart
        x_pivot = x_cart + cart_width / 2
        y_pivot = cart_height

        # Pendulum mass position
        x_mass = x_pivot - L * sin(theta)
        y_mass = y_pivot + L * cos(theta)

        mass.set_center((x_mass, y_mass))
        rod.set_data(
            [x_pivot, x_mass],
            [y_pivot, y_mass]
        )

        return cart, mass, rod

    ani = animation.FuncAnimation(
        fig,
        animate_frame,
        init_func=init,
        frames=range(0, len(x), frame_step),
        interval=20,
        blit=True
    )

    plt.show()