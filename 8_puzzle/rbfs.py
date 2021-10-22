from copy import deepcopy
from collections import deque



list_of_nodes = [
    [[3, 1, 2],[4, 0, 5],[8, 6, 7]],
    [[2, 6, 3],[1, 4, 5],[0, 7, 8]],
    [[1, 4, 2],[3, 0, 5],[6, 7, 8]],
    [[3, 1, 2],[4, 7, 5],[6, 0, 8]],
    [[1, 2, 5],[3, 0, 4],[6, 7, 8]],
    [[3, 1, 2],[4, 5, 8],[6, 7, 0]],
    [[3, 7, 5],[4, 0, 1],[6, 8, 2]],
    [[4, 3, 1],[7, 6, 2],[5, 0, 8]],
    [[1, 0, 4],[3, 5, 2],[6, 7, 8]],
    [[3, 1, 2],[4, 0, 7],[6, 8, 5]],
    [[1, 2, 5],[3, 7, 4],[0, 6, 8]],
    [[1, 5, 4],[3, 0, 2],[6, 7, 8]],
    [[3, 0, 1],[6, 4, 2],[7, 8, 5]],
    [[4, 0, 2],[1, 7, 5],[3, 6, 8]],
    [[3, 5, 1],[4, 2, 0],[6, 7, 8]],
    [[4, 3, 2],[6, 0, 5],[7, 1, 8]],
    [[1, 5, 4],[3, 2, 8],[6, 7, 0]],
    [[1, 2, 0],[3, 5, 8],[6, 7, 4]],    
    [[4, 1, 3],[6, 8, 2],[7, 5, 0]],
    [[5, 3, 1],[2, 4, 6],[0, 8, 7]]
]

def contains(lis, node):
        for el in lis:
            if el.state == node.state:
                return True
        return False

target =   [[0, 1, 2], 
            [3, 4, 5],
            [6, 7, 8]]

class Node:
    def __init__(self, state, parent_way) -> None:
        self.state = state
        self.to_end = self.H1()
        self.from_start = parent_way+1
        self.childrens = []


    def is_target(self):
        if self.state == target:
            return True
        
        return False

    def children(self):
        childrens = []

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

            self.childrens.append(Node(child, self.from_start))

            #all_nodes += 1
    
    def right(self, row, collumn):

        child = deepcopy(self.state)

        if collumn+1 < 3:
            child[row][collumn] = child[row][collumn+1]
            child[row][collumn+1] = 0

            self.childrens.append(Node(child, self.from_start))

            #all_nodes += 1

    def up(self, row, collumn):

        child = deepcopy(self.state)

        if row-1 >=0:
            child[row][collumn] = child[row-1][collumn]
            child[row-1][collumn] = 0

            self.childrens.append(Node(child, self.from_start))

            #all_nodes += 1

    def down(self, row, collumn):

        child = deepcopy(self.state)

        if row+1 < 3:
            child[row][collumn] = child[row+1][collumn]
            child[row+1][collumn] = 0

            self.childrens.append(Node(child, self.from_start))

            #all_nodes += 1

    def H1(self):
        count = 0

        for i in range(0, 3):
            for j in range(0, 3):
                if target[i][j] != self.state[i][j]:
                    count += 1
        
        return count


    def RBFS(self):
        cur = open[0]
        iteration = 0
        while(open):
            iteration += 1
            cur = min(open, key = lambda x: x.to_end + cur.from_start)
            if contains(closed, cur):
                    open.remove(cur)
                    continue

            if cur.state == target: 
                print('Iterations: ' + str(iteration))
                return cur.from_start

            open.remove(cur)
            closed.append(cur)

            cur.children()

            for el in cur.childrens:
                if not contains(open, el):
                    open.append(el)




if __name__ == '__main__':
    i = 0

    for el in list_of_nodes:
        closed = []
        open = []
        i += 1
        print('---------NODE ' + str(i) + '-----------')
        temp = Node(el, -1)

        print(temp.state)

        open.append(temp)

        print('Nodes: ' + str(temp.RBFS()))

        print('Nodes in memory: ' + str(len(open)) + str(len(closed)))


