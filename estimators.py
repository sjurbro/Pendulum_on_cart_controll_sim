from numpy import linalg, eye, atleast_1d
from dynamics import discrete_linear_state_space_matrices

class KalmanFilter:
    ''''''

    def __init__(self, kalman_config, sensor_config, sim_config, params):

        Ts = sim_config["Ts"]
        self.Ad, self.Bd, self.C, _ = discrete_linear_state_space_matrices(params, sim_config)

        self.Q = kalman_config["Qk"]
        self.R = sensor_config["Rk"]
        self.x_hat = sim_config["x0"].copy()
        self.P = kalman_config["P0"].copy()
        self.I = eye(len(sim_config["x0"]))


    def predict(self, u):
        # Sørg for at u minst er et 1D-array (eller 2D kolonnevektor) slik at matrisemultiplikasjon ikke krasjer
        u = atleast_1d(u)
        
        # 1. Prediker tilstand: x_k|k-1 = Ad * x + Bd * u
        self.x_hat = self.Ad @ self.x_hat + self.Bd @ u
        
        # 2. Prediker feil-kovarians: P_k|k-1 = Ad * P * Ad^T + Q
        self.P = self.Ad @ self.P @ self.Ad.T + self.Q

    def update(self, y):
        residual = y - self.C @ self.x_hat
        S = self.C @ self.P @ self.C.T + self.R
        K = self.P @ self.C.T @ linalg.inv(S)
        self.x_hat = self.x_hat + K @ residual

        self.P = (self.I - K @ self.C) @ self.P

        return self.x_hat