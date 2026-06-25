from parameters import params, sim_config, u
from dynamics import penudulum_on_cart, pendulum_on_cart_control
from integrators import rk2, rk4, forwardEuler
from simulate import simulate
from animation import animate
from plotting import plot_easy


t, x = simulate(system=pendulum_on_cart_control,
                integrator=rk4,
                x0=sim_config["x0"],
                dt=sim_config["dt"],
                T=sim_config["T"],
                params=params,
                u=0
            )

animate(x, params)
#plot_easy(t, x)