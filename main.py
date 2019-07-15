#!/usr/bin/env python3
import sys
import parse_file
import parse_args
import graphic

def main(av):
    args = parse_args.get_args()
    print(args)
    if not args.file:
        print('Have to call the generate function they give us')
        # generate_grid()
        sys.exit(0)
    else:
        info = parse_file.parse(args)
        info.print_grid(info.solutionGrid())
    if args.visualizer:
        graphic.StartGame(info)

if __name__ == '__main__':
    try:
        main(sys.argv)
    except Exception as exception:
        print("General uncaught exception : ", exception)
