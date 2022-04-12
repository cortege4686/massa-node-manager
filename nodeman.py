import json, time, re
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


def parser_nodov(connected):

    def save_json(inp):
        def cleaned(i):
            node_id = re.findall(r'Node\'s ID: (.*?) / IP', i)
            node_ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', i)
            return dict(zip(node_id, node_ip))

        with open("logs/connections.json", "r") as lc_read:
            from_file = dict(json.load(lc_read))
        with open("logs/connections.json", "w") as lc_write:
            lc_write.write(json.dumps(cleaned(inp) | from_file))

    save_json(connected)


def node_feel_good():
    from conf import conf_node_get_status

    led, status, connected_nodes = conf_node_get_status()
    if led == 1:
        parser_nodov(connected_nodes)
    else:
        write_log('restart attempt')
        restart_node(status)


def main():
    while 1:
        node_feel_good()
        time.sleep(conf_main_sleep_time)


if __name__ == '__main__':
    main()




