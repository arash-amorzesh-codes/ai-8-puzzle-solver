from graph import StateGraph
from states import State
import tk
from time import sleep
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
idx = 0
def next(event):
    global idx
    i = res[idx]
    print(i.st.numlist)
    tk.cnv.delete("all")
    tk.cnv.create_rectangle(0,0,400,400,fill="#FFFF85")
    tk.drawState(i.st.numlist)
    idx += 1
tk.cnv.focus_set()
tk.scr.bind_all("<Button-1>",next)
tk.scr.mainloop()