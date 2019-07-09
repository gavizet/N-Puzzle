#!/usr/bin/env python3
import Parse
import sys
from Graphic import *

def main(av):
	if len(av) != 2:
		print('Need 1 File')
		return
	# Parse threw file
	info = Parse.parse(av[1])
	StartGame(info)

if __name__ == '__main__':
	main(sys.argv)
