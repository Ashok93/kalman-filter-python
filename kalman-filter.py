import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

from state_evolution import next_state
from simulate_senor_data import mock_odo_gps_data


if __name__ == "__main__":
    
    odometry, gps = mock_odo_gps_data()
    print(odometry)