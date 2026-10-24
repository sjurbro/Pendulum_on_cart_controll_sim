from numpy import linspace, zeros, isclose, diag, deg2rad
from dynamics import discrete_linear_state_space_matrices

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


def simulate_discrete(system, integrator, controller, sim_config, params, sensor, kalman):
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
    x_hat = zeros((n_steps, len(x0)))
    u_history = zeros(n_steps)
    x[0] = x0
    x_hat[0] = x0


    u = 0.0

    for k in range(n_steps - 1):

        if k % control_interval == 0:
            # Beregn ny kontrollinput u basert på forrige estimat
            u = controller(t[k], x_hat[k], params)
            
            # Ta måling
            y = sensor.measure(x[k])        
            
            # Kalman-filteret tar ett helt T_s-steg (predict + update)
            kalman.predict(u)               
            x_hat[k+1] = kalman.update(y)   
        else:
            # Mellom T_s-intervallene beholder vi bare forrige estimat 
            # (eller lar x_hat flate ut til neste måling kommer)
            x_hat[k+1] = x_hat[k]
            

        u_history[k] = u

        x[k+1] = integrator(
            system,
            x[k],
            dt,
            params,
            u
        )

    u_history[-1] = u

    return t, x, x_hat, u_history


    