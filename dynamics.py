# her må jeg lage en funskjon... for equations of motion kinda.
from numpy import sin, cos, pi, array, linalg

def penudulum_on_cart(x, params, u):
    m = params["m"]
    M = params["M"]
    g = params["g"]
    L = params["L"]

    pos = x[0]
    vel = x[1]
    theta = x[2]
    omega = x[3]

    denom = M + m - m * cos(theta)**2

    x_dot = vel

    x_ddot = (sin(theta) / denom) * m * (L * omega**2 + g * cos(theta))

    theta_dot = omega

    theta_ddot = (sin(theta) / denom) * (-1 / L) * (g * (m + M) + m * L * cos(theta) * theta_dot**2)

    return array([x_dot, x_ddot, theta_dot, theta_ddot])

def pendulum_on_cart_control(x, params, u):
    m = params["m"]
    M = params["M"]
    g = params["g"]
    L = params["L"]

    pos = x[0]
    vel = x[1]
    theta = x[2]
    omega = x[3]

    A = array([
        [m + M, -m * L * cos(theta)],
        [-cos(theta), L]
    ])

    b = array([
        u - m * L * omega**2 * sin(theta),
        g * sin(theta)
    ])

    q_ddot = linalg.solve(A,b)

    x_ddot = q_ddot[0]
    theta_ddot = q_ddot[1]

    x_dot = array([
        vel,
        x_ddot,
        omega,
        theta_ddot
    ])

    return x_dot

def linear_pendulum_on_cart(x, params, u):
    m = params["m"]
    M = params["M"]
    g = params["g"]
    L = params["L"]

    A = array([
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, m * g / M, 0.0],
        [0.0, 0.0, 0.0, 1.0],
        [0.0, 0.0, (m + M) * g / (M * L), 0.0]
    ])

    B = array([
        0.0,
        1 / M,
        0.0,
        1 / (M * L)
    ])

    x_dot = A @ x + B * u

    return x_dot

def linear_state_space_matrices(params):
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