# -*- coding: utf-8 -*-
from tkinter import *
from internetsystem import *
from operator import eq

WorksList = []

def Loading():
    global WorksList
    WorksList = getWorkData()
    pass

def main():
    Loading()
    UIloop()
    pass

def PrintAll():
    global WorksList
    for i in WorksList:
        i.printData()

def Search():
    global WorksList

    yowon = input("요원구분 입력(1:산업기능요원,2:전문연구요원)")
    salary = input("급여조건 입력(04:1400~1600만원,05:1600~1800만원,06:1800~2000만원)")
    location = input("근무지 시도 입력(ex>경기도)")

    for i in WorksList:
        if eq(i.data["yowonGbcd"],yowon) and eq(i.data["gyjogeonCd"],salary) and eq(i.data["geunmujysido"],location):
            i.printData()

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

    SearchButton = Button(topFrame, text = "검색", fg="red",command=Search)
    PrintButton = Button(topFrame, text = "전체출력", fg="red",command=PrintAll)

    #ailButton = Button(topFrame, text="메일", fg="red",command=sendMail)

    SearchButton.grid(row=1, column=1, columnspan=2)
    PrintButton.grid(row=2, column=1, columnspan=2)
    #MailButton.grid(row=3, column=1, columnspan=2)






    #####################################################################################################################
    root.mainloop()

#######################################################################################################################

main()
