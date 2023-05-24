#!/usr/bin/env python3
import sys
import parse_file
import parse_args
import graphic

def main(av):
    args = parse_args.get_args()
    print(args)
    if not args.file:
        info = parse_args.parse_generator(args)
        info.print_grid(info.solutionGrid())
        print(info.countInversion())
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
