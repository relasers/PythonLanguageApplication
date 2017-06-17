# -*- coding: utf-8 -*-

import urllib
import spam
from urllib import request
from urllib.parse import urlencode, quote_plus
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

"""

https://maps.googleapis.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=13&size=600x300&maptype=roadmap
&markers=color:blue%7Clabel:S%7C40.702147,-74.015794&markers=color:green%7Clabel:G%7C40.711614,-74.012318
&markers=color:red%7Clabel:C%7C40.718217,-73.998284
&key=AIzaSyB224CCz7VW6IdntURnia5g4xL_CuJeLPA

"""
key = "AIzaSyB224CCz7VW6IdntURnia5g4xL_CuJeLPA"

server = "maps.google.com"
mapconn = None

def connectOpenAPIServer():
    global mapconn, server
    mapconn = HTTPConnection(server)

def GetGoogleMap(filename_wo_extension, center=None, zoom=None, imgsize="500x500", imgformat="jpeg",
                          maptype="roadmap", markers=None):
    global server
    if mapconn == None:
        connectOpenAPIServer()

    url = u"http://maps.google.com/maps/api/staticmap?"
    if center != None:
        url += "center=%s&" % center
    if center != None:
        url += "zoom=%s&" % zoom
    url += "size=%s&" % (imgsize)
    url += "format=%s&" % imgformat
    url += "maptype=%s&" % maptype

    url += "sensor=false&"

    if markers != None:
        for marker in markers:
            url += "%s&" % marker

    url += "key=%s" % key

    print(   urllib.request.quote(url.encode("utf-8"), '?=+,&/:' )  )

    urllib.request.quote(url.encode("utf-8"), '/:' )

    mapconn.request("GET",  urllib.request.quote(url.encode("utf-8"), '?=+,&/:' )   )

    req = mapconn.getresponse()

    print(req.status)
    if int(req.status) == 200:
        urllib.request.urlretrieve(   urllib.request.quote(url.encode("utf-8"), '?=+,&/:' )     , filename_wo_extension + "." + imgformat)

    mapconn.close()


"""
marker_list = []
marker_list.append( "markers=size:large|color:red|label:1|(주)한국비전기술")

get_static_google_map("parsedmap", center="(주)한국비전기술", zoom=12, imgsize="360x440",
                      imgformat="gif", maptype="roadmap", markers= marker_list )

"""

