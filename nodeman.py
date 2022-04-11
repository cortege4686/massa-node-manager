import sys,time


def write_log(msg):
    log_file = open('logs/nodeman-hidden.logs', 'a')
    log_file.write(f'{msg} \n')
    log_file.close


def main():
    while 1:
        write_log('workornot')
        time.sleep(5)


if __name__ == '__main__':
    main()


