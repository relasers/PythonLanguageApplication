
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
    """retrieve a map (image) from the static google maps server

     See: http://code.google.com/apis/maps/documentation/staticmaps/

        Creates a request string with a URL like this:
        http://maps.google.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=14&size=512x512&maptype=roadmap
&markers=color:blue|label:S|40.702147,-74.015794&sensor=false"""


    # assemble the URL

    url = "http://maps.google.com/maps/api/staticmap?"  # base URL, append query params, separated by &

    # if center and zoom  are not given, the map will show all marker locations
    if center != None:
        url += "center=%s&" % center
        # request += "center=%s&" % "40.714728, -73.998672"   # latitude and longitude (up to 6-digits)
        # request += "center=%s&" % "50011" # could also be a zipcode,
        # request += "center=%s&" % "Brooklyn+Bridge,New+York,NY"  # or a search term
    if center != None:
        url += "zoom=%s&" % zoom  # zoom 0 (all of the world scale ) to 22 (single buildings scale)

    url += "size=%s&" % (imgsize)  # tuple of ints, up to 640 by 640
    url += "format=%s&" % imgformat
    url += "maptype=%s&" % maptype  # roadmap, satellite, hybrid, terrain


    url += "sensor=false&"  # must be given, deals with getting loction from mobile device
    print(url)

    mapconn.request("GET", url)

    req = mapconn.getresponse()

    print(req.status)
    if int(req.status) == 200:
        imgdata = StringIO(req.read())

        try:
            PIL_img = Image.open(imgdata)
            # if this cannot be read as image that, it's probably an error from the server,
        except IOError:
            print("IOError:")
            imgdata.read()
            # print error (or it may return a image showing the error"
        else:
            PIL_img.show()
            # PIL_img.save(filename_wo_extension+".jpg", "JPEG") # save as jpeg




marker_list = []
marker_list.append("markers=color:blue|label:S|11211|11206|11222")  # blue S at several zip code's centers
marker_list.append("markers=size:tiny|label:B|color:0xFFFF00|40.702147,-74.015794|")  # tiny yellow B at lat/long
marker_list.append(
    "markers=size:mid|color:red|label:6|Brooklyn+Bridge,New+York,NY")  # mid-sized red 6 at search location
# see http://code.google.com/apis/maps/documentation/staticmaps/#Markers


# make a map around a center
get_static_google_map("google_map_example1", center="(주)한국비전기술", zoom=12, imgsize="500x500",
                      imgformat="jpg", maptype="terrain")

