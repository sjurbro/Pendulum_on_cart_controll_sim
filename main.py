from parameters import params, sim_config
from dynamics import penudulum_on_cart, pendulum_on_cart_control
from integrators import rk2, rk4, forwardEuler
from simulate import simulate
from animation import animate
from plotting import plot_easy
from controllers import zero_controller, angle_controller


t, x, u = simulate(system=pendulum_on_cart_control,
                integrator=rk4,
                x0=sim_config["x0"],
                dt=sim_config["dt"],
                T=sim_config["T"],
                params=params,
                controller=angle_controller
            )

animate(x, params)
#plot_easy(t, x)