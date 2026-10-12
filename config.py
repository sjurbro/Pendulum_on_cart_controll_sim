from numpy import array, pi, diag, deg2rad

params = {
    "g": 9.81,
    "m": 1.0,
    "M": 3.0,
    "L": 3.0,
}

sim_config = {
    "T": 30,
    "dt": 0.001,
    "x0": array([0.0, 0.0, deg2rad(179), 0.0])
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

swing_up_config = {
    "k": 0.09
}

hybrid_config = {
    "theta_threshold": deg2rad(15),
    "omega_threshold": deg2rad(30)
}