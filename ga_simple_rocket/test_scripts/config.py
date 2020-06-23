MAX_TIME_INTERVALS = 200

# create commands
commands_freefall = [0] * MAX_TIME_INTERVALS
commands_fullacc = [1] * MAX_TIME_INTERVALS
commands_up_and_down = [1] * (MAX_TIME_INTERVALS//4) + [0, 0, 0] * (MAX_TIME_INTERVALS//4)