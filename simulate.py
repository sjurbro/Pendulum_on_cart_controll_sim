from numpy import linspace, zeros, isclose

def simulate(system, integrator, controller, x0, dt, T, params):
    n_steps = int(T/dt) + 1
    t = linspace(0, T, n_steps)
    x = zeros((n_steps, len(x0)))
    u_history = zeros(n_steps)
    x[0] = x0

    for k in range(n_steps - 1):

        u = controller(t[k], x[k], params)
        u_history[k] = u

        x[k+1] = integrator(
            system,
            x[k],
            dt,
            params,
            u
        )

    return t, x, u_history


def simulate_discrete(system, integrator, controller, sim_config, params):
    T = sim_config["T"]
    x0 = sim_config["x0"]
    dt = sim_config["dt"]
    Ts = sim_config["Ts"]

    control_interval = int(round(Ts / dt))
    n_intervals = int(round(T / dt))

    if dt <= 0 or Ts <= 0 or T <= 0:
        raise ValueError("T, dt and Ts must be positive")

    if not isclose(T, n_intervals * dt, rtol=1e-9, atol=1e-12):
        raise ValueError("T must be an integer multiple of dt")

    if control_interval < 1 or not isclose(Ts, control_interval * dt, rtol=1e-9, atol=1e-12):
        raise ValueError("Ts must be an integer multiple of dt")

    n_steps = n_intervals + 1
    t = linspace(0, T, n_steps)

    x = zeros((n_steps, len(x0)))
    u_history = zeros(n_steps)
    x[0] = x0

    u = 0.0

    for k in range(n_steps - 1):
        if k % control_interval == 0:
            u = controller(t[k], x[k], params)

        u_history[k] = u

        x[k+1] = integrator(
            system,
            x[k],
            dt,
            params,
            u
        )

    u_history[-1] = u

    return t, x, u_history
    