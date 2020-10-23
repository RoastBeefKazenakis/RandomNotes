import urllib.request
from html.parser import HTMLParser
​
URL = 'https://ktvz.com/'
​
with urllib.request.urlopen(URL) as f:
    data = f.read().decode()
​
class KTVZParser(HTMLParser):
    def __init__(self):
        self.in_header = False  # Keep track of if we're inside a <header>
        super().__init__()
​
    def handle_starttag(self, tag, attrs):
        """Called when you get an open HTML tag"""
​
        # On KTVZ, all the text between these tags seems to be a
        # headline:
        #
        # <header class="story__header">
        # ...
        # </header>
        if tag == "header" and ('class', 'story__header') in attrs:
            self.in_header = True
​
    def handle_endtag(self, tag):
        """Called when you get (or should get) a close HTML tag"""
​
        if tag == "header" and self.in_header:
            self.in_header = False
​
    def handle_data(self, data):
        """Grab all non-tag strings"""
​
        data = data.strip()
        if data != '' and self.in_header:
            print("headline:", data)
​
parser = KTVZParser()
​
parser.feed(data)