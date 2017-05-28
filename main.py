# -*- coding: utf-8 -*-
from tkinter import *
from internetsystem import *
from operator import eq
from datetime import datetime

WorksList = []

def Loading():
    global WorksList
    print("데이터 갱신 중")
    WorksList = getWorkData()
    print("데이터 갱신 완료")
    pass

def main():
    Loading()
    UIloop()
    pass

def PrintAll():
    global WorksList

    WorksList.sort(key=Workdata.SortKey)

    for i in WorksList:
        i.printData()



def Search():
    global WorksList

    WorksList.sort(key=Workdata.SortKey)

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

    RefreshButton = Button(topFrame, text="갱신", fg="red",command=Loading)
    SearchButton = Button(topFrame, text = "검색", fg="red",command=Search)
    PrintButton = Button(topFrame, text = "전체출력", fg="red",command=PrintAll)
    QuitButton = Button(topFrame, text = "종료", fg="red",command=exit)
    #ailButton = Button(topFrame, text="메일", fg="red",command=sendMail)

    RefreshButton.grid(row=1, column=1, columnspan=2)
    SearchButton.grid(row=2, column=1, columnspan=2)
    PrintButton.grid(row=3, column=1, columnspan=2)
    QuitButton.grid(row=4, column=1, columnspan=2)

    #MailButton.grid(row=3, column=1, columnspan=2)






    #####################################################################################################################
    root.mainloop()

#######################################################################################################################

main()
