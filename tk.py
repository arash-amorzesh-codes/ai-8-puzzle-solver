import tkinter
scr = tkinter.Tk("game")
cnv = tkinter.Canvas(scr,width=400,height=400)
cnv.place(x=0,y=0)
cnv.create_rectangle(0,0,400,400,fill="#FFFF85")
def drawState(lst):
    for i in range(9):
        if lst[i] == 0:
            continue
        x,y = i%3,i//3#changes to %4 //4
        x,y = x*133,y*133#changes to *100
        x,y = x+66,y+66#changes to +50
        cnv.create_rectangle(x-60,y-60,x+60,y+60,fill="#FF8526")#changes to -44 +44
        cnv.create_text(x,y,text=str(lst[i]))