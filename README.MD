# REQ  
python3.10

$ crontab -e  
---  
SHELL=/bin/bash
*/1 * * * * /bin/bash ~/nodeman-massa/run-nodeman.sh 1>> ~/nodeman-massa/logsof-nodeman 2>> ~/nodeman-massa/errorsof-nodeman

# INSTALL  
$ sudo apt update && clear && apt list --upgradable && sudo apt upgrade && sudo apt install software-properties-common && sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt install python3.10 python3.10-venv  
$ cd ~/nodeman-massa && python3.10 -m venv venv  

# RUN  
$ 
$ screen  
---
py nodeman.py &>/dev/null

$ cd ~/nodeman-massa/shelall  
---
bash all files doljni rabotat








