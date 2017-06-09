
from urllib import request
from urllib import parse
from urllib import response

from data import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
from xml.dom import pulldom
import Image

## String IO 임포트 실패시
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

mapconn = None

def get_static_google_map(filename_wo_extension, center=None, zoom=None, imgsize="500x500", imgformat="jpeg",
                          maptype="roadmap", markers=None):

    # assemble the URL

    url = "http://maps.google.com/maps/api/staticmap?"  # base URL, append query params, separated by &

    # if center and zoom  are not given, the map will show all marker locations
    if center != None:
        url += "center=%s&" % center

    if center != None:
        url += "zoom=%s&" % zoom  # zoom 0 (all of the world scale ) to 22 (single buildings scale)

    url += "size=%s&" % (imgsize)
    url += "format=%s&" % imgformat
    url += "maptype=%s&" % maptype


    url += "sensor=false&"
    print(url)

    mapconn.request("GET", url)

    req = mapconn.getresponse()

    print(req.status)
    if int(req.status) == 200:
        imgdata = StringIO(req.read())

        try:
            PIL_img = Image.open(imgdata)
        except IOError:
            print("IOError:")
            imgdata.read()
        else:
            PIL_img.show()




marker_list = []
marker_list.append("markers=color:blue|label:S|11211|11206|11222")  # blue S at several zip code's centers
marker_list.append("markers=size:tiny|label:B|color:0xFFFF00|40.702147,-74.015794|")  # tiny yellow B at lat/long
marker_list.append( "markers=size:mid|color:red|label:6|Brooklyn+Bridge,New+York,NY")


# make a map around a center
get_static_google_map("google_map_example1", center="(주)한국비전기술", zoom=12, imgsize="500x500",
                      imgformat="jpg", maptype="terrain")

