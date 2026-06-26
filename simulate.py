from numpy import linspace, zeros

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

