from tkinter import *

def checked(button):
    global player
    if button["text"] != "          ":
        return
    button["text"] =  "    " + player+"    "
    button["bg"] = "yellow"

    if player == "X":
        player = "O"
        button["bg"] = "yellow"
        win()

    else:
        player = "X"
        button["bg"] = "lightgreen"
        win()
        
def dis():
    a0.config(state=DISABLED)
    a1.config(state=DISABLED)
    a2.config(state=DISABLED)
    a3.config(state=DISABLED)
    a4.config(state=DISABLED)
    a5.config(state=DISABLED)
    a6.config(state=DISABLED)
    a7.config(state=DISABLED)
    a8.config(state=DISABLED)
    
def win():
    if a0["text"] == "    X    " and a1["text"] == "    X    " and a2["text"] == "    X    ":
        t.config(text = "!!X의 승리!!")
        dis()

    elif a3["text"] == "    X    " and a4["text"] == "    X    " and a5["text"] == "    X    ":
        t.config(text = "!!X의 승리!!")
        dis()

    elif a0["text"] == "    X    " and a3["text"] == "    X    " and a6["text"] == "    X    ":
        t.config(text = "!!X의 승리!!")
        dis()
    elif a1["text"] == "    X    " and a4["text"] == "    X    " and a7["text"] == "    X    ":
        t.config(text = "!!X의 승리!!")
        dis()
    elif a2["text"] == "    X    " and a5["text"] == "    X    " and a8["text"] == "    X    ":
        t.config(text = "!!X의 승리!!")
        dis()
        
    elif a6["text"] == "    X    " and a7["text"] == "    X    " and a8["text"] == "    X    ":
        t.config(text = "!!X의 승리!!")
        dis()

    elif a0["text"] == "    X    " and a4["text"] == "    X    " and a8["text"] == "    X    ":
        t.config(text = "!!X의 승리!!")
        dis()

    elif a2["text"] == "    X    " and a4["text"] == "    X    " and a6["text"] == "    X    ":
        t.config(text = "!!X의 승리!!")
        dis()
        
    elif a0["text"] == "    O    " and a1["text"] == "    O    " and a2["text"] == "    O    ":
        t.config(text = "!!O의 승리!!")
        dis()

    elif a3["text"] == "    O    " and a4["text"] == "    O    " and a5["text"] == "    O    ":
        t.config(text = "!!O의 승리!!")
        dis()

    elif a6["text"] == "    O    " and a7["text"] == "    O    " and a8["text"] == "    O    ":
        t.config(text = "!!O의 승리!!")
        dis()
        
    elif a0["text"] == "    O    " and a4["text"] == "    O    " and a8["text"] == "    O    ":
        t.config(text = "!!O의 승리!!")
        dis()

    elif a2["text"] == "    O    " and a4["text"] == "    O    " and a6["text"] == "    O    ":
        t.config(text = "!!O의 승리!!")
        dis()

    elif a0["text"] == "    O    " and a3["text"] == "    O    " and a6["text"] == "    O    ":
        t.config(text = "!!O의 승리!!")
        dis()
        
    elif a1["text"] == "    O    " and a4["text"] == "    O    " and a7["text"] == "    O    ":
        t.config(text = "!!O의 승리!!")
        dis()
        
    elif a2["text"] == "    O    " and a5["text"] == "    O    " and a8["text"] == "    O    ":
        t.config(text = "!!O의 승리!!")
        dis()

tk = Tk()
tk.geometry("300x200")
player = "X"
tic = Frame(tk,width = 200, height = 180)
tic.grid(padx = 60)
tk.title("Tic Tac Toe")
t = Label(tic,text = "Tic Tac Toe",font = ("bold",15), fg = "red",pady = 20)
t.grid(row = 2,columnspan = 4)

'''    
for i in range(3):
    for j in range(3):
        z = (3*i)+j
        a_z = Button(tic,text = "          ", command = lambda : checked(a_z))
        a_z.grid(row=i,column=j)


# 왜 아래의 코드와 값이 다를까...
      
'''  

a0 = Button(tic,text = "          ", command = lambda :checked(a0))
a0.grid(row=4,column=1)


a1 = Button(tic,text = "          ", command = lambda :checked(a1))
a1.grid(row=4,column=2)


a2 = Button(tic,text = "          ", command = lambda :checked(a2))
a2.grid(row=4,column=3)


a3 = Button(tic,text = "          ", command = lambda :checked(a3))
a3.grid(row=5,column=1)


a4 = Button(tic,text = "          ", command = lambda :checked(a4))
a4.grid(row=5,column=2)

a5 = Button(tic,text = "          ", command = lambda :checked(a5))
a5.grid(row=5,column=3)


a6 = Button(tic,text = "          ", command = lambda :checked(a6))
a6.grid(row=6,column=1)


a7 = Button(tic,text = "          ", command = lambda :checked(a7))
a7.grid(row=6,column=2)


a8 = Button(tic,text = "          ", command = lambda :checked(a8))
a8.grid(row=6,column=3)



tic.mainloop()
