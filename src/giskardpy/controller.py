from collections import namedtuple, OrderedDict

import sympy as sp
import numpy as np

from giskardpy.qp_problem_builder import QProblemBuilder
from giskardpy.robot import Robot



class Controller(object):
    def __init__(self, robot):
        # TODO: replace
        self.robot = robot

        #TODO: fill in child class
        self._observables = []
        self.soft_constraints = OrderedDict()
        self.controllable_constraints = OrderedDict()

        self.make_constraints(robot)

        self.qp_problem_builder = QProblemBuilder(self.robot.joint_constraints,
                                                  self.robot.hard_constraints,
                                                  self.soft_constraints,
                                                  self.get_controller_observables(),
                                                  self.get_robot_observables())

    def make_constraints(self, robot):
        pass

    def set_goal(self, goal_dict):
        pass

    def update_observables(self, updates=None):
        if updates is None:
            updates = {}
        robot_updates = self.robot.update_observables()
        updates.update(robot_updates)
        return self.qp_problem_builder.update_observables(updates)

    def get_hard_expressions(self):
        return self.robot.hard_expressions

    def get_observables(self):
        return self.get_robot_observables() + self.get_controller_observables()

    def get_controller_observables(self):
        return self._observables

    def get_robot_observables(self):
        return self.robot.observables