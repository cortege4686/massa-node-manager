import subprocess as sp

conf_main_sleep_time = 60


def conf_node_get_status():
    node_stat = str(sp.check_output(['bash', 'shelall/get-status.sh']))

    if 'Known peers' in node_stat:
        # 1 MEANS GREEN
        return 1, node_stat
    else:
        # 0 = RED
        return 0, node_stat



