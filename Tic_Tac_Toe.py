from tkinter import *

def checked(button):
    global player
    if button["text"] != "          ":
        return
    button["text"] =  "    " + player+"    "
    button["bg"] = "yellow"

    if player == "X":
        player = "O"
        player_name()
        button["bg"] = "yellow"
        win()

    else:
        player = "X"
        button["bg"] = "lightgreen"
        win()

    player_name()
        
def dis():
    for x in range(9):
        btn = list[x]
        btn.config(state=DISABLED)

def nor():
    for x in range(9):
        btn = list[x]
        btn.config(state=NORMAL)
        btn["text"] = "          "
        btn["bg"] = "white"

def player_name():
    current_player = "현재 player는 " + player
    name = Label(tk, text = current_player, font = ("bold", 13))
    name.place(x = 280,y = 90)
    
def res():
    nor()
    t.config(text = "Tic Tac Toe")

def win():
    if a0["text"] == "    X    " and a1["text"] == "    X    " and a2["text"] == "    X    ":
        t.config(text = "!! X의 승리 !!")
        dis()

    elif a3["text"] == "    X    " and a4["text"] == "    X    " and a5["text"] == "    X    ":
        t.config(text = "!! X의 승리 !!")
        dis()

    elif a0["text"] == "    X    " and a3["text"] == "    X    " and a6["text"] == "    X    ":
        t.config(text = "!! X의 승리 !!")
        dis()
    elif a1["text"] == "    X    " and a4["text"] == "    X    " and a7["text"] == "    X    ":
        t.config(text = "!! X의 승리 !!")
        dis()
    elif a2["text"] == "    X    " and a5["text"] == "    X    " and a8["text"] == "    X    ":
        t.config(text = "!! X의 승리 !!")
        dis()
        
    elif a6["text"] == "    X    " and a7["text"] == "    X    " and a8["text"] == "    X    ":
        t.config(text = "!!X의 승리!!")
        dis()

    elif a0["text"] == "    X    " and a4["text"] == "    X    " and a8["text"] == "    X    ":
        t.config(text = "!! X의 승리 !!")
        dis()

    elif a2["text"] == "    X    " and a4["text"] == "    X    " and a6["text"] == "    X    ":
        t.config(text = "!! X의 승리 !!")
        dis()
        
    elif a0["text"] == "    O    " and a1["text"] == "    O    " and a2["text"] == "    O    ":
        t.config(text = "!! O의 승리 !!")
        dis()

    elif a3["text"] == "    O    " and a4["text"] == "    O    " and a5["text"] == "    O    ":
        t.config(text = "!! O의 승리 !!")
        dis()

    elif a6["text"] == "    O    " and a7["text"] == "    O    " and a8["text"] == "    O    ":
        t.config(text = "!! O의 승리 !!")
        dis()
        
    elif a0["text"] == "    O    " and a4["text"] == "    O    " and a8["text"] == "    O    ":
        t.config(text = "!! O의 승리 !!")
        dis()

    elif a2["text"] == "    O    " and a4["text"] == "    O    " and a6["text"] == "    O    ":
        t.config(text = "!! O의 승리 !!")
        dis()

    elif a0["text"] == "    O    " and a3["text"] == "    O    " and a6["text"] == "    O    ":
        t.config(text = "!! O의 승리 !!")
        dis()
        
    elif a1["text"] == "    O    " and a4["text"] == "    O    " and a7["text"] == "    O    ":
        t.config(text = "!! O의 승리 !!")
        dis()
        
    elif a2["text"] == "    O    " and a5["text"] == "    O    " and a8["text"] == "    O    ":
        t.config(text = "!! O의 승리 !!")
        dis()

tk = Tk()
tk.geometry("500x300")
player = "X"

tic = Frame(tk,width = 300, height = 200)
tic.grid(padx = 50,pady = 20)

down_pack = Frame(tk, width = 100, height = 50)
down_pack.grid(padx = 60)

tk.title("Tic Tac Toe")
t = Label(tic,text = "Tic Tac Toe",font = (15), fg = "red",pady = 20)
t.grid(row = 2,columnspan = 4)



list = []

a0 = Button(tic,text = "          ",bg = "white",width = 6,height = 2, command = lambda :checked(a0))
a0.grid(row=4,column=1)
list.append(a0)

a1 = Button(tic,text = "          ",bg = "white",width = 6,height = 2, command = lambda :checked(a1))
a1.grid(row=4,column=2)
list.append(a1)

a2 = Button(tic,text = "          ",bg = "white",width = 6,height = 2, command = lambda :checked(a2))
a2.grid(row=4,column=3)
list.append(a2)

a3 = Button(tic,text = "          ", bg = "white",width = 6,height = 2,command = lambda :checked(a3))
a3.grid(row=5,column=1)
list.append(a3)

a4 = Button(tic,text = "          ",bg = "white",width = 6,height = 2, command = lambda :checked(a4))
a4.grid(row=5,column=2)
list.append(a4)

a5 = Button(tic,text = "          ",bg = "white",width = 6,height = 2, command = lambda :checked(a5))
a5.grid(row=5,column=3)
list.append(a5)

a6 = Button(tic,text = "          ",bg = "white",width = 6,height = 2, command = lambda :checked(a6))
a6.grid(row=6,column=1)
list.append(a6)

a7 = Button(tic,text = "          ",bg = "white",width = 6,height = 2, command = lambda :checked(a7))
a7.grid(row=6,column=2)
list.append(a7)

a8 = Button(tic,text = "          ",bg = "white",width = 6,height = 2, command = lambda :checked(a8))
a8.grid(row=6,column=3)
list.append(a8)

restart = Button(down_pack, text = "restart",width = 6, command = res)
restart.pack()

tic.mainloop()
