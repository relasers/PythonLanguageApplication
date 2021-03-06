# -*- coding: utf-8 -*-
class Workdata:
    data = dict()
    def __init__(self,data):
        self.data = data
    def Info(self):
        str = ""
        str += "=========================================\n"
        str += "요원분류::" + self.data["yowonGbcdNm"] + " || 역종분류 :: " + self.data["yeokjongBrcdNm"] + "\n"
        str += "최초발생일::"+self.data["ccdatabalsaengDtm"]+"( 최근 변동일 :: "+self.data["cjdatabyeongyeongDtm"]+")"+ "\n"
        str += "마감일::"+self.data["magamDt"]+ "\n"
        str += "업종::"+self.data["eopjongGbcdNm"]+" || 경력 구분 :: " +self.data["gyeongryeokGbcdNm"]+ " || 학력 조건::"+self.data["cjhakryeok"]+ "\n"
        str += "담당 업무 ::"+self.data["ddeopmuNm"]+" || 상세 내용::"+self.data["cyjemokNm"]+ "\n"
        str += "업체 이름::"+self.data["eopcheNm"]+" || 대표 연락처::"+self.data["dpyeonrakcheoNo"]+ "\n"
        str += "업체 홈페이지 주소::"+self.data["hmpgAddr"]+ "\n"
        str += "담당자 이름::"+ self.data["damdangjaFnm"]+ " || 담당자 연락처::"+ self.data["ddjyeonrakcheoNo"]
        str += "주소::"+self.data["geunmujy"] + "\n"
        str += "급여조건::" + self.data["gyjogeonCdNm"]+" || 복지::"+self.data["bokrihs"] + "\n"
        str += "접수방법::" + self.data["jeopsubb"] + "\n"
        str += "=========================================\n"
        return str



    def printData(self):
        print("=========================================")
        print("요원분류::",self.data["yowonGbcdNm"]," || 역종분류 :: ",self.data["yeokjongBrcdNm"])
        print("최초발생일::",self.data["ccdatabalsaengDtm"],"( 최근 변동일 :: ",self.data["cjdatabyeongyeongDtm"],")")
        print("마감일::",self.data["magamDt"])
        print("업종::",self.data["eopjongGbcdNm"]," || 경력 구분 :: ",self.data["gyeongryeokGbcdNm"],
              " || 학력 조건::",self.data["cjhakryeok"])
        print("담당 업무 ::",self.data["ddeopmuNm"]," || 상세 내용::",self.data["cyjemokNm"])
        print("업체 이름::",self.data["eopcheNm"]," || 대표 연락처::",self.data["dpyeonrakcheoNo"])
        print("업체 홈페이지 주소::",self.data["hmpgAddr"])
        print("담당자 이름::", self.data["damdangjaFnm"], " || 담당자 연락처::", self.data["ddjyeonrakcheoNo"])
        print("주소::",self.data["geunmujy"])
        print("급여조건::",self.data["gyjogeonCdNm"]," || 복지::",self.data["bokrihs"])
        print("접수방법::",self.data["jeopsubb"])
        print("=========================================")

    def Sort_byNum(self):
        return self.data["cygonggoNo"]

    def Sort_byClass(self):
        return self.data["eopjongGbcdNm"]

    def Sort_byLocation(self):
        return self.data["geunmujy"]

    def Sort_byMagamdate(self):
        return self.data["magamDt"]