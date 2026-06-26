from graph import StateGraph
from states import State
def diff(a,b):
    i,j = a.index(0),b.index(0)
    if j == i-3:
        return 'u'
    if j == i+3:
        return 'd'
    if j == i+1:
        return 'r'
    if j == i-1:
        return 'l'
sg = None
with open("inputs.txt","r") as f:
    s = f.read()
    lst = []
    for i in s:
        if i.isnumeric():
            lst.append(int(i))
    sg = StateGraph(State(lst))
res = sg.A_star()
if res == None:
    print('puzzle is unsolveable')
else:
    s = ''
    for i in range(len(res)-1):
        s+=diff(res[i].st.numlist,res[i+1].st.numlist)
    for i in res:
        print(i.st.numlist)
    print(s)
 