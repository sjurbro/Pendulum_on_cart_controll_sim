from numpy import array, linalg, clip, cos, sin, deg2rad
from scipy.linalg import solve_continuous_are, solve_discrete_are
from dynamics import linear_state_space_matrices, discrete_linear_state_space_matrices

def zero_controller(t, x, params):
    """Apply zero control input."""
    return 0.0


class LQRController:
    """State-feedback controller based on continuous-time LQR."""

    def __init__(self, params, lqr_config):
        Q = lqr_config["Q"]
        R = lqr_config["R"]

        A, B, _, _ = linear_state_space_matrices(params)

        P = solve_continuous_are(A, B, Q, R)
        self.K = linalg.solve(R, B.T @ P)

    def __call__(self, t, x, params):
        u_unsaturated = -(self.K @ x).item()

        return u_unsaturated

class LQRController_discrete:
    """State-feedback controller based on discrete-time LQR."""

    def __init__(self, params, lqr_config, sim_config):
        Q = lqr_config["Q"]
        R = lqr_config["R"]
        Ts = sim_config["Ts"]


        Ad, Bd, Cd, Dd = discrete_linear_state_space_matrices(params, Ts)

        P = solve_discrete_are(Ad, Bd, Q, R)

        self.K = linalg.solve(
            R + Bd.T @ P @ Bd,
            Bd.T @ P @ Ad
        )

    def __call__(self, t, x, params):
        u = - (self.K @ x).item()
        return u



        


class SwingUpController:
    """Energy-based swing-up controller."""

    def __init__(self, swing_up_config):
        self.k = swing_up_config["k"]

    def __call__(self, t, x, params):
        pendulum_mass = params["m"]
        cart_mass = params["M"]
        g = params["g"]
        L = params["L"]

        theta = x[2]
        omega = x[3]

        E = pendulum_mass * g * L * cos(theta) + 0.5 * pendulum_mass * L**2 * omega**2
        E_desired = pendulum_mass * g * L

        E_error = E_desired - E

        x_ddot = self.k * omega * cos(theta) * E_error

        u = (
            x_ddot * (pendulum_mass * (1 - cos(theta)**2) + cart_mass)
            + pendulum_mass * L * omega**2 * sin(theta)
            - pendulum_mass * g * cos(theta) * sin(theta)
        )

        return u



class HybridController:
    """Switch between energy-based swing-up and LQR stabilization."""
    def __init__(self, lqr, swing_up, hybrid_config):
        self.lqr = lqr
        self.swing_up = swing_up

        self.theta_threshold = hybrid_config["theta_threshold"]
        self.omega_threshold = hybrid_config["omega_threshold"]

    def __call__(self, t, x, params):
        theta = x[2]
        omega = x[3]

        if (
            abs(theta) < self.theta_threshold
            and abs(omega) < self.omega_threshold
        ):
            return self.lqr(t, x, params)

        return self.swing_up(t, x, params)