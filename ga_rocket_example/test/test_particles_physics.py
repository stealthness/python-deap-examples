"""

Purpose of this file is to structure some test to check

"""
import numpy as np

TIME_RATE = 1000
REFRESH_RATE = 1/TIME_RATE


def calculate_motion(pos, vel, acc, time):
    acceleration = acc
    velocity = vel
    position = pos
    for t in range(time * TIME_RATE):
        velocity += acceleration * REFRESH_RATE
        position += velocity * REFRESH_RATE
        if t+1 % 10 == 0 or t == 0:
            print(f't: {t}  -- pos:{position}  --  vel:{velocity}  -- acc:{acceleration}')

    return position, velocity, acceleration


def test_motion(exp_pos, exp_vel, exp_acc, init_pos, init_vel, init_acc, time):
    new_pos, new_vel, new_acc = calculate_motion(init_pos, init_vel, init_acc, time)
    np.testing.assert_allclose(new_pos, exp_pos, err_msg='pos', rtol=0.01, atol=0.01)
    np.testing.assert_allclose(new_vel, exp_vel, err_msg='vel', rtol=0.01, atol=0.01)
    np.testing.assert_allclose(new_acc, exp_acc, err_msg='acc', rtol=0.01, atol=0.01)


# no initial vel or acc

test_motion(np.array([0.0, 0.0]), np.array([0.0, 0.0]), np.array([0.0, 0.0]),
            np.array([0.0, .0]), np.array([0.0, 0.0]), np.array([0.0, 0.0]), 1)

test_motion(np.array([0.0, 0.0]), np.array([0.0, 0.0]), np.array([0.0, 0.0]),
            np.array([0.0, 0.0]), np.array([0.0, 0.0]), np.array([0.0, 0.0]), 3)

test_motion(np.array([10.0, 10.0]), np.array([0.0, 0.0]), np.array([0.0, 0.0]),
            np.array([10.0, 10.0]), np.array([0.0, 0.0]), np.array([0.0, 0.0]), 1)

test_motion(np.array([10.0, 10.0]), np.array([0.0, 0.0]), np.array([0.0, 0.0]),
            np.array([10.0, 10.0]), np.array([0.0, 0.0]), np.array([0.0, 0.0]), 3)

# # no initial acc, and vel = [0,10]

test_motion(np.array([0.0, 10.0]), np.array([0.0, 10.0]), np.array([0.0, 0.0]),
            np.array([0.0, 0.0]), np.array([0.0, 10.0]), np.array([0.0, 0.0]), 1)

test_motion(np.array([0.0, 30.0]), np.array([0.0, 10.0]), np.array([0.0, 0.0]),
            np.array([0.0, 0.0]), np.array([0.0, 10.0]), np.array([0.0, 0.0]), 3)

test_motion(np.array([10.0, 30.0]), np.array([0.0, 10.0]), np.array([0.0, 0.0]),
            np.array([10.0, 20.0]), np.array([0.0, 10.0]), np.array([0.0, 0.0]), 1)

test_motion(np.array([10.0, 50.0]), np.array([0.0, 10.0]), np.array([0.0, 0.0]),
            np.array([10.0, 20.0]), np.array([0.0, 10.0]), np.array([0.0, 0.0]), 3)

# no initial acc, and vel = [0,0], acc = [10]

test_motion(np.array([0.0, 5.0]), np.array([0.0, 10.0]), np.array([0.0, 10.0]),
            np.array([0.0, 0.0]), np.array([0.0, 0.0]), np.array([0.0, 10.0]), 1)

test_motion(np.array([0.0, 45.0]), np.array([0.0, 30.0]), np.array([0.0, 10.0]),
            np.array([0.0, 0.0]), np.array([0.0, 0.0]), np.array([0.0, 10.0]), 3)

test_motion(np.array([0.0, 35.0]), np.array([-10.0, 20.0]), np.array([0.0, 10.0]),
            np.array([10.0, 20.0]), np.array([-10.0, 10]), np.array([0.0, 10.0]), 1)

test_motion(np.array([-20.0, 95.0]), np.array([-10.0, 40.0]), np.array([0.0, 10.0]),
            np.array([10.0, 20.0]), np.array([-10.0, 10]), np.array([0.0, 10.0]), 3)