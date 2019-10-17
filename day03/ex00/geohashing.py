#!/usr/local/bin/python3
import sys
import antigravity

def geohash(lat, longi, datedow):
    antigravity.geohash(lat, longi, datedow);

if __name__ == '__main__':
    if (len(sys.argv) == 4):
        try:
            geohash(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3].encode('ascii'))
        except ValueError as ve:
            print("Value Error", ve);
        except Exception as e:
            print(e);
    else:
        print("Usage : geohashing.py latitude longitude datedow");
