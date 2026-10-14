from config import (
    params,
    sim_config,
    lqr_config,
    swing_up_config,
    hybrid_config
)

from dynamics import pendulum_on_cart
from integrators import rk4
from simulate import simulate
from animation import animate
from plotting import plot_easy

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

"""
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
plot_easy(t, x)

"""
"""
for Ts in [0.1, 0.01, 0.001, 0.0001]:
    controller = LQRController_discrete(
        params,
        lqr_config,
        {"Ts": Ts}
    )
    print(f"Ts = {Ts}: Kd = {controller.K}")
print(lqr.K)
"""