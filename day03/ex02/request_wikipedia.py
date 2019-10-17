import requests
import json
import dewiki
import sys

def write_to_file(name, txt):
    filename = name.replace(" ", "_") + ".wiki"
    try:
        with open(filename, 'w') as f:
            f.write(txt);
    except Exception as e:
        print("io error" ,e);

def wiki(req):
    url = "https://en.wikipedia.org/w/api.php";
    payload = {'action':'query', 'titles':req, 'prop':'revisions','rvprop':'content','format':'json'};
    r = requests.get(url, params=payload);
    if (r.status_code ) != 200:
        print("request error")
        return ;
    res = r.json();
    try:
        txt = "";
        for pageid in res['query']['pages']:
            txt += res['query']['pages'][pageid]['revisions'][0]['*'] + '\n';
        write_to_file(req, dewiki.from_string(txt));
    except Exception as e:
        print("request error", e);
        print("The term might not exist")
        return;

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        wiki(sys.argv[1]);
