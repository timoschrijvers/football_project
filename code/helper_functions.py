# author: Hendrik Werner s4549775

import numpy as np
from typing import Optional


def normalize(
        vector: np.ndarray,
) -> np.ndarray:
    """
    :param vector: A vector
    :return: The normalized vector
    """
    return vector / np.linalg.norm(vector)


def angle(
        v1: np.ndarray,
        v2: np.ndarray,
) -> float:
    """
    :param v1: One vector
    :param v2: Another vector
    :return: Angle between the two vectors
    """
    v1 = normalize(v1)
    v2 = normalize(v2)
    return np.arccos(np.clip(np.dot(v1, v2), a_min=-1, a_max=1))


def as_deg(
        angle_rad: float,
) -> float:
    """
    :param angle_rad: An angle in radians
    :return: The angle in degrees
    """
    return angle_rad * 180 / np.pi


def as_rad(
        angle_deg: float,
) -> float:
    """
    :param angle_deg: An angle in degrees
    :return: The angle in radians
    """
    return angle_deg * np.pi / 180


def intersection(
        l1: np.ndarray,
        l2: np.ndarray,
) -> Optional[np.ndarray]:
    """
    Find the intersection of two lines if it exists. Lines are specified as
    pairs of points: [[x1, y1], [x2, y2]].

    This function was inspired by
    http://stackoverflow.com/a/7448287/4637060.

    :param l1: The first line
    :param l2: The second line
    :return: The intersection if it exists
    """
    l1 = l1.reshape((2, 2))
    l2 = l2.reshape((2, 2))

    x = l2[0] - l1[0]
    d1 = l1[1] - l1[0]
    d2 = l2[1] - l2[0]
    cross = np.cross(d1, d2)

    if abs(cross) < 1e-8:
        return

    t1 = (x[0] * d2[1] - x[1] * d2[0]) / cross
    return l1[0] + d1 * t1


def smaller_angle(
        v1: np.ndarray,
        v2: np.ndarray,
        min_angle: int = 10,
) -> float:
    """
    Find the smaller angle between two vectors that is at least min_angle.

    :param v1: First vector
    :param v2: Second vector
    :param min_angle: Minimum angle (in deg) that is kept. Angles below
                      that will be discarded.
    :return: Minimum angle between v1 and v2 that is at least min_angle
    """
    min_angle = as_rad(min_angle)
    angles = [angle(v1, v2)]
    angles.append(np.pi - angles[0])
    filter(lambda a: a >= min_angle, angles)
    return min(angles)
