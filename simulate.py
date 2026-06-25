

def simulate(system, integrator, x0, dt, T, params, u):
    t, x = integrator(system, x0, dt, T, params, u)
    return t, x

