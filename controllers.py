def zero_controller(t, x, params):
    return 0.0

def angle_controller(t, x, params):
    theta = x[2]
    omega = x[3]

    theta_ref = 0.0

    Kp = 50.0
    Kd = 5.0

    error = theta - theta_ref

    u = -(Kp * error + Kd * omega)

    return u
