from tkinter import *
import xml


#########################################################################################################################
root = Tk()
root.geometry('640x480+200+200')
theLabel = Label(root, text= "Alternative Military Service")
theLabel.pack()

topFrame = Frame(root)
topFrame.pack()
buttonFrame = Frame(root)
buttonFrame.pack(side=LEFT)

SearchButton = Button(topFrame, text = "검색", fg="red")
SortButton = Button(topFrame, text = "정렬", fg="red")




#SearchButton.pack()
#SortButton.pack()
SearchButton.grid(row=1, column=1, columnspan=2)
SortButton.grid(row=2, column=1, columnspan=2)
#SearchButton.place(x=0, y=0)
#SortButton.place(x=0, y=100)






#####################################################################################################################
root.mainloop()