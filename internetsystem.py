import urllib
from xmlobject import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer


##global
conn = None
regKey = 'uLFxldxGrljnNH%2BO8YO3TNTKnn%2Bb02H6WjbZavryiNNMASW31SXrJuGSTKOyU0PZtnZInjjOWuN8UUA%2BiLs7%2FQ%3D%3D'

# 다음 OpenAPI 접속 정보 information
server = "apis.data.go.kr"

# smtp 정보
host = "smtp.gmail.com"  # Gmail SMTP 서버 주소.
port = "587"

def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)

def userURIBuilder(server, **user):
    str = "http://" + server + "/1300000/CyJeongBo/list" + "?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str

def getWorkData():
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()
    uri = userURIBuilder(server, numOfRows="999", pageNo="1", ServiceKey=regKey)
    conn.request("GET", uri)

    req = conn.getresponse()
    print(req.status)
    if int(req.status) == 200:
        print("Book data downloading complete!")
        return extractWorkData(req.read().decode('utf-8'))
    else:
        print("OpenAPI request has been failed!! please retry")
        return None

def extractWorkData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    print(strXml)
    # 일터 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("item")  # return list type
    print(itemElements)

def sendMail():
    global host, port
    html = ""
    title = str(input('Title :'))
    senderAddr = str(input('sender email address :'))
    recipientAddr = str(input('recipient email address :'))
    msgtext = str(input('write message :'))
    passwd = str(input(' input your password of gmail account :'))

    #msgtext = str(input('Do you want to include book data (y/n):'))
    #if msgtext == 'y':
    #    keyword = str(input('input keyword to search:'))
    #    html = MakeHtmlDoc(SearchBookTitle(keyword))

    import smtplib
    # MIMEMultipart의 MIME을 생성합니다.
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # Message container를 생성합니다.
    msg = MIMEMultipart('alternative')

    # set message
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    msgPart = MIMEText(msgtext, 'plain')
    bookPart = MIMEText(html, 'html', _charset='UTF-8')

    # 메세지에 생성한 MIME 문서를 첨부합니다.
    msg.attach(msgPart)
    msg.attach(bookPart)

    print("connect smtp server ... ")
    s = smtplib.SMTP(host, port)
    # s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)  # 로그인을 합니다.
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

    print("Mail sending complete!!!")



def checkConnection():
    global conn
    if conn == None:
        print("Error : connection is fail")
        return False
    return True

