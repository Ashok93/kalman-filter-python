import numpy as np
from state_evolution import next_state

def mock_odo_gps_data():
    state = np.array([0,0,0.0002])
    ip = np.array([1,0.01])
    odo = []
    gps = []

    for i in range(100):
        state = next_state(state, ip) # state update
        odo.append(state + np.random.normal(0, 0.1, 3)) # odo estimate is bad
        gps.append(state + np.random.normal(0, 0.001, 3)) # gps estimate is much better

    return odo, gps