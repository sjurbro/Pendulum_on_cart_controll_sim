# Numerical integration methods

def forward_euler(f, x_k, dt, params, u):
    """Advance the state one step using Forward Euler."""
    return x_k + dt * f(x_k, params, u)


def rk2(f, x_k, dt, params, u):
    """Advance the state one step using the midpoint RK2 method."""
    k1 = f(x_k, params, u)
    k2 = f(x_k + dt/2 * k1, params, u)

    return x_k + dt * k2


def rk4(f, x_k, dt, params, u):
    """Advance the state one step using the classical RK4 method."""
    k1 = f(x_k, params, u)
    k2 = f(x_k + dt/2 * k1, params, u)
    k3 = f(x_k + dt/2 * k2, params, u)
    k4 = f(x_k + dt * k3, params, u)

    return x_k + dt/6 * (k1 + 2*k2 + 2*k3 + k4)