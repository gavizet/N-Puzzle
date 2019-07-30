# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    algorithm.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gavizet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/07/30 10:46:18 by gavizet           #+#    #+#              #
#    Updated: 2019/07/30 15:03:18 by gavizet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from priority_queue import PriorityQueue
from node import Node

'''
PLAN
OPEN = priority queue containing START
CLOSED = empty set
while lowest rank in OPEN is not GOAL:
    current = remove lowest rank item from open
    add current to CLOSED
    for nieghbors of current:
        cost = g(current) + movementcost(current, neighbor)
        if neighbor in OPEN and cost less than g(neighbor):
            remove neighbord from OPEN, because new path is better
        # should not happen if we use admissible heuristics
        if neighbor in CLOSED and cost less than g(neighbor):
            remove neighbor from CLOSED
        if neighbor not in OPEN and neighbor not in CLOSED:
            set g(neighbor) to cost
            add neighbor to OPEN
            set prio queue rank to g(neighbor) + h(neighbor)
            set neighbor's parent to current
reconstruct reverse path from goal to start by following parent pointers
'''

'''
STEPS
1. Add the starting node to the open lis
2. Repeat the following :
    A. look for the lowest cost tile in the open list. He is referred to as
    the current node
    B. switch it to the closed list
    C. for each of the 4 tiles adjacent to this current node :
        * If not walkable or in closed set, ignore it.
        * if it is not on the open list, add it to the open list. Make the
        current node the parent of this node. Record the F, G and H cost of the
        node.
        * If already in the open list, check to see if this path to that node
        is better, using G cost as a measure. A lower G cost means that this is
        a better path. If so, change the parent of the node to the current node,
        and recalculate the G and F score of the square. If you are keeping your
        open list sorted by F score, you may need to resort the list to account
        for the change.
    D. Stop when :
        * you fail to find a target node and open set queue is empty.

'''

'''
Pseudocode for that plan :
// Initialize both open and closed list
let the openList equal empty list of nodes
let the closedList equal empty list of nodes

// Add the start node
put the startNode on the openList (leave it's F at zero)

// Loop until you find the end
while open list not empty
    // get the current node
    let the currentNode equal the node with the least F value
    remove currentNode from the openList
    add currentNode to closedList

    // found the goal
    if currentNode is goal
        gg. Backtrack to get the path

    // generate children
    let the children of the currentNode equal to the adjacent nodes
    for each child
        // child is on the closedList
        if child is in the closedList
            continue to beginning of for loop
        // create f, g and h values
        child.g = currentNode.g + distance between child and current
        child.h = distance from child to end
        child.f = child.g + child.h
        
        // child aready in openList
        if child.position is in the openList's nodes positions
            if the child.g is higher than the openList node's g
                continue to beginning of for loop
        
        // add child to the openList
        add the child to the openList
'''

class Solver():

    def __init__(self):

    def current_is_goal(self):
        """
        Compares the current state to the final / goal state and return true /
        false
        """
        if node.state == self.end_state:
            return True
        else:
            return False

    def get_children(node, size):
        """
        Gets all the possible children of the current node, depending on it's
        position and the size of the puzzle.
        """
        empty_tile = node.index(0)
        children = []
        if empty_tile % size > 0:
            child = node.copy()
            left = empty_tile - 1
            child[empty_tile], child[left] = child[left], child[empty_tile]
            children.append(tuple(child))
        if empty_tile % size + 1 < size:
            child = node.copy()
            right = empty_tile + 1
            child[empty_tile], child[right] = child[right], child[empty_tile]
            children.append(tuple(child))
        if empty_tile - size >= 0:
            child = node.copy()
            up = empty_tile - size
            child[empty_tile], child[up] = child[up], child[empty_tile]
            children.append(tuple(child))
        if empty_tile + size < len(node)
            down = empty_tile + size
            child[empty_tile], child[down] = child[down], child[empty_tile]
            children.append(tuple(child))
        return children


    def astar(self, start, end, heuristic, cost):
        """
        start       : starting puzzle grid
        end         : resolved puzzle grid
        heuristic   : admissible heuristic function used to calculate h(n)
        cost        : transition cost for each movement
            
        open_set    : contains the nodes that are candidates to be examined
        closed_set  : contains the nodes that have already been examined
            
        Return a list of tuples as a path from the given starting puzzle to the
        solution puzzle
        """

        # Initialize open and closed sets
        start_node = Node(start_puzzle, cost, None)
        open_set = PriorityQueue()
        closed_set = {}
        # Add the start node to priority queue
        open_set.put(start, 0)
            
        # Loop until there is no item left in priority queue
        while not open_set.empty():
            current_node == open_set.get()

            # If current_node is equal to end, then algorithm is over
            if current_node == end:
                # Will have to return the solution later on
                return True
            # Get a list of current node children
            children = self.get_children()
            # Loop through children
            for child in children:
                print('this is a child')
