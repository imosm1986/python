#!/usr/bin/env python

import os
import datetime
from easysnmp  import Session

#Get ip address from the user and store it in a file

my_dict = dict()

#list_of_hosts = [] # create empty list
Hosts = ""
while Hosts != 'Run':
      Hosts = raw_input("Please enter ip address and community string of the host seperated by(,) : \n")
      #community_string =raw_input("Please enter community string for the above host \n")
      print("Type 'Run' to run the program")
      if Hosts != 'Run':
         k,v = Hosts.split(",")  
         my_dict[k] = v

print(my_dict)

#f = open('host_to_check.txt', 'w')

#for host,string in my_dict :
#    f.write('%s\n' % host)

#Open file and loop through all devices

#f=open('host_to_check.txt')

for h,s in my_dict.iteritems():
    device=h
    community_string=s
#    print(device)
#    print(community_string)
 #getting current date and time
    i=datetime.datetime.now()
#Create a SNMP session to be used for all our requests
    session = Session(hostname=device, community=community_string,version=2)
#MIB to get the number of interfaces
    Interfaces = session.walk('1.3.6.1.2.1.2.2.1.2')
    x=len(Interfaces)
#Looping through list to get the value of OID
    Interfaces_desc = session.walk('1.3.6.1.2.1.31.1.1.1.18')   #description
    Interfaces_status = session.walk('1.3.6.1.2.1.2.2.1.8')     #interface status
    hostname = session.walk('1.3.6.1.2.1.1.5')                  #hostname
    f1=open('free-core-ports.txt','a')
    f1.write("%s" %i)
    f1.write('\n*****Running Program Now*****\n')
    f1.write('\nDevice is**' + str(hostname[0].value) + '**' + '\n')
    f1.write('Interface Name     Description\n')
#looping through all interfaces
    n=0
    for x in range (0,len(Interfaces)) :
#if description [CUST] then mark the port as Customer port
        if(Interfaces_desc[x].value == '[CUST]') and (Interfaces_status[x].value =='2'):
           f1.write(Interfaces[x].value + '=== **[CUST]**\n') 
           n=n+1
        #else:
          # print(Interfaces[x].value + '===' + Interfaces_desc[x].value)
    f1.write('\nTotal Number of Customer Ports on '+device+' are '+str(n))
    f1.write('\n-----------------------------------\n')
#f.close()
# delete the file
#os.remove('host_to_check.txt')
import sendtoteam

