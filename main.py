#!/usr/bin/env python3
import sys
import parse_file
import parse_args
import graphic
import npuzzlegen
import random

def main(av):
    args = parse_args.get_args()
    print(args)
    if not args.file:
        s = args.size
        if args.size < 3:
            print ("Can't generate a puzzle with size lower than 2. It says so in the help. Dummy.")
            sys.exit(1)
        solv = random.choice([True, False])
        puzzle = npuzzlegen.make_puzzle(s, solv,args.iterations)
        w = len(str(s*s))
        print ("# This puzzle is %s" % ("solvable" if solv else "unsolvable"))
        print ("%d" % s)
        for y in range(s):
            for x in range(s):
                print ("%s" % (str(puzzle[x + y*s]).rjust(w)),end =" ")
            print()
        sys.exit(0)
    else:
        info = parse_file.parse(args)
        info.print_grid(info.solutionGrid())
        print(info.countInversion())
    if args.visualizer:
        graphic.StartGame(info)

if __name__ == '__main__':
    try:
        main(sys.argv)
    except Exception as exception:
        print("General uncaught exception : ", exception)
