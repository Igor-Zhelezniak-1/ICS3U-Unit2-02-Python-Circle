#!/usr/bin/env python3

# Created by: Igor
# Created on: Sept 2021
# This is math program

import math


def main():
    # This is math program
    # input
    radius = int(input("If a circle has radius (mm): "))
    # process
    print("Area = {}".format(math.pi * (radius ** 2)))
    print("diameter = {}".format(2 * radius))
    print("Done")


if __name__ == "__main__":
    main()
