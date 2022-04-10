import sys,time


path = 'logs/nodeman-hidden.logs'
sys.stdout = open(path, 'w')


def main():
    while 1:
        print('logggg')
        time.sleep(5)


if __name__ == '__main__':
    main()


