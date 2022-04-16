import subprocess as sp


conf_main_sleep_time = 60
how_much_rolls_you_want_to_hold = 0


def conf_node_buy_rolls():
    sp.run(['bash', 'shelall/buy-roll.sh'])
### change wallet adress -> shelall/buy-roll.sh

def conf_node_restart():
    sp.run(['bash', 'shelall/run-screen-and-node.sh'])

def conf_node_get_status():
    node_stat = str(sp.check_output(['bash', 'shelall/get-status.sh']))

    if 'Network stats:' in node_stat:
        # 1 MEANS GREEN
        return 1, node_stat 
    else:
        # 0 = RED
        return 0, node_stat


def conf_node_wallet_info():
    wallet_info = str(sp.check_output(['bash', 'shelall/wallet-info.sh']))
    rolls_candidate = wallet_info.split('Candidate rolls: ')[1]
    return int(rolls_candidate.split(' =')[0]), how_much_rolls_you_want_to_hold



