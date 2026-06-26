from graph import StateGraph
from states import State
sg = StateGraph(State([3,1,2,4,7,5,6,8,0]))
lst = sg.A_star()
if lst == None:
    print('puzzle is unsolveable')
else:
    for i in lst:
        print(i.st.numlist)