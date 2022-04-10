import sys,time


def makelog(filename, text):
    path = f'logs/{filename}'
    sys.stdout = open(path, 'w')
    print(text)


def main():
    while 1:
        makelog('nodeman-hidden.logs', 'da eto logi')
        time.sleep(5)


if __name__ == '__main__':
    main()


