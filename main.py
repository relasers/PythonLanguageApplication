# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import font
from internetsystem import *
from operator import eq
import webbrowser
WorksList = []
def Loading():
    global WorksList
    print("데이터 갱신 중")
    WorksList = getWorkData()
    print("데이터 갱신 완료")
    pass

def PrintAll():
    global WorksList

    RenderText.delete(1.0, END)

    sort_key = sortVariable.get()

    if (sort_key == '1'):
        WorksList.sort(key=Workdata.Sort_byNum)
    if (sort_key == '2'):
        WorksList.sort(key=Workdata.Sort_byLocation)
    if (sort_key == '3'):
        WorksList.sort(key=Workdata.Sort_byClass)
    if (sort_key == '4'):
        WorksList.sort(key=Workdata.Sort_byMagamdate)

    for i in WorksList:
        RenderText.insert(INSERT, "채용번호::")
        RenderText.insert(INSERT, i.data["cygonggoNo"])
        RenderText.insert(INSERT, "\n")

        RenderText.insert(INSERT, "요원분류::")
        RenderText.insert(INSERT, i.data["yowonGbcdNm"])
        RenderText.insert(INSERT, ", 역종분류::")
        RenderText.insert(INSERT, i.data["yeokjongBrcdNm"])
        RenderText.insert(INSERT, "\n")

        RenderText.insert(INSERT, "최초발생일::")
        RenderText.insert(INSERT, i.data["ccdatabalsaengDtm"])
        RenderText.insert(INSERT, "( 최종변동일::")
        RenderText.insert(INSERT, i.data["cjdatabyeongyeongDtm"])
        RenderText.insert(INSERT, " )")
        RenderText.insert(INSERT, "\n")

        RenderText.insert(INSERT, "마감일::")
        RenderText.insert(INSERT, i.data["magamDt"])
        RenderText.insert(INSERT, "\n")

        RenderText.insert(INSERT, "업종::")
        RenderText.insert(INSERT, i.data["eopjongGbcdNm"])
        RenderText.insert(INSERT, "\n")

        RenderText.insert(INSERT, "경력 구분::")
        RenderText.insert(INSERT, i.data["gyeongryeokGbcdNm"])
        RenderText.insert(INSERT, "\n")

        RenderText.insert(INSERT, "학력 조건::")
        RenderText.insert(INSERT, i.data["cjhakryeok"])
        RenderText.insert(INSERT, "\n")

        RenderText.insert(INSERT, "담당 업무::")
        RenderText.insert(INSERT, i.data["ddeopmuNm"])
        RenderText.insert(INSERT, "\n")

        RenderText.insert(INSERT, "상세 내용::")
        RenderText.insert(INSERT, i.data["cyjemokNm"])
        RenderText.insert(INSERT, "\n")

        RenderText.insert(INSERT, "업체 이름::")
        RenderText.insert(INSERT, i.data["eopcheNm"])
        RenderText.insert(INSERT, "\n")

        RenderText.insert(INSERT, "대표 연락처::")
        RenderText.insert(INSERT, i.data["dpyeonrakcheoNo"])
        RenderText.insert(INSERT, "\n")

        RenderText.insert(INSERT, "업체 홈페이지 주소::")
        RenderText.insert(INSERT, i.data["hmpgAddr"])
        RenderText.insert(INSERT, "\n")

        RenderText.insert(INSERT, "담당자 이름::")
        RenderText.insert(INSERT, i.data["damdangjaFnm"])
        RenderText.insert(INSERT, "\n")

        RenderText.insert(INSERT, "담당자 연락처::")
        RenderText.insert(INSERT, i.data["ddjyeonrakcheoNo"])
        RenderText.insert(INSERT, "\n")

        RenderText.insert(INSERT, "주소::")
        RenderText.insert(INSERT, i.data["geunmujy"])
        RenderText.insert(INSERT, "\n")

        RenderText.insert(INSERT, "복지::")
        RenderText.insert(INSERT, i.data["bokrihs"])
        RenderText.insert(INSERT, "\n")

        RenderText.insert(INSERT, "접수방법::")
        RenderText.insert(INSERT, i.data["jeopsubb"])
        RenderText.insert(INSERT, "\n")

        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "///////////////////////////////////////////////////")
        RenderText.insert(INSERT, "\n")



