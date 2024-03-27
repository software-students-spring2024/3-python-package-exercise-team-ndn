import math

def sphere(radius):
    volume = 4 * math.pi * (radius**3) / 3
    surfaceArea = 4 * math.pi * (radius**2)
    return volume, surfaceArea

