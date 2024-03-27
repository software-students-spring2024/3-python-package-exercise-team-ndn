import pytest
import math
from ndnGeometryCalc import packageCode

class Tests:
    def sanity_check():
        assert True == True, "True does not equal True!"

    def test_sphere(self):
        #test 100 spheres for their volume and surfacearea
        for i in range(1,100):
            vol, surfacearea = packageCode.sphere(i)
            assert isinstance(vol, float), "expected volume to be a float"
            assert isinstance(surfacearea, float), "expected surface area to be a float"
            expectedvol = 4*(math.pi)*(i**3)/3
            expectedsurfacearea = 4*(math.pi)*(i**2)
            assert expectedvol == vol, f"expected volume to be {expectedvol}, but was {vol}"
            assert expectedsurfacearea == surfacearea, f"expected volume to be {expectedsurfacearea}, but was {surfacearea}"

    def test_rectangularprism(self):

    def test_cone(self):
    
    def test_cylinder(self):
