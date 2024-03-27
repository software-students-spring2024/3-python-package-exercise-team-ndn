import pytest
import math
from src.ndnGeometryCalc import geoCalc

class Tests:
    def sanity_check():
        assert True == True, "True does not equal True!"

    def test_sphere_ret_type(self):
        #test 100 spheres for their volume and surfacearea
        for i in range(1,100):
            vol, surfacearea = geoCalc.sphere(i)
            assert isinstance(vol, float), "expected volume to be a float"
            assert isinstance(surfacearea, float), "expected surface area to be a float"
            

    def test_sphere_ret_value(self):
        for i in range(1, 100):
            vol, surfacearea = geoCalc.sphere(i)
            expectedvol = 4*(math.pi)*(i**3)/3
            expectedsurfacearea = 4*(math.pi)*(i**2)
            assert expectedvol == vol, f"expected volume to be {expectedvol}, but was {vol}"
            assert expectedsurfacearea == surfacearea, f"expected volume to be {expectedsurfacearea}, but was {surfacearea}"
    def test_sphere_ret_sign(self):
        for i in range(1, 100):
            vol, surfacearea = geoCalc.sphere(i)
            assert vol > 0, "Expected volume to be positive"
            assert surfacearea > 0, "Expected surface area to be positive"
        
    
    def test_rectangular_prism_ret_type(self):
        #test 100 rectangular prisms for their volume and surfacearea
        for i in range(1,100):
            vol, surfacearea = geoCalc.rectangularPrism(i, i, i)
            assert isinstance(vol, float) | isinstance(vol, int), "expected volume to be a float or int"
            assert isinstance(surfacearea, float) | isinstance(vol, int), "expected surface area to be a float or int"
            

    def test_rectangular_prism_ret_value(self):
        for i in range(1, 100):
            #using width, height, and length as i
            vol, surfacearea = geoCalc.rectangularPrism(i, i, i)
            expectedvol = i * i * i
            expectedsurfacearea = 2* ((i*i)+(i*i)+(i*i))
            assert expectedvol == vol, f"expected volume to be {expectedvol}, but was {vol}"
            assert expectedsurfacearea == surfacearea, f"expected volume to be {expectedsurfacearea}, but was {surfacearea}"
    def test_rectangular_prism_ret_sign(self):
        for i in range(1, 100):
            vol, surfacearea = geoCalc.rectangularPrism(i,i, i)
            assert vol > 0, "Expected volume to be positive"
            assert surfacearea > 0, "Expected surface area to be positive"
    

    def test_cylinder_ret_type(self):
        #test 100 cylinders for their volume and surfacearea
        #use all cylinders with height 5
        for i in range(1,100):
            vol, surfacearea = geoCalc.cylinder(i, 5)
            assert isinstance(vol, float), "expected volume to be a float"
            assert isinstance(surfacearea, float), "expected surface area to be a float"
            

    def test_cylinder_ret_value(self):
        for i in range(1, 100):
            vol, surfacearea = geoCalc.cylinder(i, 5)
            expectedvol = math.pi*(i**2)*5
            expectedsurfacearea = (2*math.pi*i)*(5+i)
            assert expectedvol == vol, f"expected volume to be {expectedvol}, but was {vol}"
            assert expectedsurfacearea == surfacearea, f"expected volume to be {expectedsurfacearea}, but was {surfacearea}"
    
    def test_cylinder_ret_sign(self):
        for i in range(1, 100):
            vol, surfacearea = geoCalc.cylinder(i,5)
            assert vol > 0, "Expected volume to be positive"
            assert surfacearea > 0, "Expected surface area to be positive"
    

    def test_cone_ret_type(self):
        #test 100 cones for their volume and surfacearea
        #use all cones with height 5
        for i in range(1,100):
            vol, surfacearea = geoCalc.cone(i,5)
            assert isinstance(vol, float), "expected volume to be a float"
            assert isinstance(surfacearea, float), "expected surface area to be a float"
            

    def test_cone_ret_value(self):
        for i in range(1, 100):
            vol, surfacearea = geoCalc.cone(i,5)
            expectedvol = math.pi*(i**2)*5/3
            expectedsurfacearea = math.pi*i*(i+math.sqrt((5**2)+(i**2)))
            assert expectedvol == vol, f"expected volume to be {expectedvol}, but was {vol}"
            assert expectedsurfacearea == surfacearea, f"expected volume to be {expectedsurfacearea}, but was {surfacearea}"
    def test_cone_ret_sign(self):
        for i in range(1, 100):
            vol, surfacearea = geoCalc.cone(i,5)
            assert vol > 0, "Expected volume to be positive"
            assert surfacearea > 0, "Expected surface area to be positive"
    