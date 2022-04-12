# REQ  
python3.10

# INSTALL  
$ sudo apt update && clear && apt list --upgradable && sudo apt upgrade && sudo apt install software-properties-common && sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt install python3.10 python3.10-venv python3-venv
---------------  
$ cd ~/nodeman-massa && python3.10 -m venv venv  
---  

# RUN  
$ screen -S nodeman-massa  
---  
$ cd ~/nodeman-massa && source venv/bin/activate && py nodeman.py &>/dev/null  
---  








