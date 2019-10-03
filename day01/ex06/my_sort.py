def cmp_by_year(e):
    return int(e[1]);

def cmp_by_name(e):
    return e[0];

def my_sort():
    d={
    'Hendrix'   :   '1942',
    'Allman'    :   '1946',
    'King'      :   '1925',
    'Clapton'   :   '1945',
    'Johnson'   :   '1911',
    'Berry'     :   '1926',
    'Vaughan'   :   '1954',
    'Cooder'    :   '1947',
    'Page'      :   '1944',
    'Richards'  :   '1943',
    'Hammett'   :   '1962',
    'Cobain'    :   '1967',
    'Garcia'    :   '1942',
    'Beck'      :   '1944',
    'Santana'   :   '1947',
    'Ramone'    :   '1948',
    'White'     :   '1975',
    'Frusciante':   '1970',
    'Thompson'  :   '1949',
    'Burton'    :   '1939',
    }
    sort_ret = sorted(sorted(d.items(), key=cmp_by_name), 
            key=cmp_by_year);
    for name, year in sort_ret:
        print(name);

if __name__ == '__main__':
    my_sort();
