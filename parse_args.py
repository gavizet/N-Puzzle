import os
import sys
import argparse
from board_info import BoardInfo
import random
import npuzzlegen

def get_args():
    
    parser = argparse.ArgumentParser(description="42 N-Puzzle Algorithmic Project")

    parser.add_argument('-size', type=int, default=3,
            help='Size of the puzzle\'s side. Must be >3.')
    parser.add_argument('-i', '--iterations', type=int, default=10000,
            help="Number of passes")
    parser.add_argument('-g', '--greedy', action='store_true', 
            help='Greedy-first search')
    parser.add_argument('-u', '--uniform', action='store_true',
            help='Uniform cost search')
    parser.add_argument('-v', '--visualizer', action='store_true',
            help='Print with a visualizer')
    # TODO : Heuristics
    parser.add_argument('-hf', '--heuristics', type=int, choices=list(range(1, 4)),
            default=1, help='Choose your heuristic function : 1 -> Manhattan(default) | 2 -> Euclidian Distance | 3 -> Number of Missplaced Tiles')
    # TODO : Solver Creation
    parser.add_argument('-s', '--solution', type=int, choices=range(1, 3),
            default=1, help='Choose the desired solution state : 1 -> Snail(default) | 2 -> Line')
    parser.add_argument('-f', '--file', type=argparse.FileType('r'), help='Choose an input grid file')
    
    args = parser.parse_args()
    return args

def parse_generator(args):
        s = args.size
        if args.size < 3:
            print ("Can't generate a puzzle with size lower than 2. It says so in the help. Dummy.")
            sys.exit(1)
        info = BoardInfo(args)
        info.size = s
        solv = random.choice([True, False])
        puzzle = npuzzlegen.make_puzzle(info.size, solv,args.iterations)
        w = len(str(s*s))
        print ("# This puzzle is %s" % ("solvable" if solv else "unsolvable"))
        print ("%d" % s)
        for y in range(s):
            for x in range(s):
                print ("%s" % (str(puzzle[x + y*s]).rjust(w)),end =" ")
            print()
        for i in range(s*s):
                info.node.insert(puzzle[i])
        return info