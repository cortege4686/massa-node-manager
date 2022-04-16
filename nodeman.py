import json, time, datetime, re
from conf import conf_main_sleep_time
##########################
#  --------------------
##########################
timenow = datetime.datetime.now()

def write_log(msg):
    log_file = open('logs/nodeman-hidden.logs', 'a')
    log_file.write(f'{msg}\n')
    log_file.close()
    

def restart_node(inp):
    from conf import conf_node_restart

    conf_node_restart()
    write_log(f'REASON:\n{inp}\nTImE:\n{timenow}')
    print("RESTARTED")


def parser_nodov(connected):

    def save_json(inp):
        def cleaned():
            node_id = re.findall(r'Node\'s ID: (.*?) / IP', inp.split('Connected nodes:')[1])
            node_ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', inp.split('Connected nodes:')[1])
            return dict(zip(node_id, node_ip))

        with open("logs/connections.json", "r") as lc_read:
            from_file = dict(json.load(lc_read))
        with open("logs/connections.json", "w") as lc_write:
            lc_write.write(json.dumps(cleaned() | from_file))

    save_json(connected)


def node_feel_good():
    from conf import conf_node_get_status

    led, status = conf_node_get_status()
    if led == 1:
        parser_nodov(status)
    else:
        write_log('RESTART ATTEMPT')
        restart_node(status)


def main():
    while 1:
        node_feel_good()
        print('CYCLE')
        print(datetime.datetime.now())
        print(timenow)
        time.sleep(conf_main_sleep_time)


if __name__ == '__main__':
    main()
