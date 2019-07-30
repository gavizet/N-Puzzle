import heapq

class PriorityQueue():
	
    def __init__(self):
        """
        queue           : represents the priority queue
        """
	self.queue = []

    def empty(self):
        """ Returns True if self.queue is empty """
        return len(self.queue) == 0

    def put(self, node, prio):
        """
        Push a new state (node) into the queue.
        """
        heapq.heappush(self.queue, (node, prio))

    def get(self):
        """ """
