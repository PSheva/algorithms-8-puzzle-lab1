from copy import deepcopy
from collections import deque
import random
import time
from typing import Counter

target =   [[0, 1, 2], 
            [3, 4, 5],
            [6, 7, 8]]

example =   [[3, 1, 5], 
             [8, 4, 6],
             [2, 0, 7]]

empty = [[],[],[]]

def iterate():
        global iteration 
        iteration += 1

def add_to_memory():
    global nodes_in_memory
    nodes_in_memory += 1

class Node:

    def __init__(self, state=empty, way=0, steps=0) -> None:
        if state == empty: 
            self.state = self.rand(steps)
        else:
            self.state = state
        self.childrens = []
        self.way_cost = way

    def rand(self, steps):
        state = deepcopy(target)
        collumn = 0
        row = 0

        for i in range(0, steps):
            n = random.randint(1, 4)

            if n == 1: 
                if collumn-1 >= 0:
                    state[row][collumn] = state[row][collumn-1]
                    state[row][collumn-1] = 0

                    collumn -= 1
                else:
                    n = 2
            
            if n == 2: 
                if collumn+1 < 3:
                    state[row][collumn] = state[row][collumn+1]
                    state[row][collumn+1] = 0

                    collumn += 1
                else:
                    n = 3
            
            if n == 3: 
                if row-1 >= 0:
                    state[row][collumn] = state[row-1][collumn]
                    state[row-1][collumn] = 0

                    row -= 1
                else:
                    n = 4
            
            if n == 4: 
                if row+1 < 3:
                    state[row][collumn] = state[row+1][collumn]
                    state[row+1][collumn] = 0

                    row += 1
                else:
                    n = 1
            

        return state

    def is_target(self):
        if self.state == target:
            return True
        
        return False

    def children(self):

        for i in range(0, 3):
            for j in range(0, 3):
                if self.state[i][j] == 0:
                    row = i
                    collumn = j
                    break

        self.left(row, collumn)
        self.right(row, collumn)
        self.up(row, collumn)
        self.down(row, collumn)

    def left(self, row, collumn):

        child = deepcopy(self.state)

        if collumn-1 >= 0:
            child[row][collumn] = child[row][collumn-1]
            child[row][collumn-1] = 0

            self.childrens.append(Node(child, self.way_cost+1))
            add_to_memory()
    
    def right(self, row, collumn):

        child = deepcopy(self.state)

        if collumn+1 < 3:
            child[row][collumn] = child[row][collumn+1]
            child[row][collumn+1] = 0

            self.childrens.append(Node(child, self.way_cost+1))
            add_to_memory()

    def up(self, row, collumn):

        child = deepcopy(self.state)

        if row-1 >=0:
            child[row][collumn] = child[row-1][collumn]
            child[row-1][collumn] = 0

            self.childrens.append(Node(child, self.way_cost+1))
            add_to_memory()

    def down(self, row, collumn):

        child = deepcopy(self.state)

        if row+1 < 3:
            child[row][collumn] = child[row+1][collumn]
            child[row+1][collumn] = 0

            self.childrens.append(Node(child, self.way_cost+1))
            add_to_memory()
    
    def DLS(self, maxDepth):

        iterate()

        if self.is_target() : 
            print(self.way_cost+1)
            return True

        if self.way_cost >= maxDepth :
            return False

        if self.childrens == []:
            self.children()

        for i in self.childrens:
                if(i.DLS(maxDepth)):
                    return True
        return False

    def IDS(self):

        i = 0
        while True:
            if (self.DLS(i)):
                return True
            i += 1
        


if __name__ == '__main__':

    Counter= 0
    for _ in range(15):
        iteration = 0
        nodes_in_memory = 0
        Counter = Counter+1
        print(f"Node number: {Counter}")

        
        problem = Node(empty, 0, 20)
        print(problem.state)

        
        print(problem.IDS())
        print(iteration)
        print(nodes_in_memory)



 