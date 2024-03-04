1) Which of the following is a very first requirement to assign an IP address to a system?

a) The system must be connected to the Internet.
b) The system must be connected to a network.
c) The system must be connected to a gateway.
d) The system must be connected to a router.

answer: c
system must have a physical or virtual network interface attached to it.

2) On a Linux based system which of the following command can be used to display the kernel ip routing table.

a) ip route show
b) route show
c) ip route list
d) route list

answer: c or simply route

3) Can we assign multiple IPs to a system?

a) Yes
b) No
answer: a

4) Which of the following is preferred device to connect two system which are on different networks?

For example, if System A is on 192.168.1.0/24 network and System B is on 192.168.2.0/24 network.

a) gateway
b) router
c) switch
d) bridge

answer: router

[//]: # (5&#41; What is the default gateway?)

[//]: # (   Its default gateway is 244.178.44.111)

5) Can a gateway connect a system to the internet?
Answer: Yes
        
6) We have four app server from app01 to app04. You can access each app from jump host using command ssh app01 and similarly for other apps. Assign new IPs to each host as per details given below:


a. Assign 172.16.238.15/24 ip address to app01

b. Assign 172.16.238.16/24 ip address to app02

c. Assign 172.16.239.15/24 ip address to app03

d. Assign 172.16.239.16/24 ip address to app04

e. We also need to remove existing IPs from these apps after assigning them new IPs but do not remove them right now as it can break your connection, if you are sure you are done with required changes just click on Check button below, it will do the rest.

Warning: If changes aren't made correctly it can break your connection to the environment and you may need to reload the lab.




Apply for app01

Apply for app02

Apply for app03

Apply for app04

Note: Please ensure to execute the commands on their respective app nodes.



To assign new IPs for app01 , the below command need to be executed on app01.

For app01: sudo ip addr add 172.16.238.15/24 dev eth0

Please follow the same procedure for other app nodes as well:

For app02: sudo ip addr add 172.16.238.16/24 dev eth0

For app03: sudo ip addr add 172.16.239.15/24 dev eth0

For app04: sudo ip addr add 172.16.239.16/24 dev eth0


6) Now if you try to SSH into each app one by one from jump host you will find that you are able to SSH into app01 and app02 but not into app03 and app04. Why so ?

answer : App3 and 4 are different network ranges now.

7) Since now app03 and app04 are on different network range than jump host so you are not able to SSH into those hosts from jump host. To make SSH work make required changes on jump host.


a. Assign a new IP address 172.16.239.10/24 to jump host with same network range which app03 and app04 are using.

b. Now you will be able to SSH into all apps from jump host.

NOTE: - After the change, you may experience a delay when trying to SSH from the jump server to the app servers.

9) Now jump host is able to access all four apps. But if you try to ping app03 or app04 from app01 or app02 or vice versa you will see ping is not working. So now we want to use jump host as a router so that app01 and app02 can access app03 and app04 and vice versa, lets add some routing table entries on these hosts to make it work.


a. Add a routing table entry in app01 and app02 hosts so that these hosts can reach app03 and app04 hosts via jump host.

b. Add a routing table entry in app03 and app04 hosts so that these hosts can reach app01 and app02 hosts via jump host.

c. Now try to ping app03 and app04 from app01 and app02 and vice versa, every app should be able to ping each other.




Verify app01 is able to ping app02, app03 and app04

Verify app02 is able to ping app01, app03 and app04

Verify app03 is able to ping app01, app02 and app04

Verify app04 is able to ping app01, app02 and app03




