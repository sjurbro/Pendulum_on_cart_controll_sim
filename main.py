from config import params, sim_config, lqr_config
from dynamics import penudulum_on_cart, pendulum_on_cart_control, linear_pendulum_on_cart
from integrators import rk2, rk4, forwardEuler
from simulate import simulate
from animation import animate
from plotting import plot_easy
from controllers import zero_controller, angle_controller, manual_state_feedback, LQRController

lqr = LQRController(params, lqr_config)

t, x, u = simulate(system=pendulum_on_cart_control,
                integrator=rk4,
                x0=sim_config["x0"],
                dt=sim_config["dt"],
                T=sim_config["T"],
                params=params,
                controller=lqr
            )

animate(x, params)
plot_easy(t, u)