# REQ  
python3.10

## crontab  
SHELL=/bin/bash
*/1 * * * * /bin/bash ~/nodeman-massa/run-nodeman.sh 1>> ~/nodeman-massa/logsof-nodeman 2>> ~/nodeman-massa/errorsof-nodeman


