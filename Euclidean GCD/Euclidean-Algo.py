#
#  Euclidean-Algo.py
#  An efficient algorithm for finding the greatest common divisor of two integers.
#
#  Created by Ji Hong Guen on 29/10/18.
#  Copyright © 2018 Ji Hong Guen. All rights reserved.
#
import sys

class Number:                   ## The reson why I use Number class is described on the report.
    def __init__(self, x):      ## In short, Python 3 does not support things like pointer.
        self.num = x


def euclideanGCD(x, y):              ## Get a value of two value's Greatest Common Divisor.

    if x.num < y.num:       ## For a convenience, if y is bigger, exchange them.
        swap(x, y)

    if not y.num:         ## The basis level of this recursion.
        return x.num

    tmp = Number(x.num % y.num)

    return euclideanGCD(y, tmp)             ## Do this recursively.


def swap(x, y):         ## This function exchanges original's value.
    tmp = x.num
    x.num = y.num
    y.num = tmp


def main():
    x = Number(int(input("Type the First Number : ")))
    y = Number(int(input("Type the Second Number : ")))
    print("The GCD : " + str(euclideanGCD(x, y)))

main()
