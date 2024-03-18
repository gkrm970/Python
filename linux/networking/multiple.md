### At basic level what is DNS used for ?
Answer: DNS is used to map domain names to IP addresses or to resolve Ip od domain name.

### On a Linux based system, which of the following file can be used to point domains/hostnames to IPs locally?
Answer: /etc/hosts

### On a Linux based system, which of the following command can be used to display the kernel ip routing table?
Answer: ip route show

### On a Linux based system, which of the following file contains information about dns server i.e nameserver?
Answer: /etc/resolv.conf

### On host01, if we have an entry for app01 in /etc/hosts file like 172.168.238.12 app01 and the DNS server which is used by host01 has 172.168.239.10 as app01's IP then which IP host01 will pick for app01 as per priority.
Answer: 172.168.238.12

In this scenario, host01 will prioritize the IP address listed in its local /etc/hosts file for app01. This means it will use 172.168.238.12 to resolve app01, even though the DNS server has a different IP (172.168.239.10) listed for the same hostname.

The reason for this behavior is that the /etc/hosts file is a local configuration file that takes precedence over DNS servers for hostname resolution. This allows hosts to have specific hostnames mapped to specific IP addresses, regardless of what the DNS server might return.

### On host01, point www.google.com to 127.0.0.1 IP address locally.
Answer: 
While modifying the /etc/hosts file to point www.google.com to 127.0.0.1 on host01 might seem like a quick solution, it's important to understand the implications before proceeding:

Limited Impact: This change will only affect host01 itself. Any other devices on your network will still access the real Google website through the proper DNS resolution process.
Disrupts Functionality: Pointing www.google.com to 127.0.0.1 essentially prevents you from accessing the actual Google website from host01. You'll only be able to access local resources running on host01 that might be using the same domain name (www.google.com).
Unexpected Behavior: Websites and applications that rely on external resources like Google APIs or services might malfunction due to the inability to access the real Google website.
Therefore, it's generally not recommended to modify the /etc/hosts file for this purpose. If you have a specific reason for achieving a similar outcome, it's advisable to explore alternative solutions that don't involve altering system-wide configurations or potentially disrupting other functionalities.

### On host01, add Google public DNS i.e 8.8.8.8 as a nameserver

Answer: 
There are two main approaches to adding Google Public DNS (8.8.8.8) as a nameserver on host01:

1. Modifying /etc/resolv.conf file:

This method involves editing the system-wide configuration file for DNS resolution. Be cautious when editing this file, as errors can lead to internet connectivity issues.

Steps:

Gain administrative privileges: Use sudo or log in as root to edit the file.
Open the file: Use a text editor like nano or vim:
Bash
sudo nano /etc/resolv.conf
Use code with caution.
Add the nameserver: Add a new line at the end of the file with the following entry:
nameserver 8.8.8.8


### In www.google.com, which is the top level domain?
Answer: .com

### Which of the following is a sub-domain example?
Answer: 
Out of the following options, mail.google.com is a sub-domain example.

Here's why:

Subdomain: A subdomain is a prefix added to the main domain name, separated by a dot (.). It helps organize and categorize different sections of a website.
mail.google.com: In this case, "mail" is the subdomain, "google" is the main domain name, and ".com" is the top-level domain (TLD). "mail.google.com" specifically directs users to the email service offered by Google.
The other options are not subdomains:

[invalid URL removed]: This is the main domain name itself, not a subdomain.
www.google.com: While commonly used, "www" is actually a subdomain traditionally used for the main website content. However, its use is increasingly optional and doesn't necessarily indicate a separate section within the website.
127.0.0.1: This is a loopback address that points to the local machine itself, not related to domain names or subdomains.

### On host01 we want to resolve name news to news.yahoo.com automatically without hard coding its entry in /etc/hosts file. Add the required changes on host01.
answer: Modifying the system-wide configuration for all users on host01 to resolve "news" to "news.yahoo.com" is generally not recommended as it can have unintended consequences and affect other applications relying on proper hostname resolution. However, you can achieve a similar outcome within a specific user's environment without modifying the /etc/hosts file or affecting other users.

Here's an approach using environment variables:

Set the environment variable: Open a terminal window and type the following command, replacing <username> with the actual username of the user:
Bash
export NEWS_URL="news.yahoo.com"
Use code with caution.
This command creates an environment variable named NEWS_URL and assigns the value "news.yahoo.com" to it.

Modify the application's behavior:
Command-line tools: If the application uses the $NEWS_URL environment variable, it will automatically resolve "news" to "news.yahoo.com".
Scripting languages: You can incorporate the environment variable within your scripts to access the desired URL dynamically. For example, in Python:
Python
import os

news_url = os.environ.get('NEWS_URL')

# Use news_url for your news-related task
print(f"News URL: {news_url}")
Use code with caution.
Limitations:
This approach only works within the specific user's environment where the variable is set. Other users on host01 or the system-wide behavior will remain unchanged.
Applications need to be designed to understand and utilize environment variables for this method to be effective.
Remember, this approach is specific to a user's environment and should be used cautiously to avoid unintended system-wide configurations.

### Which of the following command is used to query a hostname from a DNS server?
Answer: nslookup

The nslookup command is a versatile tool for querying DNS servers. It allows you to perform various tasks, including:

Forward lookup: This is the most common usage, where you provide a hostname and it retrieves the corresponding IP address from the DNS server. For example:
nslookup google.com
Reverse lookup: This allows you to provide an IP address and retrieve the associated hostname. For example:
nslookup 8.8.8.8
Query specific DNS servers: You can specify a particular DNS server to query by adding its address after the server keyword. For example:
nslookup google.com server 8.8.8.8
In summary, nslookup is the primary command-line tool for interacting with DNS servers and querying hostnames for their corresponding IP addresses.

### Install python3.6 in host01 server We removed python3. You can confirm by running python3 -V
answer: 


