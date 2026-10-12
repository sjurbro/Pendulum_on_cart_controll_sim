from numpy import sin, cos, array, linalg


def pendulum_on_cart(x, params, u):
    """Nonlinear dynamics of the cart-pendulum system."""

    m = params["m"]
    M = params["M"]
    g = params["g"]
    L = params["L"]

    _, velocity, theta, omega = x

    A = array([
        [M + m, -m * L * cos(theta)],
        [-cos(theta), L],
    ])

    b = array([
        u - m * L * omega**2 * sin(theta),
        g * sin(theta),
    ])

    x_ddot, theta_ddot = linalg.solve(A, b)

    return array([
        velocity,
        x_ddot,
        omega,
        theta_ddot,
    ])


def linear_state_space_matrices(params):
    """Return the state-space matrices linearized about the upright equilibrium."""

    m = params["m"]
    M = params["M"]
    g = params["g"]
    L = params["L"]

    A = array([
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, m * g / M, 0.0],
        [0.0, 0.0, 0.0, 1.0],
        [0.0, 0.0, (m + M) * g / (M * L), 0.0],
    ])

    B = array([
        [0.0],
        [1.0 / M],
        [0.0],
        [1.0 / (M * L)],
    ])

    return A, B