import time, subprocess as sp
from conf import *
##########################
#  for conf_* look conf.py
##########################


def write_log(msg):
    log_file = open('logs/nodeman-hidden.logs', 'a')
    log_file.write(f'{msg} \n')
    log_file.close()


def get_node_stat():
    node_stat = str(conf_bash_node_get_status)
    return node_stat


def restart_node(inp):
    print(inp)


def node_feel_good():
    def restart_loop():
        sleep = 5

    if 'Known Peers' in get_node_stat():
        pass
    else:
        write_log(get_node_stat())


def main():
    while 1:
        write_log('workornot')
        node_feel_good()
        time.sleep(conf_main_sleep_time)


if __name__ == '__main__':
    main()




