import math

radius = float(input("Enter a value for radius: " ))

print("radius is: " +  str(radius))

SA = 4 * (math.pi * (radius**2))
Volume = ((4 / 3) * (math.pi * (radius**3)))

print("SurfaceArea is: " + str(SA))
print("Volume is: " + str(Volume))