def Search():
    global WorksList

    sort_key =  sortVariable.get()

    if(sort_key == '1'):
        WorksList.sort(key=Workdata.Sort_byNum)
    if (sort_key == '2'):
        WorksList.sort(key=Workdata.Sort_byLocation)
    if (sort_key == '3'):
        WorksList.sort(key=Workdata.Sort_byClass)
    if (sort_key == '4'):
        WorksList.sort(key=Workdata.Sort_byMagamdate)



    yowon = yowonVariable.get()
    salary = e_salary_lbox.get(ACTIVE)
    location = e_location.get()

    dataexist = False

    RenderText.delete(1.0, END)

    for i in WorksList:
        if eq(i.data["yowonGbcd"],yowon) and eq(i.data["gyjogeonCdNm"],salary) and i.data["geunmujy"].find(location) != -1 :

            dataexist = True

            RenderText.insert(INSERT, "채용번호::")
            RenderText.insert(INSERT, i.data["cygonggoNo"])
            RenderText.insert(INSERT, "\n")

            RenderText.insert(INSERT,"요원분류::")
            RenderText.insert(INSERT, i.data["yowonGbcdNm"])
            RenderText.insert(INSERT, ", 역종분류::")
            RenderText.insert(INSERT, i.data["yeokjongBrcdNm"])
            RenderText.insert(INSERT, "\n")

            RenderText.insert(INSERT, "최초발생일::")
            RenderText.insert(INSERT, i.data["ccdatabalsaengDtm"])
            RenderText.insert(INSERT, "( 최종변동일::")
            RenderText.insert(INSERT, i.data["cjdatabyeongyeongDtm"])
            RenderText.insert(INSERT, " )")
            RenderText.insert(INSERT, "\n")

            RenderText.insert(INSERT, "마감일::")
            RenderText.insert(INSERT, i.data["magamDt"])
            RenderText.insert(INSERT, "\n")


            RenderText.insert(INSERT, "업종::")
            RenderText.insert(INSERT, i.data["eopjongGbcdNm"])
            RenderText.insert(INSERT, "\n")

            RenderText.insert(INSERT, "경력 구분::")
            RenderText.insert(INSERT, i.data["gyeongryeokGbcdNm"])
            RenderText.insert(INSERT, "\n")

            RenderText.insert(INSERT, "학력 조건::")
            RenderText.insert(INSERT, i.data["cjhakryeok"])
            RenderText.insert(INSERT, "\n")

            RenderText.insert(INSERT, "담당 업무::")
            RenderText.insert(INSERT, i.data["ddeopmuNm"])
            RenderText.insert(INSERT, "\n")

            RenderText.insert(INSERT, "상세 내용::")
            RenderText.insert(INSERT, i.data["cyjemokNm"])
            RenderText.insert(INSERT, "\n")

            RenderText.insert(INSERT, "업체 이름::")
            RenderText.insert(INSERT, i.data["eopcheNm"])
            RenderText.insert(INSERT, "\n")

            RenderText.insert(INSERT, "대표 연락처::")
            RenderText.insert(INSERT, i.data["dpyeonrakcheoNo"])
            RenderText.insert(INSERT, "\n")

            RenderText.insert(INSERT, "업체 홈페이지 주소::")
            RenderText.insert(INSERT, i.data["hmpgAddr"])
            RenderText.insert(INSERT, "\n")

            RenderText.insert(INSERT, "담당자 이름::")
            RenderText.insert(INSERT, i.data["damdangjaFnm"])
            RenderText.insert(INSERT, "\n")

            RenderText.insert(INSERT, "담당자 연락처::")
            RenderText.insert(INSERT, i.data["ddjyeonrakcheoNo"])
            RenderText.insert(INSERT, "\n")

            RenderText.insert(INSERT, "주소::")
            RenderText.insert(INSERT, i.data["geunmujy"])
            RenderText.insert(INSERT, "\n")

            RenderText.insert(INSERT, "복지::")
            RenderText.insert(INSERT, i.data["bokrihs"])
            RenderText.insert(INSERT, "\n")

            RenderText.insert(INSERT, "접수방법::")
            RenderText.insert(INSERT, i.data["jeopsubb"])
            RenderText.insert(INSERT, "\n")

            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "///////////////////////////////////////////////////")
            RenderText.insert(INSERT, "\n")

    if dataexist is False:
        RenderText.insert(INSERT, "조건에 해당하는 일터 없음")
        RenderText.insert(INSERT, "\n")








