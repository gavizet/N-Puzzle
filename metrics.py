# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    metrics.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gavizet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/07/30 11:07:31 by gavizet           #+#    #+#              #
#    Updated: 2019/07/30 17:01:35 by gavizet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time

class Metrics():

    def __init__(self):
        """
        search_time     : amount of time it took to execute the search
        moves_to_goal   : number of moves required from the starting state to the
                          goal state
        time_comp       : total number of states ever selected in the open set
        size_comp       : maximum number of states ever represented in memory at
                          the same time during the search
        """
        self.time_comp = 0
        self.size_comp = 0
        self.search_time = 0
        self.start_time = time.time()
        self.moves_to_goal = 0

    def exec_time(self):
        """ Update the value of search_time """
        self.search_time = time.time() - self.start_time 

    def nb_moves_to_goal(self):
        """ Update the value of moves_to_goal"""

    def size_complexity(self):
        """ Udpdate the value of size_comp """
        

    def time_complexity(self):
        """ Udpate the value of time_comp """

    def print_metrics(self):
        """ Print the metrics that we stored during the program's execution """
        print ("Execution time          : {0}".format(self.exec_time))
        print ("Size complexity         : {0}".format(self.size_comp))
        print ("Time complexity         : {0}".format(self.time_comp))
        print ("Number of moves to goal : {0}".format(self.moves_to_goal))
