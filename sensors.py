from numpy import random, zeros
from dynamics import discrete_linear_state_space_matrices

class Sensor:
    """Simulate noisy measurments of the system state."""


    def __init__(self, sensor_config, params, sim_config):
        _, _, self.C, _ = discrete_linear_state_space_matrices(params, sim_config)
        self.R = sensor_config["Rk"]
        self.rng = random.default_rng()

    def measure(self, x_true):
        noise = self.rng.multivariate_normal(
            mean=zeros(self.C.shape[0]),
            cov=self.R
        )

        return self.C @ x_true + noise
    