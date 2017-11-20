
from Dynamics import Dynamics
from Main.Robot import Robot
import copy
import numpy as np


class GravityCompensationController():
    def __init__(self, k_l,k_v):
        self._prev = None
        self._K_l = k_l
        self._K_v = k_v
        pass

    def getTorque(self, robot ):

        self._prev  = copy.deepcopy(robot)
        g = Dynamics.make_gravity_matrix(robot)
        M = Dynamics.make_mass_matrix(robot)
        q = np.asarray(robot.q).reshap(3, 1)
        qd = np.asarray(robot.qd).reshap(3, 1)
        qdd = np.asarray(robot.qdd).reshap(3, 1)
        load = np.asarray(robot.tau).reshap(3, 1)

        u = self._K_l*load + g - M*( self._K_v*qd)
        return u

    def update_K_l(self, k):
        self._K_l = k


    def update_K_v(self, k):
        self._K_v = k


