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
    ##### RESTART LOOP
    write_log(inp)


def node_feel_good():
    from conf import conf_node_get_status

    led,status,connected_nodes = conf_node_get_status()

    if led == 1:
        write_log(connected_nodes)
    else:
        write_log('restart attempt')
        restart_node(status)


def main():
    while 1:
        node_feel_good()
        time.sleep(conf_main_sleep_time)


if __name__ == '__main__':
    main()




