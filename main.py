from tree import StateTree
from states import State
import tk
from time import time
sg = None
with open("inputs.txt","r") as f:#change input file
    s = f.read()
    lst = []
    for i in s:
        if i in '0123456789ABCDEF':
            lst.append('0123456789ABCDEF'.index(i))
    sg = StateTree(State(lst))
start = time()
res = sg.IDS()
end = time()
print("ran for ",end-start)
if res == None:
    print('puzzle is unsolveable')
idx = 0
def next(event):
    global idx
    if idx>=len(res):
        return
    i = res[idx]
    print(i.st.numlist)
    tk.cnv.delete("all")
    tk.cnv.create_rectangle(0,0,400,400,fill="#FFFF85")
    tk.drawState(i.st.numlist)
    idx += 1
tk.cnv.focus_set()
tk.scr.bind_all("<Button-1>",next)
tk.scr.mainloop()