#!/usr/local/bin/python3

import sys

def get_state(test_str):
    states = {
    "Oregon"    : "OR",
    "Alabama"   : "AL",
    "New Jersey": "NJ",
    "Colorado"  : "CO"
    }
    if (test_str.upper() in [ state.upper() for state in states.keys()]):
        for state in states.keys(): 
            if (test_str.upper() == state.upper()):
                return (state)
    else:
        return (None);

def get_city(test_str):
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    if (test_str.upper() in [ city.upper() for city in capital_cities.values()]):
        for city in capital_cities.values(): 
            if (test_str.upper() == city.upper()):
                return (city);
    else:
        return (None);

def from_city_get_state(test_str):
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
    if test_str in capital_cities.values():
        for scIn1, city in capital_cities.items():
            if (city == test_str):
                for stateName, scIn2 in states.items():
                    if (scIn2 == scIn1):
                        return (stateName);

def all_in():
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
        str_arr = [ i.strip() for i in sys.argv[1].split(',')
                if i and len(i.strip()) > 0];
        for i in str_arr:
            if (get_state(i)):
                print("{} is the capital of {}".
                format(capital_cities[states[get_state(i)]], get_state(i)));
            elif (get_city(i)):
                for sc, city in capital_cities.items():
                    if (city.upper() == i.upper()):
                        print("{} is the capital of {}".format(get_city(i), 
                            from_city_get_state(get_city(i))));
            else:
                print("{} is neither a capital city nor a state".format(i));

if __name__ == '__main__':
    all_in();
