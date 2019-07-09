from tkinter import *
from random import randint as ri
from copy import copy

import Tile


class Map:
	def __init__(self, parent, info):

		self.root = parent
		self.width = 100 * info.size
		self.size = info.size
		self.info = info
		# Array where all the Tiles are saved
		self.table = [0] * self.size**2
		self.emptyCell = 0,0
		# Boolean to control user inputs to avoid too many clicks
		self._canclick = True
		# Score
		self._score = 0

		# Draws all the tkinter elements
		self.main_canvas = Canvas(self.root, width=self.width, height=self.width, bg="lightblue")
		self.main_canvas.pack()
		self.second_frame = Frame(self.root)
		self.second_frame.pack()
		self._scorevar = StringVar()
		self._scorevar.set(self._score)
		self._sframesetup()

		# Draws the horizontal and vertical lines
		self._griddraw()

		# Draws the Tiles
		self._Tilesetup(info)

	def callback(self, direction):
		""" Handles the user input direction: LEFT, RIGHT, DOWN, UP = 0, 1, 2, 3"""
		if self._canclick:
			self._canclick = False  # Blocks the user input

			# Makes a copy of the table to check later if something changed or not
			backup = copy(self.table)

			d = dict(enumerate([self._left, self._right, self._down, self._up]))
			d[direction]()  # Calls the right movement function

			self._canclick = True

	def restart(self):
		""" Restart button callback """

		# deletes lose text
		self.main_canvas.delete("all")

		# deletes all Tiles
		self.table = [0] * (self.size * self.size)

		self._Tilesetup(self.info)
		self._scorevar.set(0)

	def _sframesetup(self):
		pointframe = Frame(self.second_frame)
		pointframe.pack(side=LEFT, pady=20, padx=20)

		Label(pointframe, text="Moves:").pack(side=LEFT)
		Label(pointframe, textvariable=self._scorevar).pack(side=LEFT)

		restartb = Button(self.second_frame, text="Restart", command=self.restart)
		restartb.pack(side=RIGHT, pady=20, padx=20)

	def _griddraw(self):
		""" Draws the horizontal and vertical lines """

		line_color = "black"
		Tile_width = self.width / self.size

		for n in range(1, self.size):
			# Vertical lines
			self.main_canvas.create_line(n * Tile_width, 0, n * Tile_width, self.width, fill=line_color)
			# Horizontal lines
			self.main_canvas.create_line(0, n * Tile_width, self.width, n * Tile_width, fill=line_color)

	def _Tilesetup(self, info):
		""" Spawns 'nstart' new Tiles and draws them """

		idx = 0
		while idx is not info.size * info.size:
			if (info.node.get(idx) is 0):
				self.emptyCell = idx % self.size, int(idx / self.size)
				idx += 1
				continue
			posconv = idx % self.size, int(idx / self.size)  # Converts the new idx into (x, y)
			self.table[idx] = Tile.Cell(self.main_canvas, self.root, posconv, self.width / self.size, info.node.get(idx))
			idx += 1

	def _right(self):
		""" Move the Tile on the left of the empty cell"""

		if (self.emptyCell[0] is not 0):
			idx = self.emptyCell[0] + self.emptyCell[1] * self.size
			c = self.table[idx - 1]
			self.table[idx - 1] = self.table[idx]
			self.table[idx] = c

			self.move(c)
			lst = list(self.emptyCell)
			lst[0] -= 1
			self.emptyCell = tuple(lst)
			self._scorevar.set(int(self._scorevar.get()) + 1)

	def _left(self):
		""" Move the Tile on the right of the empty cell"""

		if (self.emptyCell[0] is not self.size - 1):
			idx = self.emptyCell[0] + self.emptyCell[1] * self.size
			c = self.table[idx + 1]
			self.table[idx + 1] = self.table[idx]
			self.table[idx] = c

			self.move(c)
			lst = list(self.emptyCell)
			lst[0] += 1
			self.emptyCell = tuple(lst)
			self._scorevar.set(int(self._scorevar.get()) + 1)

	def _down(self):
		""" Move the Tile over the empty cell"""

		if (self.emptyCell[1] is not 0):
			idx = self.emptyCell[0] + self.emptyCell[1] * self.size
			c = self.table[idx - self.size]
			self.table[idx - self.size] = self.table[idx]
			self.table[idx] = c

			self.move(c)
			lst = list(self.emptyCell)
			lst[1] -= 1
			self.emptyCell = tuple(lst)
			self._scorevar.set(int(self._scorevar.get()) + 1)

	def _up(self):
		""" Move the Tile under the empty cell """

		if (self.emptyCell[1] is not self.size - 1):
			idx = self.emptyCell[0] + self.emptyCell[1] * self.size
			c = self.table[idx + self.size]
			self.table[idx + self.size] = self.table[idx]
			self.table[idx] = c

			self.move(c)
			lst = list(self.emptyCell)
			lst[1] += 1
			self.emptyCell = tuple(lst)
			self._scorevar.set(int(self._scorevar.get()) + 1)

	def move(self, c):
		newx, newy = tuple(self.emptyCell)
		c.move(newx - c.pos[0] , newy - c.pos[1])
		c.pos = newx, newy

def StartGame(info):
	root = Tk()

	map = Map(root, info)

	root.bind("<a>", lambda event: map.callback(0))
	root.bind("<d>", lambda event: map.callback(1))
	root.bind("<w>", lambda event: map.callback(3))
	root.bind("<s>", lambda event: map.callback(2))

	root.bind("<r>", lambda event: map.restart())

	root.mainloop()
