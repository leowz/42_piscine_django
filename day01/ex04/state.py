import sys

def state():
    states = {
    "Oregon"    : "OR",
    "Alabama"   : "AL",
    "New Jersey": "NJ",
    "Colorado"  : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    if len(sys.argv) == 2:
        if sys.argv[1] in capital_cities.values():
            for scIn1, city in capital_cities.items():
                if (city == sys.argv[1]):
                    for stateName, scIn2 in states.items():
                        if (scIn2 == scIn1):
                            print(stateName);
        else:
            print("Unknown capital city");

if __name__ == '__main__':
    state();
