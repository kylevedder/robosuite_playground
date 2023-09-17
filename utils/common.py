import numpy as np
from robosuite.models.grippers import GRIPPER_MAPPING


def register_gripper(gripper_class):
    """
    Register @gripper_class in GRIPPER_MAPPING.

    Args:
        gripper_class (GripperModel): Gripper class which should be registered
    """
    GRIPPER_MAPPING[gripper_class.__name__] = gripper_class
