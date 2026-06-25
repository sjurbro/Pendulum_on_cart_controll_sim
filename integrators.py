# solvers: lets do forward euler, RK2 first then RK4!

from numpy import linspace, zeros, shape

def forwardEuler(f, x0, dt, T, params, u):
    n_steps = int(T/dt) + 1
    t = linspace(0, T, n_steps)
    x = zeros((n_steps, len(x0)))
    x[0] = x0

    for k in range(n_steps - 1):
        x[k+1] = x[k] + dt * f(x[k], params, u)
    return t, x

def rk2(f, x0, dt, T, params, u):
    n_steps = int(T/dt) + 1
    t = linspace(0, T, n_steps)
    x = zeros((n_steps, len(x0)))
    x[0] = x0

    for k in range(n_steps - 1):
        k1 = f(x[k], params, u)
        k2 = f(x[k] + dt/2 * k1, params, u)
        x[k+1] = x[k] + dt * k2
    return t, x

def rk4(f, x0, dt, T, params, u):
    n_steps = int(T/dt) + 1
    t = linspace(0, T, n_steps)
    x = zeros((n_steps, len(x0)))
    x[0] = x0

    for k in range(n_steps - 1):
        k1 = f(x[k], params, u)
        k2 = f(x[k] + dt/2 * k1, params, u)
        k3 = f(x[k] + dt/2 * k2, params, u)
        k4 = f(x[k] + dt * k3, params, u)
        x[k+1] = x[k] + dt/6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return t, x
