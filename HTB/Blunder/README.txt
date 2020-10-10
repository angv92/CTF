
1. Recon : Directory enumeration and nmap scan ofc 

nmap scan reveals port 80 (open), 21 (Closed)
21/tcp closed ftp
80/tcp open   http    Apache httpd 2.4.41 ((Ubuntu))

run gobuster with dirb/common.txt and extentions php,js,html,htm,txt,py,sh

- /admin (login panel)
- /todo.txt - found username (fergus)

2. Gain access through the admin panel
- try defaults with admin:password admin:admin etc. - FAILURE
- use sqlmap against the panel - FAIURE
- use rockyou.txt and hydra to bruteforce. Theres a blacklisting of IP address - FAILURE
- Google shows that theres a bruteforce script to avoid lockout. Use rockyou.txt - FAILURE
- Use CEWL to create a wordlist from the words available on the site. Create password list and then bruteforce from there. Success. 

CREDENTIALS - fergus:RolandDeschain

3. Try an upload a shell or revserse shell. 
- searched searchsploit for bludit. Found a poc. Tried it but it would not let me upload straight php files - FAILURE
- tried to upload part of a png with a php at the end or in the middle. - FAILURE
- Looking at using msfconsole -- found an exploit that may work. Lets try that. 

