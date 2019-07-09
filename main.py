#!/usr/bin/env python3
import sys
import parse_file
import graphic

def main(av):
	if len(av) != 2:
		print('Need 1 File')
		return
	# Parse threw file
	info = parse_file.parse(av[1])
	graphic.StartGame(info)

if __name__ == '__main__':
    try:
        main(sys.argv)
    except Exception as exception:
        print("General uncaught exception : ", exception)

