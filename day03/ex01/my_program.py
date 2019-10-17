#!/usr/local/bin/python3
from local_lib.path import Path

if __name__ == '__main__':
    d = Path('./tmp');
    d.mkdir_p();
    f = Path('./tmp/test');
    f.touch();
    f.open();
    f.write_text("some texts and more texts");
    print(f.text());
