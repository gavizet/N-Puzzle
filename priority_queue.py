import heapq

class PriorityQueue():
	
    def __init__(self):
        """
        queue           : represents the priority queue
        max_state_nb    : maximum number of states ever recorded in memory
        """
	self.queue = []
        max_state_nb = 0

    def empty(self):
        """ Returns True if self.queue is empty """
        return len(self.queue) == 0

    def put(self, node, prio):
        """
        Push a new state (node) into the queue.
        If the current number of recorded states in queue is greater than
        previously recorded max number of state, then add 1 to it.
        """
        heapq.heappush(self.queue, (node, prio))
        if self.max_state_nb < len(self.queue):
            self.max_state_nb += 1

    def get(self):
        """ """
