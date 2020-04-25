from  tkinter import*

def ccc():
	print(entry.get())
	# print(listbox.size())
	listsize=listbox.size()
	listbox.insert(listsize,entry.get())
	# print(listbox.curselection())

def show_msg(a):
	print(a)
	print("====")
	print(listbox.curselection())

root = Tk()
root.title('接口测试')
root.geometry('1140x560')


# frame = Frame(root, relief=RIDGE, borderwidth=2)
# frame.pack(fill=BOTH,expand=1)

frame1=Frame(root,bd=5,relief=RIDGE, borderwidth=2)
# frame1.title("frame1")
frame1.pack(fill=BOTH)

frame2=Frame(root)
# frame2.title("frame2")
frame2.pack(fill=BOTH,expand=1)

frame3=Frame(frame2,bg="black")
frame3.pack(side=LEFT)
frame4=Frame(frame2,bg="black")
frame4.pack(side=RIGHT)

lable=Label(frame1,text="接口地址")
lable.pack(side=LEFT)
entry=Entry(frame1,highlightcolor="red")  #FLAT、SUNKEN、 RAISED 、 GROOVE 、 RIDGE 。默认为 FLAT。
# entry.insert ( 0, "111aa")
# entry.insert ( 4, "22" )
entry.pack(side=LEFT,fill=X,anchor='center',ipadx='125')

test = Button(frame1, text="Click",command=ccc)
test.pack(side=LEFT)

listbox=Listbox(frame1)
# listbox.grid(row=1,column=1,padx=(10,5),pady=10)
# listbox2.grid(row=1,column=2,padx=(5,10),pady=10)
listbox.bind("<<ListboxSelect>>",show_msg)
listbox.pack(side=LEFT,fill=X,expand=1)



text1=Text(frame3,bg="white")
text1.pack(fill=BOTH,expand=1)
text2=Text(frame4,bg="white")
text2.pack(fill=BOTH,expand=1)
# test = Button(root, text="Click me!",
#               command=lambda root=root: root.test.configure(
#                   text="[%s]" % root.test['text']))
# test.pack()
# root.test = test

# 进入消息循环
root.mainloop()