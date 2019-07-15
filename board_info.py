import array
import sys
import math

class PriorityQueue(object):
	def __init__(self):
		self.queue = []

	def __str__(self):
		return ' '.join([str(i) for i in self.queue])

	def isEmpty(self):
		return len(self.queue) == []

	def insert(self, data):
		if data in self.queue:
			sys.exit("%s Duplicated ERROR !" % data)
		self.queue.append(data)

	def get(self, index):
		return self.queue[index]

	def getAll(self):
		ret = [0] * len(self.queue)
		for index in range(len(self.queue)):
			ret[index] = self.get(index)
		return ret

	def delete(self):
		try:
			max = 0
			for i in range(len(self.queue)):
				if self.queue[i] > self.queue[max]:
					max = i
			item = self.queue[max]
			del self.queue[max]
			return item
		except IndexError:
			print("Exception")
			exit()

class BoardInfo():
	size = 0
	node = PriorityQueue()

	def print_grid(self, grid):
		i = 0
		for f in grid:
			print(f, end = " ")
			i += 1
			if i >= math.sqrt(len(grid)):
				i = 0
				print()

	def solutionGridLine(self):
		p = [0] * self.size**2
		p = self.node.getAll()
		p.sort()
		p.pop(0)
		p.append(0)
		return p

	def solutionGridSnail(self):
		ret = [0] * self.size**2
		p = self.solutionGridLine()

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
					print()
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
		return ret
