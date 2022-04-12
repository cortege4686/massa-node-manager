import subprocess as sp

conf_main_sleep_time = 222

### EDIT TO GET CORRECT IF YOYRE BINARY
##########################################################################

def conf_node_get_status():
    node_stat = str(sp.check_output(['bash', 'shelall/get-status.sh']))
    return node_stat

