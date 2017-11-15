from Dynamics import Dynamics
from Main.Robot import Robot


# This class
class HapticController(object):
    def __init__(self):
        pass


# Here is some sample code to get the mass matrix
# Dyanamics
r = Robot()
M = Dynamics.make_mass_matrix(r)
print M