from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.max_depth = 0
        self.depth = 0

    def handle_starttag(self, tag, attrs):
        self.depth += 1
        if self.depth > self.max_depth:
            self.max_depth = self.depth
            self.tags = [tag]
        elif self.depth == self.max_depth and tag not in self.tags:
            self.tags.append(tag)

    def handle_endtag(self, tag):
        self.depth -= 1

def solution(document):
    parser = MyHTMLParser()
    parser.feed(document)
    return sorted(parser.tags)
