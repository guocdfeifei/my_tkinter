#coding:utf-8
from Tkinter import *

def afei():
    global root
    Label(root,text = "I love python").pack()

root = Tk()
menubar = Menu(root)
fmenu = Menu(menubar)
for item in ['新建 ','打开','保存','另存']:
    fmenu.add_command(label = item)

emenu = Menu(menubar)
for item in ['复制 ','粘帖','剪切']:
    emenu.add_command(label = item)

vmenu = Menu(menubar)
for item in ['默认视图 ','新式视图']:
    vmenu.add_command(label = item)

amenu = Menu(menubar)
for item in ['版权信息 ','注册/激活']:
    amenu.add_command(label = item)

menubar.add_cascade(label = "文件",menu = fmenu)
menubar.add_cascade(label = "编辑",menu = emenu)
menubar.add_cascade(label = "视图",menu = vmenu)
menubar.add_cascade(label = "关于",menu = amenu)

pmenu = Menu(root)
for x in ['Java','C/C++','Vb']:
    pmenu.add_command(label=x)
    
pmenu.add_command(label = 'Python',command = afei)

def pop(event):
    pmenu.post(event.x_root,event.y_root)
    

root.bind("<Button-3>",pop)
root['menu'] = menubar
root.mainloop()