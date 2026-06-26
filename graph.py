from pq import PriorityQueue
class Node:
    def __init__(self,s):
        self.st = s
        self.pre = None
        self.nexts = []
class StateGraph:
    def __init__(self,start):
        self.head = Node(start)
    def visit(self,nd):
        for i in nd.st.nextStates():
            x = Node(i)
            x.pre = nd
            nd.nexts.append(x)
    def A_star(self):
        fringe = PriorityQueue(1000000)
        fringe.insert(self.head, self.head.st.manhatandist)
        visited = set()
        g_cost = {self.head.st: 0}
        while not fringe.empty():
            current, f = fringe.pop()
            if current.st in visited:
                continue
            visited.add(current.st)
            if current.st.manhatandist == 0:
                path = []
                while current is not None:
                    path.append(current)
                    current = current.pre
                return path[::-1]
            self.visit(current)
            for child in current.nexts:
                if child.st in visited:
                    continue
                new_g = g_cost[current.st] + 1
                if child.st not in g_cost or new_g < g_cost[child.st]:
                    g_cost[child.st] = new_g
                    child.pre = current
                    f_cost = new_g + child.st.manhatandist
                    fringe.insert(child, f_cost)
        #print('puzzle is unsolveable')
        return None