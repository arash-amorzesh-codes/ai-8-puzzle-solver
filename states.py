#1  2  3
#4  5  6
#7  8  0
#0 is free space
#x = n%3 , y = n//3
#lst indexes are positions and values are tiles
def mdist(x,y):
    return abs(x%3-y%3) + abs(x//3-y//3) # changes to abs(x%4-y%4) + abs(x//4-y//4) 
class State:
    def __eq__(self, other):
        return self.numlist == other.numlist
    def __hash__(self):
        return hash(tuple(self.numlist))
    def __init__(self,lst):
        self.numlist = lst
        self.manhatandist = 0
        for pos in range(9):#changes to range(16)
            tile = (self.numlist[pos]-1)%9
            if tile != 0:
                self.manhatandist += mdist(pos, tile)
    def nextStates(self):
        st = []
        i = self.numlist.index(0)
        if i not in [2,5,8]:#changes to [3,7,11,15]
            newl = self.numlist[:]
            newl[i],newl[i+1] = newl[i+1],newl[i]
            st.append(State(newl))
        if i not in [6,7,8]:#changes to [12,13,14,15]
            newl = self.numlist[:]
            newl[i],newl[i+3] = newl[i+3],newl[i]#changes to +4
            st.append(State(newl))
        if i not in [0,1,2]:#changes to [0,1,2,3]
            newl = self.numlist[:]
            newl[i],newl[i-3] = newl[i-3],newl[i]#changes to -4
            st.append(State(newl))
        if i not in [0,3,6]:#changes to [0,4,8,12]
            newl = self.numlist[:]
            newl[i],newl[i-1] = newl[i-1],newl[i]
            st.append(State(newl))
        return st