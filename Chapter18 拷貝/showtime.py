#!/usr/bin/python
# L-18 MCS 260 : showtime.py
"""
Illustration of writing the current time on a web page.
On Unix, save this script in /var/www/cgi-bin
and execute pointing the browser to
dezon.math.uic.edu/cgi-bin/showtime.py
"""
print("Content-Type: text/html\n\n")
import time

def print_header(title):
    """
    prints the title of the web page
    """
    print("""
<html>
<head><title>%s</title></head>
<body>""" % title)

print_header("current date and time")
print(time.ctime(time.time()))
print("</body></html>")
