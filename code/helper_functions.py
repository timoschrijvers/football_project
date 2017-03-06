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