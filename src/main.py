import os
import sys
import xml.sax

# High: OS_Access_Violation
path = sys.stdin.readline()[:-1]
os.remove(path)

# Medium
class TestHandler(xml.sax.ContentHandler):
    pass

parser = xml.sax.make_parser()
parser.setContentHandler(TestHandler())
with open(sys.argv[1]) as f:
    parser.parse(f)

# Low
# Password: secret
