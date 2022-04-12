import time
from conf import conf_main_sleep_time
##########################
#  --------------------
##########################


def write_log(msg):
    log_file = open('logs/nodeman-hidden.logs', 'a')
    log_file.write(f'{msg}\n')
    log_file.close()
    

def restart_node(inp):
    print(inp)


def node_feel_good():
    from conf import conf_node_get_status

    led,status = conf_node_get_status()

    if led == 1:
        write_log('YES WORK')
    else:
        write_log('not work')
        write_log(status)


def main():
    while 1:
        write_log('workornot')
        node_feel_good()
        time.sleep(conf_main_sleep_time)


if __name__ == '__main__':
    main()




