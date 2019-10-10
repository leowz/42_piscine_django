import sys
import os
import re

def file_check(fn):
    try:
      open(fn, "r")
      return 1
    except IOError:
      print("Error: File {0} does not appear to exist.".format(fn))
      return 0

def read_settings():
    ret  = {};
    with open('settings.py') as f:
        for line in f:
            data = line.split('=');
            ret[data[0].strip(" ")] = data[1].strip("\n \r");
        return ret;

def render():
    settings = None;
    if (not (file_check('settings.py'))):
        return ;
    else:
        settings = read_settings();

    if (len(sys.argv) == 2 and file_check(sys.argv[1])):
        with open(sys.argv[1], 'r') as f:
            for line in f:
                for key,val in settings.items():
                    reg = "{%s}"%key;
                    line = re.sub(reg, val, line); 
                print(line, end="");

if __name__ == '__main__':
    if (len(sys.argv) == 2 and sys.argv[1].endswith('.template')):
        render();
    elif (len(sys.argv) == 2 and not sys.argv[1].endswith('.template')):
        print("Error: only take file with extension template");
