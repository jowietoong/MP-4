from math import radians
from math import cos
from math import sin
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

height = int(input('Initial height of the projectile above the ground in meters: '))
v = int(input('Magnitude of the Velocity in m/s: '))
deg = int(input('Angle in degrees with respect to the positive x-axis at which the projectile is fired: '))
xcom = eval(input('x-component of the acceleration in m/s^2: '))
ycomp = eval(input('y-component of the acceleration in m/s^2: '))
xcomp = 0 

if ycomp == 0:
    print('')
    print('Please enter a non-zero vertical acceleration component')
    ycomp = print(eval(input('y-component of the acceleration in m/s^2: ')))

rad = radians(deg)
vx = v*cos(rad)
vy = v*sin(rad)
dist = ((vy**2) - (4*(1/2*ycomp)*height))
dsqrt = sqrt(dist)
t1 = (-vy + dsqrt )/ ycomp
t2 = (-vy - dsqrt )/ ycomp

 
if t1 <= 0:
    t1 = t2
    xi = vx*(np.linspace(0,t1)) + 1/2*xcomp*np.linspace(0,t1)**2
    yi = vy*np.linspace(0,t1) + 1/2*ycomp*np.linspace(0,t1)**2
else:
    xi = vx*(np.linspace(0,t1)) + 1/2*xcomp*np.linspace(0,t1)**2
    yi = vy*np.linspace(0,t1) + 1/2*ycomp*np.linspace(0,t1)**2
        
if t1 <= 0:
        t1 = t2
        xni = vx*(np.linspace(0,t1)) + 1/2*xcom*np.linspace(0,t1)**2
        yni = vy*np.linspace(0,t1) + 1/2*ycomp*np.linspace(0,t1)**2
else:
        xni = vx*(np.linspace(0,t1)) + 1/2*xcom*np.linspace(0,t1)**2
        yni = vy*np.linspace(0,t1) + 1/2*ycomp*np.linspace(0,t1)**2
        
plt.plot(xi, yi, color = 'g', label = 'Graph of Ideal Motion')
plt.plot(xni, yni, color = 'b', label = 'Graph of Non-Ideal Motion')
plt.title('Projectile Motion')
plt.xlabel('Trajectory in the X direction')
plt.ylabel('Trajectory in the Y direction')
plt.legend()
plt.grid()
plt.show()