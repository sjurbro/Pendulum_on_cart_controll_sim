from numpy import array, diag, linalg
from scipy.linalg import solve_continuous_are
from config import params, lqr_config
from dynamics import linear_state_space_matrices

M = params["M"]
m = params["m"]
g = params["g"]
L = params["L"]

A, B = linear_state_space_matrices(params)

Q = lqr_config["Q"]

R = lqr_config["R"]

# Solve continuous-time riccati equation
P = solve_continuous_are(A, B, Q, R)

# Compute state-feedback gain
K = linalg.inv(R) @ B.T @ P

print("K =", K)
print("Closed-loop eigenvalues =", linalg.eigvals(A - B @ K))
