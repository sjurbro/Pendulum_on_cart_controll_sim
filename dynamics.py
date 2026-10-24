from numpy import sin, cos, array, linalg
from scipy.signal import cont2discrete


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

    C = array([
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0]
    ])

    D = array([
        [0.0],
        [0.0]
    ])

    return A, B, C, D


def discrete_linear_state_space_matrices(params, sim_config):
    """Return the discrete state-space matrices linearized about the upright equilibrium."""

    A, B, C, D = linear_state_space_matrices(params)

    Ts = sim_config["Ts"]

    Ad, Bd, Cd, Dd, _ = cont2discrete((A, B, C, D), Ts, method='zoh')

    return Ad, Bd, Cd, Dd