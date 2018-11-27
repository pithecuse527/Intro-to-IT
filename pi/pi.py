#
#  pi.py
#  Calculate Pi using Monte Carlo Method.
#
#  Created by Ji Hong Geun on 25/11/18.
#  Copyright © 2018 Ji Hong Geun. All rights reserved.
#

from random import *

n = int(input("Type the count : "))

inside = 0
for i in range(0,n):
    x = random()
    y = random()
    if (x**2 + y**2) <= 1:    # if the dot is in circle part, increase the 'inside' value.
        inside += 1
Pi = 4 * inside/n             # since the 'inside' value is just for one of the four parts,
                              # needs to multiply by 4.
print(Pi)
