import json, time, datetime, re
from conf import conf_main_sleep_time
###################################
#  ------------------
###############################


def the_time():
    timess = str(datetime.datetime.now())
    return timess


def write_log(msg):
    log_file = open('logs/nodeman-hidden.logs', 'a')
    log_file.write(f'{msg}\n')
    log_file.close()
    

def restart_node(inp):
    from conf import conf_node_restart
    
    conf_node_restart()
    write_log(f'REASON:\n{inp}\nTImE:\n{the_time()}')
    print("RESTARTED")


def roll_scare():
    from conf import conf_node_wallet_info
    candidate_rolls, hold_state = conf_node_wallet_info()

    if candidate_rolls <= hold_state:
        from conf import conf_node_buy_rolls
        conf_node_buy_rolls()
        write_log(f'ROLL PURCHASED\n{the_time()}')
    else:
        print(f'ROLLS {candidate_rolls}')
        pass


def parser_nodov(connected):

    def save_json(inp):
        def cleaned():
            node_id = re.findall(r'", "(.*?)"],', inp.split('Connected nodes:')[1])
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
        roll_scare()
    else:
        write_log('RESTART ATTEMPT')
        restart_node(status)


def main():
    while 1:
        node_feel_good()
        print('CYCLE')
        print(the_time())
        time.sleep(conf_main_sleep_time)


if __name__ == '__main__':
    main()
