# THIS CODE FOR PYTHON 2.0 VERSION

from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print 'Start :',tag
        for attr in attrs:
                print '->',' > '.join(map(str,attr))
    def handle_endtag(self, tag):
        print 'End   :',tag
    def handle_startendtag(self, tag, attrs):
        print 'Empty :',tag
        for attr in attrs:
                print '->',' > '.join(map(str,attr))

html = ""
for i in range(int(raw_input())):
    html += raw_input()


parser = MyHTMLParser()
parser.feed(html)
parser.close()