Loading()
#########################################################################################################################
root = Tk()
root.geometry('640x720+400+400')
theLabel = Label(root, text= "Alternative Military Service")
theLabel.pack()

topFrame = Frame(root)
topFrame.pack()
RenderFrame = Frame(root)
RenderFrame.pack()
buttonFrame = Frame(root)
buttonFrame.pack()

RefreshButton = Button(buttonFrame, text="갱신", fg="red",command=Loading)
SearchButton = Button(buttonFrame, text = "검색", fg="red",command=Search)
PrintButton = Button(buttonFrame, text = "전체출력", fg="red",command=PrintAll)
QuitButton = Button(buttonFrame, text = "종료", fg="red",command=exit)
#ailButton = Button(topFrame, text="메일", fg="red",command=sendMail)

RefreshButton.grid(row=0, column=0)
SearchButton.grid(row=0, column=1)
PrintButton.grid(row=0, column=2)
QuitButton.grid(row=0, column=3)

#MailButton.grid(row=3, column=1, columnspan=2)

l1 = Label(topFrame, text="요원구분")
l2 = Label(topFrame, text="급여조건")
l3 = Label(topFrame, text="근무지")
l1.grid(row=1, column=0)
l2.grid(row=2, column=0)
l3.grid(row=3, column=0)
################################################################################################
yowonVariable = StringVar()
yowonVariable.initialize('1')
e_yowon_1= Radiobutton(topFrame, text="산업기능요원", variable=yowonVariable, value='1')
e_yowon_2 = Radiobutton(topFrame, text="전문연구요원", variable=yowonVariable, value='2')

e_salary_sbar = Scrollbar(topFrame)
e_salary_sbar.grid(row = 2, column = 2)
TempFont = font.Font(topFrame, size=15, weight='bold', family='Consolas')
e_salary_lbox = Listbox(topFrame, font=TempFont, activestyle='none',
width=10, height=1, borderwidth=12, relief='ridge',
                        yscrollcommand=e_salary_sbar.set)

e_salary_lbox.insert(1,"1000~1200만원")
e_salary_lbox.insert(2,"1200~1400만원")
e_salary_lbox.insert(3,"1400~1600만원")
e_salary_lbox.insert(4,"1600~1800만원")
e_salary_lbox.insert(5,"1800~2000만원")
e_salary_lbox.insert(6,"2000~2200만원")
e_salary_lbox.insert(7,"2200~2400만원")
e_salary_lbox.insert(8,"2400~2600만원")
e_salary_lbox.insert(9,"2600~2800만원")
e_salary_lbox.insert(10,"2800~3000만원")
e_salary_lbox.insert(11,"3000~3200만원")
e_salary_lbox.insert(12,"3200~3400만원")

e_location = Entry(topFrame)
###################################################################################################
sortVariable = StringVar()
sortVariable.initialize('1')

e_sort_number= Radiobutton(topFrame, text="채용번호별 정렬", variable=sortVariable, value='1')
e_sort_area= Radiobutton(topFrame, text="지역별 정렬", variable=sortVariable, value='2')
e_sort_upjong = Radiobutton(topFrame, text="업종별 정렬", variable=sortVariable, value='3')
e_sort_magam = Radiobutton(topFrame, text="마감별 정렬", variable=sortVariable, value='4')
####################################################################################################################
e_yowon_1.grid(row = 1, column = 1)
e_yowon_2.grid(row = 1, column = 2)

e_salary_lbox.grid(row=2,column=1)
e_location.grid(row=3, column=1)

e_sort_number.grid(row = 4, column = 1)
e_sort_area.grid(row = 4, column = 2)
e_sort_upjong.grid(row = 4, column = 3)
e_sort_magam.grid(row = 4, column = 4)
#################################################################################################################

RenderTextScrollbar = Scrollbar(RenderFrame)
RenderTextScrollbar.grid(row=0, column=1)

TempFont = font.Font(RenderFrame, size=10, family='Consolas')
RenderText = Text(RenderFrame, width=80, height=40, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
RenderText.grid(row=0, column=0)
RenderTextScrollbar.config(command=RenderText.yview)



#####################################################################################################################
root.mainloop()

#######################################################################################################################
