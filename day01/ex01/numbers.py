def numbers():
    f = open('./numbers.txt', 'r');
    data = f.read();
    f.close();
    ret = data.split(',');
    for i in ret:
        print(i);

if __name__ == '__main__':
    numbers();

