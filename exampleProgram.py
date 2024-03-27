from src.ndnGeometryCalc import geoCalc

#Calculating for sphere with radius 5
sphereV, sphereSA = geoCalc.sphere(5)
print("A sphere with radius 5 has volume", sphereV, "and surface area", sphereSA)

#Calculating for cylinder with radius 4, height 6
cylinderV, cylinderSA = geoCalc.cylinder(4,6)
print("A cylinder with radius 5 and height 6 has volume", cylinderV, "and surface area ", cylinderSA)

#Calculating for rectangular prism with length 6, width 5, height 7
rpV, rpSA = geoCalc.rectangularPrism(6,5,7)
print("A rectangular prism with length 6, width 5, height 7, has volume", rpV, "and surface area ", rpSA)

#Calculating for cone with radius 4, height 7
coneV, coneSA = geoCalc.cone(4,7)
print("A cone with radius 4 and height 7 has volume", coneV, "and surface area", coneSA)

