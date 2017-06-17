# -*- coding: utf-8 -*-
import urllib
from data import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request
import urllib.parse
from xml.dom import pulldom
import pickle
import spam

##global
conn = None
regKey = 'uLFxldxGrljnNH%2BO8YO3TNTKnn%2Bb02H6WjbZavryiNNMASW31SXrJuGSTKOyU0PZtnZInjjOWuN8UUA%2BiLs7%2FQ%3D%3D'
mapKey = 'AIzaSyB224CCz7VW6IdntURnia5g4xL_CuJeLPA'

server = "apis.data.go.kr"

# smtp 정보
host = "smtp.gmail.com"
port = "587"

def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)

def userURIBuilder(server, **user):
    str = spam.string_merger(["http://",server,"/1300000/CyJeongBo/list","?"])

    for key in user.keys():
        str = spam.string_merger([str, key, "=", user[key], "&"])
    return str

def getWorkData():
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()
    url = userURIBuilder(server, numOfRows="999", pageNo="1", ServiceKey=regKey)
    conn.request("GET", url)

    req = conn.getresponse()
    worklist = []

    print(req.status)
    if int(req.status) == 200:

###################################<데이터 추출 단계>#####################################################################
        print("Connect Complete")

        from xml.etree import ElementTree
        tree = ElementTree.fromstring(req.read())

        itemElements = tree.getiterator("item")  # return list type

        for item in itemElements:
            bokrihs                 = item.find("bokrihs")              # 복리 후생
            ccdatabalsaengDtm       = item.find("ccdatabalsaengDtm")    # 최초 발생일
            cjdatabyeongyeongDtm    = item.find("cjdatabyeongyeongDtm") # 최근 변동일
            cjhakryeok              = item.find("cjhakryeok")           # 학력 조건
            cygonggoNo              = item.find("cygonggoNo")           # 채용 번호
            cyjemokNm               = item.find("cyjemokNm")            # 채용 제목
            damdangjaFnm            = item.find("damdangjaFnm")         # 담당자 이름
            ddeopmuNm               = item.find("ddeopmuNm")            # 담당 업무
            ddjyeonrakcheoNo        = item.find("ddjyeonrakcheoNo")     # 담당자 연락처
            dpyeonrakcheoNo         = item.find("dpyeonrakcheoNo")      # 대표 연락처
            eopcheNm                = item.find("eopcheNm")             # 업체 이름
            hmpgAddr                = item.find("hmpgAddr")             # 업체 홈페이지 주소
            eopjongGbcd             = item.find("eopjongGbcd")          # 업종 구분 코드
            eopjongGbcdNm           = item.find("eopjongGbcdNm")        # 업종 구분 명
            geunmujy                = item.find("geunmujy")             # 근무지 주소
            geunmujysido            = item.find("geunmujysido")         # 근무지 동
            gmjybjusoCd             = item.find("gmjybjusoCd")          # 근무지 법정동 코드
            gyeongryeokGbcdNm       = item.find("gyeongryeokGbcdNm")    # 경력 구분
            gyjogeonCd              = item.find("gyjogeonCd")           # 급여 조건 코드
            gyjogeonCdNm            = item.find("gyjogeonCdNm")         # 급여 조건 명
            jeopsubb                = item.find("jeopsubb")             # 접수 방법
            magamDt                 = item.find("magamDt")              # 마감 일자
            sschaeyongYn            = item.find("sschaeyongYn")         # 상시 채용 여부
            yeokjongBrcd            = item.find("yeokjongBrcd")         # 역종 분류 코드
            yeokjongBrcdNm          = item.find("yeokjongBrcdNm")       # 역종 분류 명
            yowonGbcd               = item.find("yowonGbcd")            # 요원 구분 코드
            yowonGbcdNm             = item.find("yowonGbcdNm")          # 요원 구분 명
            yuhyoYn                 = item.find("yuhyoYn")              # 유효 여부


            workdata = dict()

            if len(cygonggoNo.text) > 0:
                try:
                    workdata["bokrihs"]                 = bokrihs.text
                except Exception:
                    workdata["bokrihs"] = "없음"
                try:
                    workdata["ccdatabalsaengDtm"]       = ccdatabalsaengDtm.text
                except Exception:
                    workdata["ccdatabalsaengDtm"] ="없음"
                try:
                    workdata["cjdatabyeongyeongDtm"]    = cjdatabyeongyeongDtm.text
                except Exception:
                    workdata["cjdatabyeongyeongDtm"] = "없음"
                try:
                    workdata["cjhakryeok"]              = cjhakryeok.text
                except Exception:
                    workdata["cjhakryeok"] = "없음"
                try:
                    workdata["cygonggoNo"]              = cygonggoNo.text
                except Exception:
                    workdata["cygonggoNo"] = "없음"
                try:
                    workdata["cyjemokNm"]               = cyjemokNm.text
                except Exception:
                    workdata["cyjemokNm"] = "없음"
                try:
                    workdata["damdangjaFnm"]            = damdangjaFnm.text
                except Exception:
                    workdata["damdangjaFnm"] = "없음"
                try:
                    workdata["ddeopmuNm"]               = ddeopmuNm.text
                except Exception:
                    workdata["ddeopmuNm"] = "없음"

                try:
                    workdata["ddjyeonrakcheoNo"]        = ddjyeonrakcheoNo.text
                except Exception:
                    workdata["ddjyeonrakcheoNo"] = "없음"

                try:
                    workdata["dpyeonrakcheoNo"]         = dpyeonrakcheoNo.text
                except Exception:
                    workdata["dpyeonrakcheoNo"] = "없음"
                try:
                    workdata["eopcheNm"]                = eopcheNm.text
                except Exception:
                    workdata["eopcheNm"] ="없음"
                try:
                    workdata["hmpgAddr"]                = hmpgAddr.text
                except Exception:
                    workdata["hmpgAddr"] = "없음"
                try:
                    workdata["eopjongGbcd"]             = eopjongGbcd.text
                except Exception:
                    workdata["eopjongGbcd"] = "없음"
                try:
                    workdata["eopjongGbcdNm"]           = eopjongGbcdNm.text
                except Exception:
                    workdata["eopjongGbcdNm"] = "없음"
                try:
                    workdata["geunmujy"]                = geunmujy.text
                except Exception:
                    workdata["geunmujy"] ="없음"
                try:
                    workdata["geunmujysido"]            = geunmujysido.text
                except Exception:
                    workdata["geunmujysido"] =  "없음"
                try:
                    workdata["gmjybjusoCd"]             = gmjybjusoCd.text
                except Exception:
                    workdata["gmjybjusoCd"] =  "없음"
                try:
                    workdata["gyeongryeokGbcdNm"]       = gyeongryeokGbcdNm.text
                except Exception:
                    workdata["gyeongryeokGbcdNm"] =  "없음"
                try:
                    workdata["gyjogeonCd"]              = gyjogeonCd.text
                except Exception:
                    workdata["gyjogeonCd"] =  "없음"
                try:
                    workdata["gyjogeonCdNm"]            = gyjogeonCdNm.text
                except Exception:
                    workdata["gyjogeonCdNm"] =  "없음"
                try:
                    workdata["jeopsubb"]                = jeopsubb.text
                except Exception:
                    workdata["jeopsubb"] = "없음"
                try:
                    workdata["magamDt"]                 = magamDt.text
                except Exception:
                    workdata["magamDt"] =  "없음"
                try:
                    workdata["sschaeyongYn"]            = sschaeyongYn.text
                except Exception:
                    workdata["sschaeyongYn"] = "없음"
                try:
                    workdata["yeokjongBrcd"]            = yeokjongBrcd.text
                except Exception:
                    workdata["yeokjongBrcd"] = "없음"
                try:
                    workdata["yeokjongBrcdNm"]          = yeokjongBrcdNm.text
                except Exception:
                    workdata["yeokjongBrcdNm"] = "없음"
                try:
                    workdata["yowonGbcd"]               = yowonGbcd.text
                except Exception:
                    workdata["yowonGbcd"] = "없음"
                try:
                    workdata["yowonGbcdNm"]             = yowonGbcdNm.text
                except Exception:
                    workdata["yowonGbcdNm"] = "없음"
                try:
                    workdata["yuhyoYn"]                 = yuhyoYn.text
                except Exception:
                    workdata["yuhyoYn"] = "없음"

                OverlappedData = False
                for i in worklist:
                    if i == workdata:
                        OverlappedData = True
                        break

                if OverlappedData is False:
                    worklist.append(Workdata(workdata))

        f = open("data.txt", 'wb')
        pickle.dump(worklist, f)
        f.close()

        conn.close()
        return worklist
#######################################################################################################################
    else:
        print("OpenAPI request has been failed!! please retry")
        return None



def checkConnection():
    global conn
    if conn == None:
        print("Error : connection is fail")
        return False
    return True

