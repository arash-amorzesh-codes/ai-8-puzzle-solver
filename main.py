from tree import StateTree
from states import State
import tk
from tkinter import simpledialog, messagebox
from time import time
method = simpledialog.askinteger("hello","1: Default puzzle\n2: Enter a puzzle\n3: Shuffle the solved puzzle",minvalue=1,maxvalue=3)
if method == 1:
    lst = []
    with open("inputs.txt") as f:
        s = f.read()
        for i in s:
            if i in '0123456789ABCDEF':
                lst.append('0123456789ABCDEF'.index(i))
    if sorted(lst) != list(range(9)):
        messagebox.showerror("JOHN CENA SAYS:","not valid file")
elif method == 2:
    s = simpledialog.askstring("hello","Enter the 9 numbers from 0 to 8, separated by spaces:")
    if s is None:
        name = "Toasty!"
        raise SystemExit
    try:
        lst = [int(i) for i in s.replace(",", " ").split()]
    except ValueError:
        messagebox.showerror("what?","Enter each number from 0 to 8 exactly once.")
        raise SystemExit
    if len(lst) != 9 or sorted(lst) != list(range(9)):
        messagebox.showerror("what?","Enter each number from 0 to 8 exactly once.")
        raise SystemExit
else:
    lst = [1,2,3,4,5,6,7,8,0]
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
def solve():
    global res, idx
    sg = StateTree(State(lst))
    w = simpledialog.askinteger("HELLO WORLD","Enter the way to do search:\n1.A*\n2.IDS",minvalue=1,maxvalue=2)
    if w==1:
        start = time()
        res = sg.A_star()
        end = time()
    else:
        start = time()
        res = sg.IDS()
        end = time()
    print("ran for ",end-start)
    if res == None:
        print('puzzle is unsolveable')
        return
    idx = 0
    tk.scr.bind_all("<Button-1>",next)
num = -26
def move(event):
    global num
    blank = lst.index(0)
    key = event.keysym.lower()
    pos = None
    if key == "w" and blank//3 > 0:
        pos = blank-3
    elif key == "s" and blank//3 < 2:
        pos = blank+3
    elif key == "a" and blank%3 > 0:
        pos = blank-1
    elif key == "d" and blank%3 < 2:
        pos = blank+1
    else:
        return
    if num < 0:
        return
    if num == 0:
        solve()
        return
    num-=1
    if pos is not None:
        lst[blank],lst[pos] = lst[pos],lst[blank]
        tk.cnv.delete("all")
        tk.cnv.create_rectangle(0,0,400,400,fill="#FFFF85")
        tk.drawState(lst)
if method == 3:
    num = simpledialog.askinteger("HARRY KANE","Enter number of moves:")
    tk.cnv.delete("all")
    tk.cnv.create_rectangle(0,0,400,400,fill="#FFFF85")
    tk.drawState(lst)
    tk.cnv.focus_set()
    tk.scr.bind_all("<Key>",move)
else:
    solve()
tk.scr.mainloop()