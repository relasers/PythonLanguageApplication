from tkinter import *
from internetsystem import *

def Loading():
    LoadXMLFromFile()
    getWorkData()
    pass

def main():
    Loading()


    UIloop()
    pass

def UIloop():
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
    MailButton = Button(topFrame, text="메일", fg="red",command=sendMail)

    SearchButton.grid(row=1, column=1, columnspan=2)
    SortButton.grid(row=2, column=1, columnspan=2)
    MailButton.grid(row=3, column=1, columnspan=2)






    #####################################################################################################################
    root.mainloop()

#######################################################################################################################

main()
