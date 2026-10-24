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
    "Ts": 0.01,
    "x0": array([0.0, 0.0, deg2rad(40), 0.0])
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

sensor_config = {
    "Rk": diag([ # Representerer målestøy i sensorene i elementene (på diagonalen).
        0.01**2,
        deg2rad(0.5)**2
    ])
}

kalman_config = {
    "Qk": diag([ # Representerer prossestøy, altså usikkerhet i modellen og tilfeldige påvirkninger.
        0.01,  # Posisjon
        0.1,   # Vognfart
        0.001, # Vinkel
        0.1    # Vinkelhastighet (ofte støyete, og den lineariserte modellen feiler mest her)
    ]),

    "P0": diag([ # representer den initielle ussikerhets kovarians matrisen. nå er elementene lav fordi vi simulerer med x0_hat = x0.
        1e-4,  # Posisjon (p) - svært sikker
        1e-4,  # Vognfart (\dot{p}) - svært sikker (starter i ro)
        1e-4,  # Vinkel (\theta) - svært sikker (starter oppreist/nedhengende)
        1e-4   # Vinkelhastighet (\dot{\theta}) - svært sikker (starter i ro)
    ])
}