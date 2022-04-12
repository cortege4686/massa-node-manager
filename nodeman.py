import time, subprocess as sp


def write_log(msg):
    log_file = open('logs/nodeman-hidden.logs', 'a')
    log_file.write(f'{msg} \n')
    log_file.close


def get_node_stat():
    node_stat = str(sp.check_output(['bash', 'shelall/get-status.sh']))
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
        time.sleep(120)


if __name__ == '__main__':
    main()




