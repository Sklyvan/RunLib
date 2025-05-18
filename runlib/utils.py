def semicirclesToDegrees(semicircles: int) -> float:
    """
    Convert semicircles to degrees. The semicircle is a unit of angular measurement that is equal to 180 degrees.
    The semicircle is used in some applications, such as in the field of astronomy and navigation.
    :param semicircles: The number of semicircles to convert to degrees.
    :return: The equivalent angle in degrees.
    """
    return semicircles * (180 / 2**31)


def degreesToSemicircles(degrees: float) -> int:
    """
    Convert degrees to semicircles. The semicircle is a unit of angular measurement that is equal to 180 degrees.
    The semicircle is used in some applications, such as in the field of astronomy and navigation.
    :param degrees: The number of degrees to convert to semicircles.
    :return: The equivalent angle in semicircles.
    """
    return int(degrees * (2**31 / 180))
