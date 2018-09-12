#!/usr/bin/env python

list_of_hosts = [] # create empty list
Hosts = ""
while Hosts != 'Quit':
      Hosts = raw_input("Please enter ip address of the hosts, type 'Quit' to terminate \n")
      if Hosts != 'Quit': 
         list_of_hosts.append(Hosts)

print(list_of_hosts)

file_host = open('host_to_check', 'w')

for host in list_of_hosts:
    file_host.write('%s\n' % host)


