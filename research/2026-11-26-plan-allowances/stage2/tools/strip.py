import sys, re, html
from html.parser import HTMLParser

class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1
        if tag in ('tr', 'p', 'h1', 'h2', 'h3', 'h4', 'li', 'table', 'br', 'div'):
            self.out.append('\n')
        if tag in ('td', 'th'):
            self.out.append(' | ')
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip -= 1
    def handle_data(self, d):
        if not self.skip:
            self.out.append(d)

def text(path):
    p = P()
    p.feed(open(path, encoding='utf-8', errors='replace').read())
    t = ''.join(p.out)
    t = re.sub(r'[ \t]+', ' ', t)
    t = re.sub(r'\n\s*\n+', '\n', t)
    return t

if __name__ == '__main__':
    sys.stdout.write(text(sys.argv[1]))
