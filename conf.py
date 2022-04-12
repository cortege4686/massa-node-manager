import subprocess as sp

conf_main_sleep_time = 60


def conf_node_get_status():
    node_stat = str(sp.check_output(['bash', 'shelall/get-status.sh']))

    if 'Network stats:' in node_stat:
        # 1 MEANS GREEN
        return 1, node_stat, node_stat.split('Connected nodes:')[1]
    else:
        # 0 = RED
        return 0, node_stat, ''




