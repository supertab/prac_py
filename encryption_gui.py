from tkinter import *
from encryption_source import *
from PIL import Image, ImageTk  # pillow 模块

root = Tk()
#pack(padx, pady) 设置与边框的距离，单位（像素）
root.title("加密小程序")
root.resizable(False, False)
class Var:
    msg = ""
    cipher = ""

#添加文本框，显示文本
#tShowMsg = Text(root, yscrollcommand=sb.set)#文本框注入
#使用pack设置位置
#tShowMsg.pack()
#使用grid()设置位置

txtw = 50
txth = 10
btw = 12
bth = 1#30ppi


tShowMsg = Text(root, width=txtw, height=txth)
tShowMsg.grid(row=0, column=0, rowspan=2, padx=10, pady=10)


tShowMsg.insert(INSERT, "显示框")


#输入框，只能输入一行
#eInputMsg = Entry(root)
#eInputMsg.pack()
#使用文本框进行输入
eInputMsg = Text( root, width=txtw, height=txth )
eInputMsg.grid( row=2, column=0, rowspan=2, padx=10, pady=10 )
eInputMsg.insert(INSERT, "输入框")

def TipClear(event):
    if event.widget.get(1.0, END) in ("输入框\n", "显示框\n"):#get会自动插入换行符
        event.widget.delete(1.0, END)

eInputMsg.bind("<Button-1>", TipClear)
tShowMsg.bind("<Button-1>", TipClear)

class section:
    def onCopy(self, TextFlame):
        root.clipboard_clear()
        root.clipboard_append( TextFlame.get(1.0, END))
    def onPaste(self, TextFlame):
        TextFlame.insert(INSERT, root.clipboard_get())
    def onCut(self, TextFlame):
        self.onCopy(TextFlame)
        TextFlame.delete(1.0, END)
section = section()

def popmenu(event):
    menu = Menu(root, tearoff=0)
    menu.add_command(label="复制", command=lambda:section.onCopy(event.widget))
    menu.add_separator()
    menu.add_command(label="粘贴", command=lambda:section.onPaste(event.widget))
    menu.add_separator()
    menu.add_command(label="剪切", command=lambda:section.onCut(event.widget))
    menu.post(event.x_root, event.y_root)
eInputMsg.bind("<ButtonRelease-3>", popmenu)
tShowMsg.bind("<ButtonRelease-3>", popmenu)

def encrypt_gui():
    tShowMsg.delete(1.0, END)
    Var.msg = eInputMsg.get(1.0, END)
    Var.cipher = encrypt(Var.msg)
    tShowMsg.insert(INSERT, Var.cipher)

bEncryption = Button( root, text="加密", command=encrypt_gui, width=btw, height=bth)
bEncryption.grid( row=0, column=1, padx=10, pady=10, sticky=N)

def crack_gui():
    tShowMsg.delete(1.0, END)
    Var.cipher = eInputMsg.get(1.0, END)
    Var.msg = crack(Var.cipher)
    tShowMsg.insert(INSERT, Var.msg)

def sav():
    save_info(Var.msg, Var.cipher)
    tShowMsg.delete(1.0, END)
    tShowMsg.insert(INSERT, "保存成功，文件名为record.txt~")

Button(root, text="解密", command=crack_gui, width=btw, height=bth ).place(x=384, y=60)#


Button(root, text="保存", command=sav, width=btw, height=bth).place(x=384, y=110)
#退出
Button(root, text="退出", command=root.quit, width=btw, height=bth).place(x=384, y=160)

#添加图片
photo =ImageTk.PhotoImage(Image.open("fang.jpg"))
imgLabel = Label(root, image=photo)
imgLabel.place(x=384, y=210)


############
#窗口居中
root.update()                       # update window ,must do
curWidth = root.winfo_reqwidth()    # get current width
curHeight = root.winfo_height()     # get current height
scnWidth,scnHeight = root.maxsize() # get screen width and height
# now generate configuration information
tmpcnf = '%dx%d+%d+%d'%(curWidth,curHeight,
(scnWidth-curWidth)/2,(scnHeight-curHeight)/2)
root.geometry(tmpcnf)
###########
mainloop()

