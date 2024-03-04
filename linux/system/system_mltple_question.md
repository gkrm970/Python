1) Which of the following is not valid systemctl command?

#### following command are valid
1) systemctl start httpd
2) systemctl stop httpd
3) systemctl restart httpd
4) systemctl enable httpd
5) systemctl disable httpd
6) systemctl status httpd
7) systemctl reload httpd
8) systemctl daemon-reload
9) systemctl daemon-restart httpd
10) systemctl daemon-enable httpd
11) systemctl daemon-disable httpd
12) systemctl daemon-status httpd
13) systemctl daemon-reload httpd
14) systemctl daemon-restart httpd
15) systemctl daemon-enable httpd
16) systemctl daemon-disable httpd
17) systemctl daemon-status httpd

#### following commands are invalid
1) systemctl httpd start
2) systemctl httpd stop
3) systemctl httpd restart
4) systemctl httpd enable
5) systemctl httpd disable
6) systemctl httpd status
7) systemctl httpd reload
8) systemctl httpd daemon-reload
9) systemctl httpd daemon-restart
10) systemctl httpd daemon-enable
11) systemctl httpd daemon-disable
12) systemctl httpd daemon-status
13) systemctl httpd daemon-reload
14) systemctl httpd daemon-restart
15) systemctl httpd daemon-enable
16) systemctl httpd daemon-disable
17) systemctl httpd daemon-status


2) What is the status of httpd service?

We have pre-installed httpd (apache package) which is used for hosting web server.


NOTE: Don't forget to make use of the sudo command.
thor@host01 ~$ sudo systemctl status httpd
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset: disabled)
   Active: inactive (dead)
     Docs: man:httpd(8)
           man:apachectl(8)
thor@host01 ~$

3) Let's start httpd service so that our host01 can act as web server.


We have pre-installed httpd (apache package) which is used for hosting web server.


NOTE: Don't forget to make use of the sudo command.

thor@host01 ~$ sudo systemctl start httpd
thor@host01 ~$


4) Now we have to enable httpd service so that it starts automatically when system boots up and we dont need to manually start the service.


thor@host01 ~$ sudo systemctl enable httpd
thor@host01 ~$

5) Now we decided to use dedicated python flask app instead of apache so please stop httpd service.

thor@host01 ~$ sudo systemctl stop httpd
thor@host01 ~$

6) Now we have to disable httpd service so that it doesn't start automatically when system boots up.

thor@host01 ~$ sudo systemctl disable httpd
thor@host01 ~$

7) We have added a new python flask based service called app. In which systemd unit file is this service configured?


thor@host01 ~$ sudo systemctl edit app.service
thor@host01 ~$
location of the file is /etc/lib/systemd/system/app.service

8) What is the status of app service?

thor@host01 ~$ sudo systemctl status app
● app.service - My python web application
   Loaded: loaded (/usr/lib/systemd/system/app.service; disabled; vendor preset: disabled)
   Active: inactive (dead)
thor@host01 ~$ 


9) Look at the service configuration file (systemd unit file) and identify which script is run before the app service starts.






