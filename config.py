from numpy import array, pi, diag, deg2rad

params = {
    "g": 9.81,
    "m": 1.0,
    "M": 3.0,
    "L": 3.0,
}

sim_config = {
    "T": 50,
    "dt": 0.05,
    "x0": array([0.0, 0.0, deg2rad(25), 0.0])
}

lqr_config = {
    "Q": diag([
        1.0,    # cart position
        1.0,    # cart velocity
        100.0,  # pendulum angle
        10.0    # angular velocity
    ]),

    "R": array([[1.0]])
}