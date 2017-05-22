# -*- coding: cp949 -*-
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree

##### global
xmlFD = -1
WorksDoc = None

### xml ���� �Լ� ����
def LoadXMLFromFile():
    fileName = "work.xml"
    global xmlFD, WorksDoc
    try:
        xmlFD = open(fileName)
    except IOError:
        print ("invalid file name or path")
    else:
        try:
            dom = parse(xmlFD)
        except Exception:
            print ("loading fail!!!")
        else:
            print ("XML Document loading complete")
            WorksDoc = dom
            return dom
    return None


def WorksFree():
    if checkDocument():
        WorksDoc.unlink()


def AddWork(workdata):
    global WorksDoc
    if not checkDocument():
        return None

    # book ������Ʈ ����
    newWork = WorksDoc.createElement('work')
    newWork.setAttribute('ISBN', workdata['ISBN'])

    # Title ������Ʈ ����
    titleEle = WorksDoc.createElement('title')
    # �ؽ�Ʈ ��� ����
    titleNode = WorksDoc.createTextNode(workdata['title'])
    # �ؽ�Ʈ ��带 Title ������Ʈ�� ����
    try:
        titleEle.appendChild(titleNode)
    except Exception:
        print("append child fail- please,check the parent element & node!!!")
        return None
    else:
        titleEle.appendChild(titleNode)

    # Title ������Ʈ�� Book ������Ʈ�� ����.
    try:
        newWork.appendChild(titleEle)
        worklist = WorksDoc.firstChild
    except Exception:
        print("append child fail- please,check the parent element & node!!!")
        return None
    else:
        if worklist != None:
            worklist.appendChild(newWork)



def PrintDOMtoXML():
    if checkDocument():
        print(WorksDoc.toxml())


def PrintWorkList(tags):
    global WorksDoc
    if not checkDocument():
        return None

    worklist = WorksDoc.childNodes
    work = worklist[0].childNodes
    for item in work:
        if item.nodeName == "book":
            subitems = item.childNodes
            for atom in subitems:
                if atom.nodeName in tags:
                    print("title=", atom.firstChild.nodeValue)


def printWorkList(blist):
    for res in blist:
        print (res)

def checkDocument():
    global WorksDoc
    if WorksDoc == None:
        print("Error : Document is empty")
        return False
    return True
