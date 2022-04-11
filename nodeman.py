import time, subprocess as sp


def write_log(msg):
    log_file = open('logs/nodeman-hidden.logs', 'a')
    log_file.write(f'{msg} \n')
    log_file.close

def node_get_status():
    node_stat = str(sp.check_output(['bash', 'shelall/get-status.sh']))
    return node_stat

def main():
    while 1:
        write_log('workornot')
        print(node_get_status())
        time.sleep(5)


if __name__ == '__main__':
    main()


