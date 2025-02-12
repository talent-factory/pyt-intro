#-----------------------------------------------------------------------
# universe.py
#-----------------------------------------------------------------------

import sys

import stdarray
import stddraw
from instream import InStream

from body import Body
from vector import Vector


#-----------------------------------------------------------------------

class Universe:

    # Construct a new Universe object by reading a description
    # from the file whose name is filename.

    def __init__(self, filename):
        instream = InStream(filename)
        n = instream.read_number()
        radius = instream.read_float()
        stddraw.set_xscale(-radius, +radius)
        stddraw.set_yscale(-radius, +radius)
        self._bodies = stdarray.create_1d(n)
        for i in range(n):
            rx   = instream.read_float()
            ry   = instream.read_float()
            vx   = instream.read_float()
            vy   = instream.read_float()
            mass = instream.read_float()
            r = Vector([rx, ry])
            v = Vector([vx, vy])
            self._bodies[i] = Body(r, v, mass)

    # Simulate the passing of dt seconds in self.
    
    def increaseTime(self, dt):
        
        # Initialize the forces to zero.
        n = len(self._bodies)
        f = stdarray.create_1d(n, Vector([0, 0]))
        
        # Compute the forces.
        for i in range(n):
            for j in range(n):
                if i != j:
                    bodyi = self._bodies[i]
                    bodyj = self._bodies[j]
                    f[i] = f[i] + bodyi.forceFrom(bodyj)

        # Move the bodies.
        for i in range(n):
            self._bodies[i].move(f[i], dt)    

    # Draw self to standard draw.
    def draw(self):
        for body in self._bodies:
            body.draw()

#-----------------------------------------------------------------------

# Accept a string filename and a float dt as command-line arguments.
# Simulate the motion in the universe defined by the contents of
# the file with the given filename, increasing time at the rate
# specified by dt.

def main():
    filename = sys.argv[1]
    dt = float(sys.argv[2])
    universe = Universe(filename)
    while True:
        universe.increaseTime(dt)
        stddraw.clear()
        universe.draw()
        stddraw.show(10)

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python universe.py 2bodyTiny.txt 20000

# python universe.py 2body.txt 20000

# python universe.py 3body.txt 20000

# python universe.py 4body.txt 20000

