import priority_queue
import math

class BoardInfo():
	size = 0
	node = priority_queue.PriorityQueue()
	greedy = False
	uniform = False
	heuristics = 0
	visualizer = False
	solution = 1

	def __init__(self, args):
		self.greedy = args.greedy
		self.uniform = args.uniform
		self.heuristics = args.heuristics
		self.visualizer = args.visualizer
		self.solution = args.solution

	def print_grid(self, grid):
		i = 0
		for f in grid:
			print(f, end = " ")
			i += 1
			if i >= math.sqrt(len(grid)):
				i = 0
				print()

	def solutionGrid(self, snail = 1):
		print("SOLUTION GRID :")
		ret = [0] * self.size**2

		# Solution Grid Line
		p = [0] * self.size**2
		p = self.node.getAll()
		p.sort()
		p.pop(0)
		p.append(0)

		if snail is 0:
			return p

		index = self.size - 1
		s_index = index
		size = self.size
		for m_size in range(size):
			ret[m_size] = p[m_size]
		size -= 1
		dir = 1
		# dir 1 = Down, 2 = Left, 3 = Up, 4 = Right
		while (size):
			if dir is 1 :
				for m_size in range(size):
					ret[s_index + (m_size + 1) * self.size] = p[index + m_size + 1]
				s_index += size * self.size
			elif dir is 2 :
				for m_size in range(size):
					ret[s_index - (m_size + 1)] = p[index + m_size + 1]
				s_index -= size
			elif dir is 3 :
				for m_size in range(size):
					ret[s_index - (m_size + 1) * self.size] = p[index + m_size + 1]
				s_index -= size * self.size
			elif dir is 4 :
				for m_size in range(size):
					ret[s_index + m_size + 1] = p[index + m_size + 1]
				s_index += size
			index += size
			dir += 1
			if (dir % 2):
				size -= 1
			if (dir is 5):
				dir = 1
		print(ret)
		return ret

	def countInversion(self, snail = 0):
		tab = [0] * self.size**2
		tab = self.node.getAll()
		p = [0] * self.size**2
		p = self.node.getAll()
		count = 0

		if (snail is 0):
			for i in range(self.size**2):
				a = 0
				while (tab[i] is not 0 and a + i < self.size**2):
					if (tab[i + a] is not 0 and tab[i + a] < tab[i]):
						count += 1
					a += 1
			print("Count Inversion :", end=" ")
			return count
			
		dir = 1
		size = self.size - 1
		index = size
		s_index = index
		while (size):
			if dir is 1 :
				for m_size in range(size):
					tab[index + m_size + 1] = p[s_index + (m_size + 1) * self.size]
				s_index += size * self.size
			elif dir is 2 :
				for m_size in range(size):
					tab[index + m_size + 1] = p[s_index - (m_size + 1)]
				s_index -= size
			elif dir is 3 :
				for m_size in range(size):
					tab[index + m_size + 1] = p[s_index - (m_size + 1) * self.size]
				s_index -= size * self.size
			elif dir is 4 :
				for m_size in range(size):
					tab[index + m_size + 1] = p[s_index + m_size + 1]
				s_index += size
			index += size
			dir += 1
			if (dir % 2):
				size -= 1
			if (dir is 5):
				dir = 1
		print("GRID SNAIL :", tab)
		for i in range(self.size**2):
			a = 0
			while (tab[i] is not 0 and a + i < self.size**2):
				if (tab[i + a] is not 0 and tab[i + a] < tab[i]):
					count += 1
				a += 1
		print("Count Inversion :", end=" ")
		return count
