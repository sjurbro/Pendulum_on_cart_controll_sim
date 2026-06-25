from numpy import array, pi

params = {
    "g": 9.81,
    "m": 1.0,
    "M": 3.0,
    "L": 3.0,
}

sim_config = {
    "T": 50,
    "dt": 0.2,
    "x0": array([0.0, 0.0, 0.1, 0.0])
}

u = 0