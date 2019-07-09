import os
import sys
import argparse

def get_args():
    
    parser = argparse.ArgumentParser(description="42 N-Puzzle Algorithmic Project")

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
