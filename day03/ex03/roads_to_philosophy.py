import requests
from bs4 import BeautifulSoup as bs
import sys

def get_request(req):
    url = 'https://en.wikipedia.org/wiki/' + req;
    r = requests.get(url);
    if (r.status_code != 200):
        print("request error");
        exit(1);

    soup = bs(r.text, 'html.parser')
    title = str(soup.title.string).replace(' - Wikipedia', '').strip().lower();
    content = soup.find(id="mw-content-text");
    p = content.p
    b = p.b
    if (title == 'philosophy'):
        return title;
    if not b:
        print('It leads to a dead end !')
        exit(1)
    a = p.find_all('a')
    if not a:
        print('It leads to a dead end !')
        exit(1)
    for elem in a:
        if str(elem).find('title') > 0:
            target = elem['title']
            if target:
                if not target.startswith('Help:'):
                    return target

def process_request(req):
    ret = get_request(req);

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        process_request(sys.argv[1]);
