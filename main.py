SIM = "discrete"
from numpy import diag, deg2rad

from config import (
    params,
    sim_config,
    lqr_config,
    swing_up_config,
    hybrid_config,
    sensor_config,
    kalman_config
)

from dynamics import pendulum_on_cart, linear_state_space_matrices, discrete_linear_state_space_matrices
from integrators import rk4
from simulate import simulate, simulate_discrete
from animation import animate
from plotting import plot_states, plot_control, plot_simulation, plot_measurements, plot_estimation_comparison
from sensors import Sensor
from estimators import KalmanFilter

from controllers import (
    LQRController,
    LQRController_discrete,
    SwingUpController,
    HybridController,
    zero_controller
)


# Initialize controllers
lqr = LQRController(params, lqr_config)
lqr_discrete = LQRController_discrete(params, lqr_config, sim_config)

swing_up = SwingUpController(swing_up_config)

hybrid = HybridController(
    lqr,
    swing_up,
    hybrid_config
)

# initialize sensor and estimator
sensor = Sensor(sensor_config, params, sim_config)

kalman = KalmanFilter(kalman_config, sensor_config, sim_config, params)


"""Here begins the simulation"""
if SIM == "continous":
    # Run simulation
    t, x, u = simulate(
        system=pendulum_on_cart,
        integrator=rk4,
        x0=sim_config["x0"],
        dt=sim_config["dt"],
        T=sim_config["T"],
        params=params,
        controller=hybrid
    )


    # Visualize results
    animate(x, params)

elif SIM == "discrete":
    # run discrete simulation
    t, x, x_hat, u = simulate_discrete(
        system=pendulum_on_cart,
        integrator=rk4,
        controller=lqr_discrete,
        sim_config=sim_config,
        params=params,
        kalman=kalman,
        sensor=sensor
    )

    animate(x, params)
    plot_estimation_comparison(t, x, x_hat)

'''
    from numpy import diag, deg2rad, array
    R = diag([
        0.01**2,
        deg2rad(0.5)**2
    ])

    sensor = Sensor(C, R)
    y = array([sensor.measure(xk) for xk in x])
    plot_measurements(t, x, y)
'''