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

	def print_grid(self):
		i = 0
		for f in self.queue:
			print(f, end = " ")
			i += 1
			if i >= math.sqrt(len(self.queue)):
				i = 0
				print()

	def get(self, index):
		return self.queue[index]

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
