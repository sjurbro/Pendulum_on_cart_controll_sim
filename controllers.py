from numpy import array, linalg, clip
from scipy.linalg import solve_continuous_are
from dynamics import linear_state_space_matrices

def zero_controller(t, x, params):
    return 0.0

def angle_controller(t, x, params):
    theta = x[2]
    omega = x[3]

    theta_ref = 0.0

    Kp = 100.0
    Kd = 5.0

    error = theta - theta_ref

    u = -(Kp * error + Kd * omega)

    return u

def manual_state_feedback(t, x, params):
    
    x_ref = 0
    theta_ref = 0

    Kx = -2
    Kv = -7
    Ktheta = 110
    Komega = 50

    u = (
        -Kx * (x[0] - x_ref)
        -Kv * x[1]
        -Ktheta * (x[2] - theta_ref)
        -Komega * x[3]
    )

    return u

class LQRController:
    def __init__(self, params, lqr_config):
        M = params["M"]
        m = params["m"]
        g = params["g"]
        L = params["L"]

        Q = lqr_config["Q"]
        R = lqr_config["R"]

        A, B = linear_state_space_matrices(params)

        P = solve_continuous_are(A, B, Q, R)
        self.K = linalg.inv(R) @ B.T @ P

    def __call__(self, t, x, params):
        u_unsaturated = -(self.K @ x).item()

        u_max = 20.0
        return clip(u_unsaturated, -u_max, u_max)