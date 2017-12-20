#!/usr/bin/python
#
# Options:
#
# -a active
# -a accepted
# -a handled
# -a requests
# -a reading
# -a writing
# -a waiting
#


import sys
import getopt
import urllib2
import re
import ssl


def usage():
    print "usage: nginx-stat.py -h 127.0.0.1 -p 80 -a [active|accepted|handled|request|reading|writing|waiting]"
    sys.exit(2)


def main():

    # Default values
    host = "localhost"
    port = "80"
    getInfo = "None"
    proto = "http"
    _headers = {}
    gcontext = ""


    if len(sys.argv) < 2:
        usage()

    try:
        opts, _ = getopt.getopt(sys.argv[1:], "h:p:a:")
    except getopt.GetoptError:
        usage()

    # Assign parameters as variables
    for opt, arg in opts:
        if opt == "-h":
            host = arg
        if opt == "-p":
            port = arg
        if opt == "-a":
            getInfo = arg

    if port == "443":
        proto = "https"
        _headers = {'X-Mashape-Key': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
        gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

    url = proto + "://" + host + ":" + port + "/nginx_status/"
    request = urllib2.Request(url, headers=_headers)
    result = urllib2.urlopen(request, context=gcontext)

    buffer = re.findall(r'\d{1,8}', result.read())

## Format:
## Active connections: 196
## server accepts handled requests
## 272900 272900 328835
## Reading: 0 Writing: 6 Waiting: 190

    if getInfo == "active":
        print buffer[0]
    elif getInfo == "accepted":
        print buffer[1]
    elif getInfo == "handled":
        print buffer[2]
    elif getInfo == "requests":
        print buffer[3]
    elif getInfo == "reading":
        print buffer[4]
    elif getInfo == "writing":
        print buffer[5]
    elif getInfo == "waiting":
        print buffer[6]
    else:
        print "unknown"
        sys.exit(1)

if __name__ == "__main__":
    main()
